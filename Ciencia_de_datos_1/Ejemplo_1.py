import pandas as pd

# Ingresa datos en una variable data en un diccionario con columnas y sus valores son notas
data = {
    'Nota1': [8, 9, 7, 6, 8, 9, 9, 20, 5],
    'Nota2': [9, 8, 7, 6, 8, 9, 9, 20, 5],
    'Nota3': [7, 6, 8, 9, 8, 9, 9, 20, 5],
    'Nota4': [6, 5, 9, 8, 8, 9, 9, 20, 7],
    'Nota5': [5, 7, 6, 5, 8, 9, 9, 20, 9],
    'Nota6': [5, 7, 6, 5, 8, 9, 9, 20, 9],
    'Nota7': [5, 7, 6, 5, 8, 9, 9, 20, 9],
    
    'grupo': ['A', 'B', 'A', 'B', 'A','B', 'A', 'B', 'A']
}

# Crea un DataFrame a partir de la variable data
df = pd.DataFrame(data)

# Imprime las primeras y últimas filas del DataFrame
print(f'Primeras filas \n{df.head()} \nÚltimas filas \n{df.tail()}')
#haciendo slicing 
S_filas = df[:3]
print(f'Segmento de filas \n {S_filas}')
S_columnas = df[['Nota1','Nota4']]
print(f'Segmento de columnas \n {S_columnas}')
