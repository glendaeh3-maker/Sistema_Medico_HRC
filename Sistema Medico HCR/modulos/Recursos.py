def area_mas_colapsada(lista_recursos):
    """
    Devuelve el área con mayor porcentaje de ocupación.
    """
    return _buscar_extremo(lista_recursos, mayor=True)


def area_menos_colapsada(lista_recursos):
    """
    Devuelve el área con menor porcentaje de ocupación.
    """
    return _buscar_extremo(lista_recursos, mayor=False)


def _buscar_extremo(lista_recursos, mayor=True):
    """
    Algoritmo Divide y Vencerás para encontrar el área con
    mayor o menor porcentaje de ocupación.
    """

    # Caso base
    if len(lista_recursos) == 1:
        return lista_recursos[0]

    # 1. Divide
    mitad = len(lista_recursos) // 2
    izquierda = lista_recursos[:mitad]
    derecha = lista_recursos[mitad:]

    # 2. Vencerás
    ganador_izquierda = _buscar_extremo(izquierda, mayor)
    ganador_derecha = _buscar_extremo(derecha, mayor)

    # 3. Combina
    if mayor:
        return (
            ganador_izquierda
            if ganador_izquierda.porcentaje_ocupacion() >= ganador_derecha.porcentaje_ocupacion()
            else ganador_derecha
        )
    else:
        return (
            ganador_izquierda
            if ganador_izquierda.porcentaje_ocupacion() <= ganador_derecha.porcentaje_ocupacion()
            else ganador_derecha
        )


def total_camas_disponibles(lista_recursos):
    """
    Calcula el total de camas disponibles usando Divide y Vencerás.
    """

    # Caso base
    if len(lista_recursos) == 1:
        return lista_recursos[0].camas_disponibles()

    # Divide
    mitad = len(lista_recursos) // 2

    # Vencerás
    suma_izquierda = total_camas_disponibles(lista_recursos[:mitad])
    suma_derecha = total_camas_disponibles(lista_recursos[mitad:])

    # Combina
    return suma_izquierda + suma_derecha


def obtener_resumen_recursos(lista_recursos):
    """
    Devuelve un resumen del estado de todas las áreas.
    """
    return "\n".join(str(recurso) for recurso in lista_recursos)