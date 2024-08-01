#importamos librerias
import pandas as pd


# Solicita al usuario el rango de años
inicio = int(input("Ingrese el año de inicio: "))
fin = int(input("Ingrese el año de fin: "))
print("------------------------------------------------------")

# Verifica rango de años y crea diccionario 
if fin < inicio:
    print("El año de fin debe ser mayor o igual al año de inicio.")
else:
    ventas = {}

    # Solicita montos para cada año 
    for año in range(inicio, fin):
        ventas[año] = float(input(f"Ingrese el monto de ventas para el año {año}: "))
        ventas = pd.Series(ventas)

    ventas_con_descuento_10 = ventas * 0.9
    ventas_con_descuento_igv = ventas * (1 - 0.18)
    ventas_con_igv_y_descuento = ventas_con_descuento_igv * 0.9
#imprime sets con descuento del 10% y con deceunto de igv
print("------------------------------------------------------")
print(f'Ventas con descuento del 10%: {ventas_con_descuento_10}')
print("------------------------------------------------------")
print(f'Ventas con descuento de igv: {ventas_con_descuento_igv}')
print("------------------------------------------------------")
#con descuento de ivg y de
print(f'Ventas precio con ambos descuentos:  {ventas_con_igv_y_descuento}')
print("------------------------------------------------------")

print(ventas)
