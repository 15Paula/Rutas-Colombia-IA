# probar_rutas.py
from grafo_ciudades import grafo, mostrar_grafo, consultar_distancia

print("----- Grafo de ciudades cargado -----")
mostrar_grafo()

print("\n----- Consultas de conexión -----")
print(consultar_distancia("Bogotá", "Neiva"))
print(consultar_distancia("San Andrés", "Bogotá"))
print(consultar_distancia("Cali", "Pasto"))