def asignar_triaje_voraz(lista_pacientes, camas_disponibles):
    """
    Aplica un Algoritmo Voraz (Greedy) para gestionar la cola de triaje.
    La regla de oro aquí es: siempre elegir al paciente más grave en ese 
    instante y asignarle un recurso inmediatamente, sin mirar el panorama futuro.
    """
    # El primer paso voraz: ordenar a todos por su nivel de gravedad de mayor a menor.
    # Así nos aseguramos de que los más críticos queden primeritos en la fila.
    pacientes_priorizados = sorted(lista_pacientes, key=lambda p: p.nivel_triaje)
    
    atendidos = []
    en_espera = []
    camas_libres = camas_disponibles
    
    # Recorremos la fila de pacientes ya ordenados por gravedad
    for paciente in pacientes_priorizados:
        if camas_libres > 0:
            # Si hay una cama libre, el algoritmo voraz no la piensa dos veces: 
            # mete al paciente más grave de inmediato.
            atendidos.append(paciente)
            camas_libres -= 1
        else:
            # Si el hospital ya colapsó (0 camas), los demás se van a la sala de espera,
            # sin importar si su caso se complica después (típica desventaja del voraz).
            en_espera.append(paciente)
            
    # Devolvemos quiénes consiguieron cama y quiénes se quedaron esperando
    return atendidos, en_espera

"""
mini prueba para los triajes


if __name__ == "__main__":
    # 1. Clase falsa de Paciente para simular la prueba
    class PacienteMock:
        def __init__(self, nombre, nivel_triaje):
            self.nombre = nombre
            self.nivel_triaje = nivel_triaje # Del 1 (Leve) al 5 (Crítico)
            
        def __repr__(self):
            return f"[{self.nombre} | Gravedad: {self.nivel_triaje}]"

    # 2. Llegaron 5 pacientes al mismo tiempo a la emergencia
    pacientes_emergencia = [
        PacienteMock("Luis Fernando", 2),
        PacienteMock("Carmen Rosa", 5),   # ¡Muy grave!
        PacienteMock("Jorge Luis", 1),
        PacienteMock("Teresa Silva", 4),  # Urgente
        PacienteMock("Miguel Angel", 4)   # Urgente
    ]

    # 3. Digamos que solo nos quedan 2 camas disponibles en todo el hospital
    camas_totales = 2 

    print("--- INICIANDO PRUEBA DE TRIAJE (ALGORITMO VORAZ) ---")
    print(f" Camas disponibles: {camas_totales}")
    print(f" Pacientes recién llegados: {pacientes_emergencia}\n")

    # 4. Llamamos a la función voraz
    los_atendidos, los_que_esperan = asignar_triaje_voraz(pacientes_emergencia, camas_totales)

    # 5. Mostramos el resultado del triaje
    print(" RESULTADO DEL TRIAJE VORAZ:")
    print(" PACIENTES INGRESADOS (Atención inmediata):")
    for p in los_atendidos:
        print(f"   -> {p.nombre} (Gravedad {p.nivel_triaje})")
        
    print("\n PACIENTES EN SALA DE ESPERA (No alcanzaron cama):")
    for p in los_que_esperan:
        print(f"   -> {p.nombre} (Gravedad {p.nivel_triaje})")

"""