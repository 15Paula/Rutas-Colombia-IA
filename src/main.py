# main.py
from grafo_ciudades import grafo, mostrar_grafo, dijkstra

# Mostrar grafo completo
print("----- Grafo de ciudades cargado -----")
mostrar_grafo()

print("\n----- Consultas de conexión -----")

# Ejemplo de consulta directa
ruta, distancia = dijkstra(grafo, "Bogotá", "Neiva")
if ruta:
    print("Ruta:", " -> ".join(ruta))
    print("Distancia total:", distancia, "km")

# Ejemplos de casos sin conexión
dijkstra(grafo, "San Andrés", "Bogotá")
dijkstra(grafo, "Cali", "Pasto")