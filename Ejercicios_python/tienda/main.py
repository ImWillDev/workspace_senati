import pandas as pd
import matplotlib.pyplot as plt
import os

#creamos listas de los productos vantas y precios 
productos = [
    'Teclado', 'Ratón', 'Monitor', 'CPU', 'Memoria RAM', 
    'Disco Duro', 'Fuente de Poder', 'Placa Base', 'Impresora', 'Webcam'
]
cantidades_vendidas = [50, 150, 380, 40, 70, 30, 60, 45, 20, 100]
precios = [30, 20, 150, 500, 80, 100, 70, 120, 200, 60]
#se crea un dict para poder convetilo a data frame
data = {
    'producto': productos,  
    'cantidad_vendida': cantidades_vendidas, 
    'precio': precios, 
    'fecha_venta': pd.date_range(start='2024-08-01', periods=len(productos), freq='D')
}


df = pd.DataFrame(data)




df['total_generado'] = df['cantidad_vendida'] * df['precio']

print (df[['producto', 'total_generado']])
# Total de ventas por producto
ventas_por_producto = df.groupby('producto')['cantidad_vendida'].sum()

# Guardar en CSV
guardar_csv = os.path.join('data', 'ventas_infotel.csv')
df.to_csv(guardar_csv, index=False)
print(f"Datos guardados en {guardar_csv}")

#calcular producto mas vendido
producto_mas_vendido = df.loc[df['cantidad_vendida'].idxmax()]['producto']
                                                               
print(f"El producto mas vendido fue {producto_mas_vendido}")

# más de 200 unidades vendidas
productos_mas_200 = ventas_por_producto[ventas_por_producto > 200]
print("Productos con más de 200 unidades vendidas:")
print(productos_mas_200)

# Crear gráfico 
plt.figure(figsize=(12, 7))
ventas_por_producto.plot(kind='bar', color='teal')
plt.title('Ventas Totales Infotel')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')

plt.show()

