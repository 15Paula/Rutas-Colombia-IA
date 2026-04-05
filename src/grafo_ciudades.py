# ================================================================
# GRAFO DE CAPITALES DE COLOMBIA (Estructura de Carreteras)
# ================================================================

grafo = {
    # --- REGIÓN ANDINA ---
    "Bogotá": {"Tunja": 150.99, "Ibagué": 196.75, "Villavicencio": 113.64, "Neiva": 298.31},
    "Tunja": {"Bogotá": 150.99, "Bucaramanga": 284.06, "Yopal": 220.61},
    "Medellín": {"Manizales": 196.73, "Montería": 402.49, "Quibdó": 229.12, "Bucaramanga": 392.0, "Pereira": 210.94, "Sincelejo": 468.65},
    "Manizales": {"Medellín": 196.73, "Pereira": 50.93, "Armenia": 100.39},
    "Pereira": {"Manizales": 50.93, "Armenia": 49.47, "Ibagué": 120.84, "Quibdó": 253.17, "Medellín": 210.94},
    "Armenia": {"Pereira": 49.47, "Manizales": 100.39, "Ibagué": 82.18, "Cali": 175.21},
    "Ibagué": {"Bogotá": 196.75, "Armenia": 82.18, "Pereira": 120.84, "Neiva": 211.03, "Cali": 258.80},
    "Neiva": {"Bogotá": 298.31, "Ibagué": 211.03, "Florencia": 243.25, "Mocoa": 325.29, "Pasto": 479.40, "Popayán": 283.79},
    "Bucaramanga": {"Tunja": 284.06, "Cúcuta": 197.29, "Medellín": 392.0, "Valledupar": 444.11, "Santa Marta": 530.85, "Yopal": 433.79, "Arauca": 520.60, "Sincelejo": 598.78},
    "Cúcuta": {"Bucaramanga": 197.29, "Valledupar": 579.28, "Arauca": 470.23, "Yopal": 525.19},

    # --- REGIÓN CARIBE ---
    "Barranquilla": {"Cartagena": 128.49, "Santa Marta": 98.0, "Valledupar": 361.6, "Montería": 348.61},
    "Cartagena": {"Barranquilla": 128.49, "Sincelejo": 185.28, "Montería": 272.17},
    "Santa Marta": {"Barranquilla": 98.0, "Riohacha": 168.12, "Bucaramanga": 530.85, "Valledupar": 317.38},
    "Riohacha": {"Santa Marta": 168.12, "Valledupar": 158.90},
    "Valledupar": {"Riohacha": 158.90, "Barranquilla": 361.6, "Bucaramanga": 444.11, "Santa Marta": 317.38, "Cúcuta": 579.28},
    "Sincelejo": {"Cartagena": 185.28, "Montería": 122.12, "Medellín": 468.65, "Bucaramanga": 598.78},
    "Montería": {"Sincelejo": 122.12, "Medellín": 402.49, "Barranquilla": 348.61, "Cartagena": 272.17},

    # --- REGIÓN PACÍFICA ---
    "Cali": {"Armenia": 175.21, "Popayán": 142.23, "Quibdó": 418.12, "Ibagué": 250.98},
    "Popayán": {"Cali": 142.23, "Pasto": 245.47, "Mocoa": 279.14, "Neiva": 283.79},
    "Pasto": {"Popayán": 245.47, "Mocoa": 154.11, "Neiva": 479.40},
    "Quibdó": {"Medellín": 229.12, "Pereira": 253.17, "Cali": 418.12},

    # --- REGIÓN ORINOQUÍA ---
    "Villavicencio": {"Bogotá": 113.64, "Yopal": 260.72, "San José del Guaviare": 281.68, "Arauca": 660.2, "Puerto Carreño": 849.0},
    "Yopal": {"Tunja": 220.61, "Villavicencio": 260.72, "Arauca": 399.48, "Bucaramanga": 433.79, "Cúcuta": 525.19},
    "Arauca": {"Yopal": 399.48, "Bucaramanga": 520.60, "Villavicencio": 660.2, "Cúcuta": 470.23},
    "Puerto Carreño": {"Villavicencio": 849.0},

    # --- REGIÓN AMAZONÍA ---
    "Florencia": {"Neiva": 243.25, "Mocoa": 191.54},
    "Mocoa": {"Pasto": 154.11, "Popayán": 279.14, "Florencia": 191.54, "Neiva": 325.29},
    "San José del Guaviare": {"Villavicencio": 281.68},

    # --- AISLADAS (Sin carretera directa) ---
    "Mitú": {}, "Inírida": {}, "Leticia": {}, "San Andrés": {}
}

# ================================================================
# COORDENADAS (Ubicación visual y lógica)
# ================================================================
coordenadas = {
    "Bogotá": (260, 260), "Tunja": (296, 227), "Bucaramanga": (303, 179),
    "Cúcuta": (330, 149), "Valledupar": (296, 80), "Riohacha": (330, 34),
    "Santa Marta": (259, 50), "Barranquilla": (218, 65), "Cartagena": (201, 81),
    "San Andrés": (43, 55), "Sincelejo": (213, 111), "Montería": (192, 128),
    "Medellín": (205, 201), "Arauca": (402, 186), "Yopal": (343, 240),
    "Puerto Carreño": (536, 221), "Inírida": (526, 288), "Villavicencio": (286, 282),
    "Mitú": (416, 365), "Leticia": (446, 478), "Florencia": (237, 377),
    "San José del Guaviare": (329, 335), "Mocoa": (160, 382), "Pasto": (113, 367),
    "Popayán": (155, 332), "Neiva": (211, 317), "Ibagué": (222, 267),
    "Cali": (162, 300), "Quibdó": (144, 239), "Manizales": (194, 251),
    "Pereira": (193, 267), "Armenia": (191, 279)
}

# ================================================================
# HEURÍSTICAS (Ejemplo base para Santa Marta)
# ================================================================
heuristicas = {
    "Bogotá": 708, "Tunja": 612, "Bucaramanga": 448, "Cúcuta": 418,
    "Medellín": 535, "Montería": 285, "Barranquilla": 72, "Santa Marta": 0,
    "Riohacha": 135, "Cartagena": 164, "Sincelejo": 286, "Manizales": 612,
    "Pereira": 643, "Armenia": 668, "Ibagué": 701, "Neiva": 880,
    "Florencia": 1052, "Mocoa": 1150, "Pasto": 1238, "Popayán": 1095,
    "Cali": 967, "Quibdó": 745, "Villavicencio": 782, "Yopal": 680,
    "Arauca": 598, "Puerto Carreño": 860, "Inírida": 980, "Mitú": 1150,
    "Leticia": 1850, "San José del Guaviare": 950, "San Andrés": 780
}

# ================================================================
# FUNCIONES DE CONSULTA Y CONTROL
# ================================================================

def revisar_conexiones():
    """Imprime el estado de las rutas críticas definidas por el usuario."""
    print("--- Auditoría de Rutas Críticas ---")
    rutas_a_revisar = [
        ("Cúcuta", "Valledupar"),
        ("Medellín", "Sincelejo"),
        ("Cali", "Ibagué"),
        ("Sincelejo", "Bucaramanga"),
        ("Arauca", "Cúcuta")
    ]
    
    for c1, c2 in rutas_a_revisar:
        dist = grafo.get(c1, {}).get(c2)
        if dist is None:
            estado = "❌ No existe conexión"
        elif dist == 0.0:
            estado = "⚠️ Pendiente (0.0)"
        else:
            estado = f"✅ Definida ({dist} km)"
        print(f"Ruta {c1} -> {c2}: {estado}")

def consultar_distancia(c1, c2):
    """Consulta la distancia directa entre dos ciudades manejando errores."""
    if c1 not in grafo or c2 not in grafo:
        return "❌ Una de las ciudades no existe en el grafo"

    distancia = grafo[c1].get(c2)

    if distancia is None:
        return f"⚠️ No hay carretera directa entre {c1} y {c2}"
    elif distancia == 0.0:
        return f"⚠️ La carretera entre {c1} y {c2} existe pero su distancia no ha sido definida (0.0 km)"
    else:
        return f"✅ Distancia directa entre {c1} y {c2}: {distancia} km"

# ================================================================
# BLOQUE PRINCIPAL
# ================================================================
if __name__ == "__main__":
    revisar_conexiones()
    print("\n--- Pruebas de Consulta ---")
    print(consultar_distancia("Bogotá", "Tunja"))
    print(consultar_distancia("Bogotá", "Leticia"))
    print(consultar_distancia("Cúcuta", "Valledupar"))