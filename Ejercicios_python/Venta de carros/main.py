import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scripts import entrenamiento, evaluacion, prediccion, preprocesamiento
import os

DATA_DIR = 'data'
RAW_DATA_PATH = os.path.join(DATA_DIR,'datos_venta_ampliado.csv')
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'datos_procesados.csv')
MODEL_DIR = 'models'
MODEL_PATH = os.path.join(MODEL_DIR, 'modelo_regreción.pkl')
VISUALIZATIONS_DIR= 'visualizations'

print("Cargando datos...")
df = pd.read_csv(RAW_DATA_PATH)
print(f"Datos cargados: {df.shape[0]} filas y {df.shape[1]} columnas.")
# Preprocesamiento
print("Preprocesando datos...")
df_preprocesado = preprocesamiento.procesar_datos(df)
df_preprocesado.to_csv(PROCESSED_DATA_PATH, index=False)
print(f"Datos preprocesados guardados en {PROCESSED_DATA_PATH}")

# Entrenamiento del modelo
print("Entrenando modelo...")
modelo = entrenamiento.entrenar_modelo(df_preprocesado)
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
entrenamiento.guardar_modelo(modelo, MODEL_PATH)
print(f"Modelo guardado en {MODEL_PATH}")

# Evaluación del modelo
print("Evaluando modelo...")
df_resultados = evaluacion.evaluar_modelo(modelo, df_preprocesado)
evaluacion.graficar_resultados(df_resultados, VISUALIZATIONS_DIR)

# Realizar predicciones
print("Realizando predicciones...")
nuevos_datos = {
    # Agregar datos nuevos para predecir
    'Marca': ['Toyota', 'Honda'],
    'Modelo': ['Corolla', 'Civic'],
    'Año': [2018, 2019],
    'kilometraje': [50000, 30000],
    # Agregar más características según corresponda
}
df_nuevos_datos = pd.DataFrame(nuevos_datos)
df_nuevos_datos = preprocesamiento.procesar_datos(df_nuevos_datos, es_nuevo=True)
predicciones = prediccion.realizar_predicciones(modelo, df_nuevos_datos)
print("Predicciones realizadas:")
print(predicciones)

print("Proceso completado.")