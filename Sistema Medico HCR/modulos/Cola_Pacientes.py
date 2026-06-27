def ordenar_por_triaje(lista_pacientes):
    """
    Ordena pacientes de mayor a menor urgencia usando el método sorted().
    Triaje 1 = más urgente, 5 = menos urgente.
    Usamos el __lt__ ya definido en la clase Paciente.
    """
    return sorted(lista_pacientes)  # usa el __lt__ de Paciente (nivel_triaje)


def ordenar_burbuja(lista_pacientes):
    # Implementación manual de Bubble Sort por triaje (fuerza bruta).
    
    n = len(lista_pacientes)
    lista = lista_pacientes.copy()  # no modificamos la original

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].nivel_triaje > lista[j + 1].nivel_triaje:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def agregar_paciente(cola, paciente):
    
    #Agrega un paciente a la cola y la reordena por triaje.
    
    cola.append(paciente)
    return ordenar_por_triaje(cola)


def siguiente_paciente(cola):

    #Retorna el paciente más urgente (el primero de la cola ordenada)
    if not cola:
        print("La cola está vacía.")
        return None
    return cola[0]


def mostrar_cola(cola):
    #Muestra todos los pacientes en orden de atención.
    if not cola:
        print("No hay pacientes en cola.")
        return
    print("\n=== Cola de Atención (ordenada por triaje) ===")
    for i, p in enumerate(cola, 1):
        print(f"{i}. {p}")