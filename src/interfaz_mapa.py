import os
import sys
import json # Agregado para el historial
import tkinter as tk
from tkinter import ttk
from datetime import datetime # Agregado para la fecha
from PIL import Image, ImageTk

# Importamos los datos de tu otro archivo
from grafo_ciudades import grafo, coordenadas
from busqueda import a_estrella

def recurso_ruta(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------- LÓGICA DE PERSISTENCIA (AGREGADO) ----------------

def guardar_en_historial(origen, destino, distancia, ruta):
    archivo = "historial_rutas.json"
    nuevo_registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "origen": origen,
        "destino": destino,
        "distancia": f"{round(distancia, 2)} km",
        "ruta": " -> ".join(ruta)
    }
    
    datos = []
    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
        except: datos = []
    
    datos.append(nuevo_registro)
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def abrir_historial():
    ventana_h = tk.Toplevel(ventana)
    ventana_h.title("Historial de Rutas Optimizadas")
    ventana_h.geometry("700x400")
    
    columnas = ("fecha", "origen", "destino", "distancia")
    tabla = ttk.Treeview(ventana_h, columns=columnas, show="headings")
    for col in columnas: tabla.heading(col, text=col.capitalize())
    tabla.pack(expand=True, fill="both", padx=10, pady=10)
    
    if os.path.exists("historial_rutas.json"):
        with open("historial_rutas.json", "r", encoding="utf-8") as f:
            for r in reversed(json.load(f)):
                tabla.insert("", "end", values=(r["fecha"], r["origen"], r["destino"], r["distancia"]))

# ---------------- CONFIGURACIÓN DE ESTILO ----------------
COLOR_FONDO = "#F8FAFC"      
COLOR_PRIMARIO = "#2563EB"   
COLOR_SECUNDARIO = "#1E293B" 
COLOR_TARJETA = "#FFFFFF"    
COLOR_ACENTO = "#F1F5F9"     
COLOR_GRIS_PUNTO = "#94A3B8" # Gris más oscuro para cubrir mejor el mapa
COLOR_ORIGEN = "#10B981"     
COLOR_DESTINO = "#EF4444"    
COLOR_INTERMEDIO = "#6366F1" 
FUENTE_TITULO = ("Segoe UI", 16, "bold")
FUENTE_TEXTO = ("Segoe UI", 10)
FUENTE_BOLD = ("Segoe UI", 10, "bold")

# ---------------- LÓGICA DE INTERFAZ ----------------

def limpiar_mapa():
    canvas.delete("ruta")
    canvas.delete("puntos_destacados")

def marcar_ciudad(ciudad, tipo="intermedio"):
    if ciudad not in coordenadas: return
    x, y = coordenadas[ciudad]
    
    if tipo == "origen":
        color, radio = COLOR_ORIGEN, 7
        etiqueta = "Inicio"
    elif tipo == "destino":
        color, radio = COLOR_DESTINO, 7
        etiqueta = "Llegada"
    else:
        color, radio = COLOR_INTERMEDIO, 5
        etiqueta = ""

    # Dibujamos con un borde blanco para que resalte y tape el mapa base
    canvas.create_oval(x-radio, y-radio, x+radio, y+radio, 
                       fill=color, outline="white", width=2, tags="puntos_destacados")
    if etiqueta:
        canvas.create_text(x, y-18, text=etiqueta, fill=COLOR_SECUNDARIO, 
                           font=("Segoe UI", 8, "bold"), tags="puntos_destacados")

def actualizar_vista_previa(event=None):
    canvas.delete("puntos_destacados")
    origen = combo_origen.get()
    destino = combo_destino.get()
    if origen: marcar_ciudad(origen, "origen")
    if destino: marcar_ciudad(destino, "destino")

def animar_segmento(ruta, indice, distancia_total):
    if indice < len(ruta) - 1:
        marcar_ciudad(ruta[indice + 1], "intermedio" if indice + 1 < len(ruta)-1 else "destino")
        
        x1, y1 = coordenadas[ruta[indice]]
        x2, y2 = coordenadas[ruta[indice + 1]]
        
        # Aumentamos los pasos para que la línea crezca más "pixel a pixel"
        pasos = 25  # Antes eran 10 o 12. Más pasos = más fluidez.
        dx, dy = (x2 - x1) / pasos, (y2 - y1) / pasos

        def dibujar_paso(p):
            if p <= pasos:
                canvas.create_line(x1 + dx*(p-1), y1 + dy*(p-1), x1 + dx*p, y1 + dy*p,
                                 fill=COLOR_PRIMARIO, width=5, capstyle="round", tags="ruta")
                
                # Aumentamos el tiempo de espera entre cada micro-tramo
                # 40ms es una velocidad cómoda (similar a 25 cuadros por segundo)
                ventana.after(40, lambda: dibujar_paso(p + 1)) 
            else:
                # Tiempo de espera al llegar a una ciudad antes de seguir a la otra
                ventana.after(300, lambda: animar_segmento(ruta, indice + 1, distancia_total))
        dibujar_paso(1)
    else:
        marcar_ciudad(ruta[0], "origen")
        marcar_ciudad(ruta[-1], "destino")
        resultado_label.config(text=f"✅ {round(distancia_total, 2)} km", fg=COLOR_PRIMARIO)
        info_ruta.config(text=f"Ruta óptima trazada:\n{' ➔ '.join(ruta)}")
        # GUARDAR EN HISTORIAL (AGREGADO)
        guardar_en_historial(ruta[0], ruta[-1], distancia_total, ruta)

def iniciar_busqueda():
    limpiar_mapa()
    origen, destino = combo_origen.get(), combo_destino.get()
    
    if not origen or not destino or origen == destino:
        resultado_label.config(text="⚠️ Selección inválida", fg=COLOR_DESTINO)
        return

    ruta, distancia = a_estrella(origen, destino)

    if ruta:
        marcar_ciudad(origen, "origen")
        animar_segmento(ruta, 0, distancia)
    else:
        resultado_label.config(text="❌ Sin conexión terrestre", fg=COLOR_DESTINO)
        info_ruta.config(text="No hay una ruta registrada entre estas ciudades en el grafo actual.")

# ---------------- VENTANA PRINCIPAL ----------------
ventana = tk.Tk()
ventana.title("Navega por Colombia Pro")
ventana.geometry("1100x680")
ventana.configure(bg=COLOR_FONDO)

main_container = tk.Frame(ventana, bg=COLOR_FONDO)
main_container.pack(expand=True, fill="both", padx=40, pady=30)

# --- PANEL IZQUIERDO: MAPA ---
map_card = tk.Frame(main_container, bg=COLOR_TARJETA, highlightthickness=1, highlightbackground="#E2E8F0")
map_card.pack(side="left", fill="both", expand=True)

canvas = tk.Canvas(map_card, width=600, height=500, bg="white", highlightthickness=0)
canvas.pack(padx=20, pady=20)

try:
    ruta_mapa = recurso_ruta("src/mapa_colombia.png")
    img_mapa = ImageTk.PhotoImage(Image.open(ruta_mapa).resize((600, 500)))
    canvas.create_image(0, 0, anchor="nw", image=img_mapa)
except:
    canvas.create_text(300, 250, text="Error: No se encontró mapa_colombia.png")

# Dibujar ciudades base (Gris un poco más grandes para tapar el rojo del PNG)
for c, (x, y) in coordenadas.items():
    canvas.create_oval(x-4, y-4, x+4, y+4, fill=COLOR_GRIS_PUNTO, outline="white", width=1)

# --- PANEL DERECHO: CONTROL ---
control_panel = tk.Frame(main_container, bg=COLOR_TARJETA, width=380, padx=30, pady=30, highlightthickness=1, highlightbackground="#E2E8F0")
control_panel.pack(side="right", fill="y", padx=(20, 0))
control_panel.pack_propagate(False) # Mantiene el ancho fijo

tk.Label(control_panel, text="Navega por Colombia", font=FUENTE_TITULO, bg=COLOR_TARJETA, fg=COLOR_SECUNDARIO).pack(anchor="w")
tk.Label(control_panel, text="Inteligencia Artificial aplicada", font=FUENTE_TEXTO, bg=COLOR_TARJETA, fg="#64748B").pack(pady=(0, 20), anchor="w")

# Selectores
tk.Label(control_panel, text="📍 Ciudad de Origen", font=FUENTE_BOLD, bg=COLOR_TARJETA).pack(anchor="w")
combo_origen = ttk.Combobox(control_panel, values=sorted(grafo.keys()), font=FUENTE_TEXTO, state="readonly")
combo_origen.pack(fill="x", pady=(5, 15))
combo_origen.bind("<<ComboboxSelected>>", actualizar_vista_previa)

tk.Label(control_panel, text="🏁 Ciudad de Destino", font=FUENTE_BOLD, bg=COLOR_TARJETA).pack(anchor="w")
combo_destino = ttk.Combobox(control_panel, values=sorted(grafo.keys()), font=FUENTE_TEXTO, state="readonly")
combo_destino.pack(fill="x", pady=(5, 25))
combo_destino.bind("<<ComboboxSelected>>", actualizar_vista_previa)

btn_buscar = tk.Button(control_panel, text="TRAZAR RECORRIDO", bg=COLOR_PRIMARIO, fg="white", font=FUENTE_BOLD, 
                      relief="flat", pady=15, cursor="hand2", command=iniciar_busqueda)
btn_buscar.pack(fill="x")

# BOTÓN HISTORIAL (AGREGADO)
btn_historial = tk.Button(control_panel, text="REVISAR HISTORIAL", bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOLD, 
                         relief="flat", pady=10, cursor="hand2", command=abrir_historial)
btn_historial.pack(fill="x", pady=10)

# --- ÁREA DE INFORMACIÓN (CORREGIDA) ---
# Usamos un frame con padding para simular la tarjeta de resultados
result_card = tk.Frame(control_panel, bg=COLOR_ACENTO, padx=15, pady=15)
result_card.pack(fill="both", expand=True, pady=20)

resultado_label = tk.Label(result_card, text="Sistema en espera", font=FUENTE_BOLD, bg=COLOR_ACENTO, fg="#475569", anchor="w")
resultado_label.pack(fill="x")

# El wraplength de 280 evita que el texto se salga del recuadro
# --- REEMPLAZA SOLO ESTA PARTE DEL info_ruta ---
info_ruta = tk.Label(
    result_card, 
    text="Selecciona el origen y destino para calcular la ruta más corta.", 
    font=("Segoe UI", 9), 
    bg=COLOR_ACENTO, 
    fg="#64748B", 
    justify="left", 
    wraplength=250, # Bajamos a 250 para evitar que choque con los bordes
    anchor="nw"
)
info_ruta.pack(fill="both", expand=True, pady=(10, 0))

ventana.mainloop()