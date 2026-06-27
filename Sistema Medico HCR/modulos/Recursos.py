def area_mas_colapsada(lista_recursos):
    # Punto de entrada: arranca la recursividad con la lista completa
    print(f"Iniciando busqueda del area mas colapsada entre {len(lista_recursos)} areas...")
    return _buscar_extremo(lista_recursos, mayor=True)
 
 
def area_menos_colapsada(lista_recursos):
    # Mismo algoritmo pero buscando el menor porcentaje de ocupacion
    print(f"Iniciando busqueda del area menos colapsada entre {len(lista_recursos)} areas...")
    return _buscar_extremo(lista_recursos, mayor=False)
 
 
def _buscar_extremo(lista_recursos, mayor=True):
    # CASO BASE: si solo queda 1 area, esa misma es el resultado (no hay nada que dividir)
    if len(lista_recursos) == 1:
        print(f"  Caso base -> {lista_recursos[0].area} ({lista_recursos[0].porcentaje_ocupacion()}%)")
        return lista_recursos[0]
 
    # 1. DIVIDE: cortamos la lista a la mitad
    mitad = len(lista_recursos) // 2
    izquierda = lista_recursos[:mitad]
    derecha = lista_recursos[mitad:]
    print(f"  Dividiendo en {[r.area for r in izquierda]} y {[r.area for r in derecha]}")
 
    # 2. VENCERAS: resolvemos cada mitad por recursividad
    ganador_izquierda = _buscar_extremo(izquierda, mayor)
    ganador_derecha = _buscar_extremo(derecha, mayor)
 
    # 3. COMBINA: comparamos los dos ganadores y nos quedamos con el mejor
    if mayor:
        resultado = ganador_izquierda if ganador_izquierda.porcentaje_ocupacion() >= ganador_derecha.porcentaje_ocupacion() else ganador_derecha
    else:
        resultado = ganador_izquierda if ganador_izquierda.porcentaje_ocupacion() <= ganador_derecha.porcentaje_ocupacion() else ganador_derecha
 
    print(f"  Combinando -> entre {ganador_izquierda.area} y {ganador_derecha.area} gana {resultado.area}")
    return resultado
 
 
def total_camas_disponibles(lista_recursos):
    """
    Suma el total de camas disponibles en todas las areas usando Divide y Venceras
    en vez de un simple for (para mantener la misma estrategia recursiva).
    """
    # CASO BASE: si solo queda 1 area, retornamos sus camas disponibles directo
    if len(lista_recursos) == 1:
        return lista_recursos[0].camas_disponibles()
 
    # 1. DIVIDE
    mitad = len(lista_recursos) // 2
    izquierda = lista_recursos[:mitad]
    derecha = lista_recursos[mitad:]
 
    # 2. VENCERAS: sumamos recursivamente cada mitad
    suma_izquierda = total_camas_disponibles(izquierda)
    suma_derecha = total_camas_disponibles(derecha)
 
    # 3. COMBINA: la suma total es la union de ambas mitades
    return suma_izquierda + suma_derecha
 
 
def mostrar_resumen_recursos(lista_recursos):
    # Solo para ver bonito el estado de todas las areas en consola
    print("\n=== Estado de Areas del Hospital ===")
    for recurso in lista_recursos:
        print(f"  {recurso}")