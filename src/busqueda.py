# busqueda.py
from grafo_ciudades import grafo, coordenadas
import heapq
import math

# --------- COSTO UNIFORME (Dijkstra) ---------
def costo_uniforme(origen, destino):
    visitados = set()
    heap = [(0, origen, [origen])]  # (costo_acumulado, ciudad_actual, camino)
    
    while heap:
        costo, actual, camino = heapq.heappop(heap)
        if actual == destino:
            return camino, costo
        if actual in visitados:
            continue
        visitados.add(actual)
        for vecino, distancia in grafo.get(actual, {}).items():
            if distancia is not None and vecino not in visitados:
                heapq.heappush(heap, (costo + distancia, vecino, camino + [vecino]))
    return None, float('inf')


# --------- DFS LIMITADO POR PROFUNDIDAD PARA EVITAR DESVÍOS LARGOS ---------
def profundidad(origen, destino, limite=10):
    mejor_ruta = None
    mejor_distancia = float('inf')
    
    def dfs(actual, camino, distancia_acum, visitados):
        nonlocal mejor_ruta, mejor_distancia
        if len(camino) > limite:  # evita rutas muy largas
            return
        if actual == destino:
            if distancia_acum < mejor_distancia:
                mejor_ruta = camino[:]
                mejor_distancia = distancia_acum
            return
        for vecino, distancia in grafo.get(actual, {}).items():
            if distancia is not None and vecino not in visitados:
                visitados.add(vecino)
                dfs(vecino, camino + [vecino], distancia_acum + distancia, visitados)
                visitados.remove(vecino)
    
    dfs(origen, [origen], 0, set([origen]))
    return mejor_ruta, mejor_distancia


# --------- HEURÍSTICA MEJORADA ---------
def heuristica(ciudad1, ciudad2):
    x1, y1 = coordenadas[ciudad1]
    x2, y2 = coordenadas[ciudad2]
    # Escalar euclidiana para que se asemeje a kilómetros reales
    escala = 2.5
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) * escala


# --------- A ESTRELLA (A*) ---------
def a_estrella(origen, destino):
    visitados = set()
    heap = [(0, 0, origen, [origen])]  # (f=g+h, g, ciudad_actual, camino)
    
    while heap:
        f, g, actual, camino = heapq.heappop(heap)
        if actual == destino:
            return camino, g
        if actual in visitados:
            continue
        visitados.add(actual)
        for vecino, distancia in grafo.get(actual, {}).items():
            if distancia is not None and vecino not in visitados:
                h = heuristica(vecino, destino)
                heapq.heappush(heap, (g + distancia + h, g + distancia, vecino, camino + [vecino]))
    return None, float('inf')


# --------- MEJOR RUTA ENTRE MÉTODOS ---------
def mejor_ruta(origen, destino):
    rutas = {}
    
    ruta_cu, dist_cu = costo_uniforme(origen, destino)
    rutas["Costo Uniforme"] = (ruta_cu, dist_cu)
    
    ruta_p, dist_p = profundidad(origen, destino)
    rutas["Profundidad"] = (ruta_p, dist_p)
    
    ruta_a, dist_a = a_estrella(origen, destino)
    rutas["A*"] = (ruta_a, dist_a)
    
    # Elegir la ruta de menor distancia válida
    mejor_algo = min(rutas, key=lambda k: rutas[k][1] if rutas[k][0] else float('inf'))
    mejor_ruta_val, mejor_distancia = rutas[mejor_algo]
    
    return {
        "rutas": rutas,
        "mejor": (mejor_algo, mejor_ruta_val, mejor_distancia)
    }


# --------- PRUEBA RÁPIDA ---------
if __name__ == "__main__":
    origen = "Bogotá"
    destino = "Popayán"
    resultado = mejor_ruta(origen, destino)
    
    print("----- Resultados -----")
    for metodo, (ruta, distancia) in resultado["rutas"].items():
        print(f"{metodo}:")
        if ruta:
            print(f"  Ruta: {' -> '.join(ruta)}")
            print(f"  Distancia: {round(distancia,2)} km")
        else:
            print("  No hay ruta disponible")
    
    print("\nMejor resultado:")
    metodo, ruta, distancia = resultado["mejor"]
    print(f"Metodo: {metodo}")
    print(f"Ruta: {' -> '.join(ruta)}")
    print(f"Distancia: {round(distancia,2)} km")