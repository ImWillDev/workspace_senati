import pickle
from sklearn.linear_model import LinearRegression
from . import preprocesamiento


def entrenar_modelo(df):
    # Divide los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = preprocesamiento.dividir_datos(df)
    
    # Inicializa y entrena el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    return modelo

def guardar_modelo(modelo, path):
    # Guarda el modelo entrenado en un archivo pickle
    with open(path, 'wb') as file:
        pickle.dump(modelo, file)

