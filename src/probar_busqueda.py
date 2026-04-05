from busqueda import costo_uniforme, profundidad, voraz, a_estrella
from grafo_ciudades import grafo

# ---------------- Mostrar ciudades ----------------
ciudades_disponibles = sorted(grafo.keys())
print("Ciudades disponibles:")
for c in ciudades_disponibles:
    print("-", c)

# ---------------- Entrada usuario ----------------
origen = input("Ingresa la ciudad de origen: ").strip()
while origen not in grafo:
    print("Ciudad no válida, intenta nuevamente.")
    origen = input("Ingresa la ciudad de origen: ").strip()

destino = input("Ingresa la ciudad de destino: ").strip()
while destino not in grafo:
    print("Ciudad no válida, intenta nuevamente.")
    destino = input("Ingresa la ciudad de destino: ").strip()

print(f"\n==== Ruta: {origen} -> {destino} ====")

# ---------------- Costo Uniforme ----------------
ruta_cu, distancia_cu = costo_uniforme(origen, destino)
print("\n----- Costo Uniforme -----")
if ruta_cu:
    print("Ruta:", " -> ".join(ruta_cu))
    print("Distancia total:", distancia_cu, "km")
else:
    print("No hay ruta")

# ---------------- Profundidad ----------------
ruta_prof = profundidad(origen, destino)
print("\n----- Profundidad -----")
if ruta_prof:
    print("Ruta:", " -> ".join(ruta_prof))
else:
    print("No hay ruta")

# ---------------- Voraz ----------------
ruta_voraz = voraz(origen, destino)
print("\n----- Voraz -----")
if ruta_voraz:
    print("Ruta:", " -> ".join(ruta_voraz))
else:
    print("No hay ruta")

# ---------------- A* ----------------
ruta_a, distancia_a = a_estrella(origen, destino)
print("\n----- A* -----")
if ruta_a:
    print("Ruta:", " -> ".join(ruta_a))
    print("Distancia total:", distancia_a, "km")
else:
    print("No hay ruta")

# ---------------- Comparación ----------------
print("\n===== MEJOR RESULTADO =====")
resultados = []

if distancia_cu is not None:
    resultados.append(("Costo Uniforme", distancia_cu))

if distancia_a is not None:
    resultados.append(("A*", distancia_a))

if resultados:
    mejor = min(resultados, key=lambda x: x[1])
    print("Mejor algoritmo:", mejor[0])
    print("Distancia:", mejor[1], "km")
else:
    print("No hay rutas válidas")