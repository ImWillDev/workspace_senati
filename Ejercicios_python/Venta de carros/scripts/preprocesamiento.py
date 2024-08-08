import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def procesar_datos(df, es_nuevo=False):
    # Ejemplo de preprocesamiento básico: codificación de variables categóricas
    label_encoders = {}
    for column in ['Marca', 'Modelo']:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        if not es_nuevo:
            label_encoders[column] = le
    
    # Escalado de las características numéricas
    scaler = StandardScaler()
    df[['Año', 'Kilometraje']] = scaler.fit_transform(df[['Año', 'Kilometraje']])
    
    return df

def dividir_datos(df):
    X = df.drop(columns=['Precio'])
    y = df['Precio']
    return train_test_split(X, y, test_size=0.2, random_state=42)
