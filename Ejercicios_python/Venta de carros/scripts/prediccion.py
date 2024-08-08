import pandas as pd

def realizar_predicciones(modelo, df_nuevos_datos):
    predicciones = modelo.predict(df_nuevos_datos)
    df_nuevos_datos['Precio Predicho'] = predicciones
    return df_nuevos_datos
