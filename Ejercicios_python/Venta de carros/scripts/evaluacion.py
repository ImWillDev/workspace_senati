import matplotlib.pyplot as plt
import os
import pandas as pd
from . import preprocesamiento



def evaluar_modelo(modelo, df):
    X_train, X_test, y_train, y_test = preprocesamiento.dividir_datos(df)
    y_pred = modelo.predict(X_test)
    df_resultados = pd.DataFrame({'Precio Real': y_test, 'Precio Predicho': y_pred})
    return df_resultados

def graficar_resultados(df_resultados, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df_resultados['Precio Real'], df_resultados['Precio Predicho'], color='blue')
    plt.plot([df_resultados['Precio Real'].min(), df_resultados['Precio Real'].max()],
             [df_resultados['Precio Real'].min(), df_resultados['Precio Real'].max()],
             color='red', linestyle='--')
    plt.xlabel('Precio Real')
    plt.ylabel('Precio Predicho')
    plt.title('Comparación entre Precio Real y Predicho')
    plt.savefig(os.path.join(save_dir, 'comparacion_precio_real_vs_predicho.png'))
    plt.show()
