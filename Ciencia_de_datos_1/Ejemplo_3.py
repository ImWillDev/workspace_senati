import pandas as pd

# Diccionario con las notas de los estudiantes
notas = {
    "Juan": [8.5, 15, 10, 7.2, 9.4],
    "Pedro": [7.8, 6.9, 8.1, 7.3],
    "Ana": [9.2, 8.7, 9.5, 8.9],
    "Luis": [6.5, 7.0, 5.8, 6.2],
    "Maria": [8.8, 9.0, 9.3, 8.6],
    "Carlos": [9.0, 8.5, 9.1, 8.8],
    "Sofia": [7.0, 6.8, 7.5, 7.1],
    "Juan2": [8.5, 8.2, 8.9, 8.4]
}

def estadisticas_notas(notas):

    resultados = {}
    
    for estudiante, lista_notas in notas.items():
        notas_estudiante = pd.Series(lista_notas)
        nota_max = round(notas_estudiante.max(),2)
        nota_min = round(notas_estudiante.min(),2)
        mediana = round(notas_estudiante.median(),2)
        desviacion_tipica = round(notas_estudiante.std(),2)
        
        # Guardar Series en un diccionario de resultados
        resultados[estudiante] = pd.Series({
            'Nota Maxima': nota_max,
            'Nota Minima': nota_min,
            'Mediana': mediana,
            'Desviación Típica': desviacion_tipica
        })
    
    # Convertir el diccionario de Series en un DataFrame
    resultados_df = pd.DataFrame(resultados)
    return resultados_df

# Obtener las estadísticas y mostrar el resultado
salida = estadisticas_notas(notas)
print(salida)
