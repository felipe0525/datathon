import time
import pandas as pd

def generar_combinaciones(estado_inicial):
    combinaciones = []

    def generar_recursivamente(estado_actual, combinacion_actual):
        if len(combinacion_actual) == 4:
            combinaciones.append(combinacion_actual)
            return

        if estado_actual == 4:
            generar_recursivamente(4, combinacion_actual + [4])
        elif estado_actual == 5:
            for estado_siguiente in range(4, 6):
                generar_recursivamente(estado_siguiente, combinacion_actual + [estado_siguiente])
        elif estado_actual == 6:
            for estado_siguiente in range(4, 7):
                generar_recursivamente(estado_siguiente, combinacion_actual + [estado_siguiente])
        elif estado_actual == 7:
            for estado_siguiente in range(4, 8):
                generar_recursivamente(estado_siguiente, combinacion_actual + [estado_siguiente])
        elif estado_actual == 8:
            for estado_siguiente in range(4, 9):
                generar_recursivamente(estado_siguiente, combinacion_actual + [estado_siguiente])

    generar_recursivamente(estado_inicial, [estado_inicial])
    return combinaciones

def agregar_uno_a_combinaciones(combinaciones):
    combinaciones_modificadas = []
    for combinacion in combinaciones:
        combinacion_modificada = combinacion + [1]
        combinaciones_modificadas.append(combinacion_modificada)
    return combinaciones_modificadas

def extender_con_combinaciones_anteriores(combinaciones_con_uno, todas_combinaciones):
    combinaciones_extendidas = []
    for combinacion in combinaciones_con_uno:
        for combinacion_anterior in todas_combinaciones:
            combinacion_extendida = combinacion + combinacion_anterior[:-1]
            combinaciones_extendidas.append(combinacion_extendida)
    return combinaciones_extendidas

def reemplazar_numeros(combinacion):
    mapeo = {
        4: [2, 2, 2, 2, 3],
        5: [2, 2, 2, 3, 2],
        6: [2, 2, 3, 2, 2],
        7: [2, 3, 2, 2, 2],
        8: [3, 2, 2, 2, 2]
    }
    nueva_combinacion = []
    for numero in combinacion:
        if numero in mapeo:
            nueva_combinacion.extend(mapeo[numero])
        else:
            nueva_combinacion.append(numero)
    return nueva_combinacion

def recortar_combinacion(combinacion, posicion):
    index_uno = combinacion.index(1)
    start = max(0, index_uno - posicion + 1)
    end = start + 25
    return combinacion[start:end]

def ajustar_ultimo_numero(combinaciones_ajustadas):
    combinaciones_modificadas = []
    for combinacion in combinaciones_ajustadas:
        nueva_combinacion = [2] + combinacion[1:-1] + [2]  # Reemplazar el primer y el último número por 2
        combinaciones_modificadas.append(nueva_combinacion)
    return combinaciones_modificadas

def garantizar_dos_en_extremos(combinaciones):
    combinaciones_modificadas = []
    for combinacion in combinaciones:
        nueva_combinacion = [2, 2, 2, 2] + combinacion[4:-4] + [2, 2, 2, 2]
        combinaciones_modificadas.append(nueva_combinacion)
    return combinaciones_modificadas

def eliminar_filas_nueve_dos_seguidos(combinaciones):
    combinaciones_filtradas = []
    for combinacion in combinaciones:
        cadena = ''.join(map(str, combinacion))
        if '222222222' not in cadena:
            combinaciones_filtradas.append(combinacion)
    return combinaciones_filtradas

def agregar_ceros(paquete, patrones):
    nuevas_combinaciones = []
    for combinacion in paquete:
        for patron in patrones:
            ceros_izquierda, ceros_derecha = patron
            nueva_combinacion = [0] * ceros_izquierda + combinacion + [0] * ceros_derecha
            nuevas_combinaciones.append(nueva_combinacion)
    return nuevas_combinaciones

def reemplazar_uno_por_secuencia(combinaciones):
    secuencia = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2]
    combinaciones_modificadas = []
    for combinacion in combinaciones:
        nueva_combinacion = []
        for numero in combinacion:
            if numero == 1:
                nueva_combinacion.extend(secuencia)
            else:
                nueva_combinacion.append(numero)
        combinaciones_modificadas.append(nueva_combinacion)
    return combinaciones_modificadas

def eliminar_filas_con_muchos_dos_seguidos(combinaciones, max_dos_seguidos):
    combinaciones_filtradas = []
    for combinacion in combinaciones:
        cadena = ''.join(map(str, combinacion))
        if '2' * (max_dos_seguidos + 1) not in cadena:
            combinaciones_filtradas.append(combinacion)
    return combinaciones_filtradas

def main():
    todas_combinaciones = []

    # Generar, modificar y unir todas las combinaciones para cada estado inicial del 4 al 8
    for estado in range(4, 9):
        combinaciones = generar_combinaciones(estado)
        combinaciones_modificadas = agregar_uno_a_combinaciones(combinaciones)
        todas_combinaciones.extend(combinaciones_modificadas)
    print(f"Total de combinaciones después de agregar uno: {len(todas_combinaciones)}")

    # Extender combinaciones modificadas con todas las combinaciones previas
    combinaciones_extendidas = extender_con_combinaciones_anteriores(todas_combinaciones, todas_combinaciones)
    print(f"Total de combinaciones después de extender: {len(combinaciones_extendidas)}")

    # Reemplazar números en combinaciones extendidas
    combinaciones_finales = [reemplazar_numeros(combinacion) for combinacion in combinaciones_extendidas]
    print(f"Total de combinaciones después de reemplazar números: {len(combinaciones_finales)}")

    # Generar todas las combinaciones recortadas con el '1' en las posiciones del 6 al 20
    combinaciones_recortadas = []
    for posicion in range(6, 21):
        for combinacion in combinaciones_finales:
            combinaciones_recortadas.append(recortar_combinacion(combinacion, posicion))
    print(f"Total de combinaciones después de recortar: {len(combinaciones_recortadas)}")

    # Ajustar el primer y el último número de cada combinación
    combinaciones_ajustadas = ajustar_ultimo_numero(combinaciones_recortadas)
    print(f"Total de combinaciones después de ajustar el primer y el último número: {len(combinaciones_ajustadas)}")

    # Garantizar que los primeros y últimos cuatro números sean dos
    combinaciones_garantizadas = garantizar_dos_en_extremos(combinaciones_ajustadas)
    print(f"Total de combinaciones después de garantizar dos en extremos: {len(combinaciones_garantizadas)}")

    # Eliminar filas con nueve 2 seguidos
    combinaciones_filtradas = eliminar_filas_nueve_dos_seguidos(combinaciones_garantizadas)
    print(f"Total de combinaciones después de eliminar filas con nueve 2 seguidos: {len(combinaciones_filtradas)}")

    # Paquetes basados en la posición del 1
    paquetes_combinaciones = [combinaciones_filtradas[i:i + 4900] for i in range(0, len(combinaciones_filtradas), 4900)]

    patrones_tabla = [
        [(8, 0)],  # Paquete 1
        [(8, 0), (7, 1)],  # Paquete 2
        [(8, 0), (7, 1), (6, 2)],  # Paquete 3
        [(8, 0), (7, 1), (6, 2), (5, 3)],  # Paquete 4
        [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4)],  # Paquete 5
        [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5)],  # Paquete 6
        [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6)],  # Paquete 7
        [        (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7)],  # Paquete 8
        [                (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)],  # Paquete 9
        [                        (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)],  # Paquete 10
        [                                (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)],  # Paquete 11
        [                                        (3, 5), (2, 6), (1, 7), (0, 8)],  # Paquete 12
        [                                                (2, 6), (1, 7), (0, 8)],  # Paquete 13
        [                                                        (1, 7), (0, 8)],  # Paquete 14
        [                                                                (0, 8)]  # Paquete 15
    ]

    paquetes_modificados = []
    for i, paquete in enumerate(paquetes_combinaciones):
        patrones = patrones_tabla[i] if i < len(patrones_tabla) else [(8, 0)]
        paquete_modificado = agregar_ceros(paquete, patrones)
        paquetes_modificados.extend(paquete_modificado)
    print(f"Total de combinaciones después de agregar ceros: {len(paquetes_modificados)}")

    # Reemplazar 1 por la secuencia
    combinaciones_secuencia = reemplazar_uno_por_secuencia(paquetes_modificados)
    print(f"Total de combinaciones después de reemplazar 1 por secuencia: {len(combinaciones_secuencia)}")

    # Eliminar filas con diez o más 2 seguidos
    combinaciones_sin_muchos_dos_seguidos = eliminar_filas_con_muchos_dos_seguidos(combinaciones_secuencia, 8)
    print(f"Total de combinaciones después de eliminar filas con nueve o más 2 seguidos: {len(combinaciones_sin_muchos_dos_seguidos)}")

    # Eliminar filas repetidas
    df_combinaciones = pd.DataFrame(combinaciones_sin_muchos_dos_seguidos).drop_duplicates()
    print(f"Total de combinaciones después de eliminar filas repetidas: {len(df_combinaciones)}")

    # Guardar en un archivo CSV
    df_combinaciones.to_csv('combinaciones_finales.csv', index=False)

    # Imprimir el número de filas (combinaciones recortadas únicas)
    print(f"Total de combinaciones finales guardadas: {len(df_combinaciones)}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Tiempo de ejecución del algoritmo: {end_time - start_time} segundos")
