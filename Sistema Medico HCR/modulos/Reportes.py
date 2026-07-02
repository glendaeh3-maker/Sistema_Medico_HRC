def generar_reporte_optimizacion_dp(lista_pacientes, tiempo_maximo_minutos):
    """
    Aplicando la programación dinámica.
    Creamos un reporte que selecciona el grupo de pacientes ideal para atender,
    logrando asi resolver la mayor cantidad de casos graves en el tiempo disponible.
    """
    n = len(lista_pacientes)
    
    # Tabla DP para guardar resultados: filas = pacientes, columnas = tiempo en minutos
    dp = [[0 for _ in range(tiempo_maximo_minutos + 1)] for _ in range(n + 1)]

    # Llenamos la tabla resolviendo los subproblemas pasito a pasito :)
    for i in range(1, n + 1):
        paciente_actual = lista_pacientes[i - 1]
        
        # Tiempo aproximado de atencion
        # Mientras mas critico el paciente, normalmente requiere atencion mas rapida
        tiempo_requerido = paciente_actual.nivel_triaje * 10 

        # En el sistema, triaje 1 es el mas urgente y triaje 5 el menos urgente
        # Por ello aca se invierte el valor para que DP priorice los casos graves
        valor_urgencia = 6 - paciente_actual.nivel_triaje

        for w in range(1, tiempo_maximo_minutos + 1):
            if tiempo_requerido <= w:
                # Aquí el algoritmo decide si conviene más atender a este paciente o simplemente dejarlo pasar
                dp[i][w] = max(valor_urgencia + dp[i - 1][w - tiempo_requerido], dp[i - 1][w])
            else:
                # Si el tiempo no alcanza, simplemente arrastramos el mejor resultado anterior
                dp[i][w] = dp[i - 1][w]


    # Fase de retroceso: revisamos la matriz para identificar a qué pacientes elegimos

    w = tiempo_maximo_minutos
    pacientes_seleccionados = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            pacientes_seleccionados.append(lista_pacientes[i - 1])
            # Descontamos el tiempo que nos tomará atender a este paciente
            w -= (lista_pacientes[i - 1].nivel_triaje * 10) 

    # Devuelve el valor máximo de urgencia cubierta y la lista final para el reporte
    return dp[n][tiempo_maximo_minutos], pacientes_seleccionados