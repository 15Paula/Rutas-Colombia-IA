import tkinter as tk
from tkinter import ttk, messagebox

from busqueda import costo_uniforme, profundidad, voraz, a_estrella
from grafo_ciudades import grafo


# ---------------- FUNCION PRINCIPAL ----------------
def calcular_rutas():
    origen = combo_origen.get()
    destino = combo_destino.get()

    if origen not in grafo or destino not in grafo:
        messagebox.showerror("Error", "Selecciona ciudades válidas")
        return

    resultado_text.delete("1.0", tk.END)

    resultado_text.insert(tk.END, f"Ruta: {origen} → {destino}\n\n")

    # Costo uniforme
    ruta_cu, dist_cu = costo_uniforme(origen, destino)
    resultado_text.insert(tk.END, "Costo Uniforme:\n")
    if ruta_cu:
        resultado_text.insert(tk.END, f"{' -> '.join(ruta_cu)}\nDistancia: {dist_cu} km\n\n")
    else:
        resultado_text.insert(tk.END, "No hay ruta\n\n")

    # Profundidad
    ruta_prof = profundidad(origen, destino)
    resultado_text.insert(tk.END, "Profundidad:\n")
    if ruta_prof:
        resultado_text.insert(tk.END, f"{' -> '.join(ruta_prof)}\n\n")
    else:
        resultado_text.insert(tk.END, "No hay ruta\n\n")

    # Voraz
    ruta_v = voraz(origen, destino)
    resultado_text.insert(tk.END, "Voraz:\n")
    if ruta_v:
        resultado_text.insert(tk.END, f"{' -> '.join(ruta_v)}\n\n")
    else:
        resultado_text.insert(tk.END, "No hay ruta\n\n")

    # A*
    ruta_a, dist_a = a_estrella(origen, destino)
    resultado_text.insert(tk.END, "A*:\n")
    if ruta_a:
        resultado_text.insert(tk.END, f"{' -> '.join(ruta_a)}\nDistancia: {dist_a} km\n\n")
    else:
        resultado_text.insert(tk.END, "No hay ruta\n\n")

    # Mejor resultado
    resultados = []
    if dist_cu is not None:
        resultados.append(("Costo Uniforme", dist_cu))
    if dist_a is not None:
        resultados.append(("A*", dist_a))

    if resultados:
        mejor = min(resultados, key=lambda x: x[1])
        resultado_text.insert(tk.END, f"⭐ Mejor: {mejor[0]} ({mejor[1]} km)\n")


# ---------------- INTERFAZ ----------------
ventana = tk.Tk()
ventana.title("Rutas Colombia IA")
ventana.geometry("600x500")

# Título
titulo = tk.Label(ventana, text="Rutas Colombia IA", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame de selección
frame = tk.Frame(ventana)
frame.pack(pady=10)

ciudades = sorted(grafo.keys())

# Origen
tk.Label(frame, text="Origen:").grid(row=0, column=0, padx=5)
combo_origen = ttk.Combobox(frame, values=ciudades, width=25)
combo_origen.grid(row=0, column=1, padx=5)

# Destino
tk.Label(frame, text="Destino:").grid(row=1, column=0, padx=5)
combo_destino = ttk.Combobox(frame, values=ciudades, width=25)
combo_destino.grid(row=1, column=1, padx=5)

# Botón
btn = tk.Button(ventana, text="Calcular Ruta", command=calcular_rutas)
btn.pack(pady=10)

# Área de resultados
resultado_text = tk.Text(ventana, height=20, width=70)
resultado_text.pack(pady=10)

# Ejecutar
ventana.mainloop()