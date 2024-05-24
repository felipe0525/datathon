## Proyecto de Dataton 2023

Este proyecto está basado en el Dataton 2023 disponible en [Kaggle](https://www.kaggle.com/datasets/cvelas24/dataton-2023). El objetivo de esta primera etapa es generar combinaciones y realizar un análisis genético para minimizar la diferencia entre una demanda y una combinación modificada. El archivo `main.py` orquesta la ejecución de los scripts `combinaciones.py` y `convergencia.py` y se asegura de que todas las dependencias necesarias estén instaladas.



## Requisitos

- Python 3.6 o superior
- Entorno virtual (`virtualenv`) recomendado

## Instrucciones de Ejecución

1. **Clonar el Repositorio**

   Clona este repositorio en tu máquina local.

2. **Crear y Activar el Entorno Virtual**

   En la raíz del proyecto, crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   source .venv/bin/activate  # En macOS/Linux
   python main.py
   
## Descripción de la Primera Etapa del Dataton 2023

### Objetivo

La primera etapa del Dataton 2023 se centra en generar y modificar combinaciones para minimizar la diferencia entre una demanda predefinida y las combinaciones resultantes utilizando un algoritmo genético.

### Datos

Los datos utilizados en este proyecto provienen del conjunto de datos del Dataton 2023 disponible en Kaggle.

### Metodología

#### Generación de Combinaciones:

- Generación recursiva de combinaciones iniciales.
- Modificación de combinaciones mediante varias reglas.

#### Algoritmo Genético:

- Carga de combinaciones modificadas desde un archivo CSV.
- Definición de una función de aptitud para evaluar las combinaciones.
- Implementación de un algoritmo genético que incluye generación de población inicial, selección por torneo, cruce y mutación de combinaciones.
- Optimización para encontrar la mejor combinación que minimice la diferencia con la demanda.

  ## Nota
- Para incremtenar la posibildad de un mejor resultado, incremente el numero de iteraciones en `convergencia.py`
