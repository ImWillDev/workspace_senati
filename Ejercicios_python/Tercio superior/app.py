import pandas as pd 
import matplotlib.pyplot as plt

data_estudantes = {
    "Estudiante":['Juan', 'Ana', 'Carlos', 'Laura', 'Pedro', 'Marta', 'Luis', 'Isabel', 'Roberto', 'Silvia'],
    "promedio": [16, 19, 12, 18, 10, 20, 15, 18, 13, 17],
}

df = pd.DataFrame(data_estudantes)

print (df)

# Calcular el umbral del tercio superior
tercio_superior = df['promedio'].quantile(2/3)

print ("----------------------------------------------------------------")
print (tercio_superior)
estudiantes_tercio_superior = df[df['promedio'] >= tercio_superior]
print ("----------------------------------------------------------------")
print(f'Los estudiantes de tercio supeiror se encuentran: \n {estudiantes_tercio_superior}')
print ("----------------------------------------------------------------")


#Realizar graficas 
plt.figure(figsize=(10, 6))
plt.bar(df['Estudiante'], df['promedio'], color='green')
plt.axhline(y=tercio_superior, color='red', linestyle='--', label='Tercio Superior')
plt.title('Distribución de Promedios de los Estudiantes')
plt.xlabel('Nombre del Estudiante')
plt.ylabel('Promedio')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
plt.close()



# PAra los becados 
plt.title('imagen')
plt.figure(figsize=(10, 6))
plt.bar(estudiantes_tercio_superior['Estudiante'], estudiantes_tercio_superior['promedio'], color='green')
plt.title('Promedios de Estudiantes en el Tercio Superior')
plt.xlabel('Nombre del Estudiante')
plt.ylabel('Promedio')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
plt.close() 
