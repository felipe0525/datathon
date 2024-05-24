import numpy as np
import pandas as pd
import random
import time
import matplotlib.pyplot as plt

# Cargar combinaciones modificadas finales desde el CSV
df_combinaciones_modificadas = pd.read_csv('combinaciones_finales.csv')
combinaciones_modificadas = df_combinaciones_modificadas.values.tolist()

# Definir el arreglo de demanda
demanda = [2, 2, 4, 7, 8, 8, 9, 8, 6, 8, 9, 9, 9, 12, 16, 16, 16, 13, 12, 11, 13, 14, 10, 9, 9, 11, 8, 9, 10, 8, 9, 9,
           5, 5, 4, 6, 8, 4, 5, 1, 3, 2, 2, 2, 2, 2]

# Función de aptitud (fitness) para calcular la minimización
def fitness(combinacion_grupo):
    suma_columnas = np.sum([[1 if val == 2 else 0 for val in fila] for fila in combinacion_grupo], axis=0)
    diferencia = demanda - suma_columnas
    minimizacion = np.sum(diferencia[diferencia > 0])
    return minimizacion

# Función de depuración para imprimir valores intermedios
def depurar_combinacion(combinacion_grupo):
    suma_columnas = np.sum([[1 if val == 2 else 0 for val in fila] for fila in combinacion_grupo], axis=0)
    diferencia = demanda - suma_columnas
    media = np.mean(diferencia)
    print(f"Suma columnas: {suma_columnas}")
    print(f"Diferencia: {diferencia}")
    print(f"Media: {media}")
    minimizacion = np.sum(diferencia[diferencia > 0])
    print(f"Minimización: {minimizacion}")
    return minimizacion

# Comprobar si una combinación cumple con las restricciones
def verificar_restricciones(combinacion_grupo):
    for col in range(len(combinacion_grupo[0])):
        columna = [fila[col] for fila in combinacion_grupo]
        if not any(val == 2 for val in columna) or all(val == 3 for val in columna) or all(val == 0 for val in columna):
            return False
    return True

# Generar población inicial
def generar_poblacion_inicial(combinaciones_modificadas, tamano_poblacion):
    poblacion = []
    while len(poblacion) < tamano_poblacion:
        grupo = random.sample(combinaciones_modificadas, 8)
        if verificar_restricciones(grupo):
            poblacion.append(grupo)
    return poblacion

# Selección por torneo
def seleccion_torneo(poblacion, k=3):
    seleccionados = []
    for _ in range(len(poblacion)):
        k_actual = min(k, len(poblacion))
        aspirantes = random.sample(poblacion, k_actual)
        ganador = min(aspirantes, key=fitness)
        seleccionados.append(ganador)
    return seleccionados

# Cruce de dos combinaciones
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Mutación de una combinación
def mutacion(combinacion, tasa_mutacion=0.1):
    for i in range(len(combinacion)):
        if random.random() < tasa_mutacion:
            combinacion[i] = random.choice(combinaciones_modificadas)
    return combinacion

# Algoritmo genético
def algoritmo_genetico(combinaciones_modificadas, demanda, tamano_poblacion=100, generaciones=1000):
    poblacion = generar_poblacion_inicial(combinaciones_modificadas, tamano_poblacion)
    mejor_combinacion = None
    mejor_fitness = float('inf')

    for _ in range(generaciones):
        poblacion = seleccion_torneo(poblacion)
        nueva_poblacion = []

        for i in range(0, len(poblacion) - 1, 2):
            padre1, padre2 = poblacion[i], poblacion[i + 1]
            hijo1, hijo2 = cruce(padre1, padre2)
            nueva_poblacion.append(mutacion(hijo1))
            nueva_poblacion.append(mutacion(hijo2))

        # Si el tamaño de la población es impar, agregar el último individuo directamente a la nueva población
        if len(poblacion) % 2 == 1:
            nueva_poblacion.append(poblacion[-1])

        poblacion = [individuo for individuo in nueva_poblacion if verificar_restricciones(individuo)]

        for combinacion in poblacion:
            valor_fitness = fitness(combinacion)
            if valor_fitness < mejor_fitness:
                mejor_fitness = valor_fitness
                mejor_combinacion = combinacion

    return mejor_combinacion, mejor_fitness

# Ejecutar el algoritmo genético varias veces para encontrar la mejor combinación posible
def ejecutar_varias_veces(combinaciones_modificadas, demanda, iteraciones=10, tamano_poblacion=100, generaciones=1000):
    mejor_combinacion_global = None
    mejor_fitness_global = float('inf')

    for i in range(iteraciones):
        print(f"Iteración {i + 1} de {iteraciones}")
        mejor_combinacion, mejor_fitness = algoritmo_genetico(combinaciones_modificadas, demanda, tamano_poblacion, generaciones)

        if mejor_fitness < mejor_fitness_global:
            mejor_fitness_global = mejor_fitness
            mejor_combinacion_global = mejor_combinacion

        print(f"Mejor minimización en iteración {i + 1}: {mejor_fitness}")

    return mejor_combinacion_global, mejor_fitness_global

# Ajuste del número de iteraciones
numero_iteraciones = 10

# Temporización del algoritmo genético
start_time = time.time()
mejor_combinacion_global, mejor_fitness_global = ejecutar_varias_veces(combinaciones_modificadas, demanda, iteraciones=numero_iteraciones, tamano_poblacion=100, generaciones=1000)
end_time = time.time()

print("Mejor combinación global encontrada:")
for fila in mejor_combinacion_global:
    print(fila)
print("Mejor minimización global:", mejor_fitness_global)
print(f"Tiempo de ejecución del algoritmo: {end_time - start_time} segundos")

# Depuración de la mejor combinación global
print("\nDepuración de la mejor combinación global:")
depurar_combinacion(mejor_combinacion_global)

# Visualización de la tabla de colores
def mostrar_tabla_colores(mejor_combinacion_global):
    color_map = {0: "white", 2: "green", 3: "blue"}

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('tight')
    ax.axis('off')

    cell_colors = [[color_map[val] for val in row] for row in mejor_combinacion_global]

    table = ax.table(cellText=None, cellColours=cell_colors, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)

    plt.show()

# Mostrar la tabla de colores
mostrar_tabla_colores(mejor_combinacion_global)
