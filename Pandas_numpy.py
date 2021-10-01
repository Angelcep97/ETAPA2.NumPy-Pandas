import numpy as np
import pandas as pd

SEPARADOR = ("*" * 20) + "\n"

#Crear una serie con valores iniciales
notas = pd.Series([87, 100, 85, 60, 78])
print(type(notas))
print(SEPARADOR)

#Crear una seriede 6 elementos que tengas el mismo valor
iguales = pdSeries(100, range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)


#Estadisitca Descriptiva para una serie
print('Notas : ')
print(f"{notas}")
print(f"Cantidad = {notas.count()}")
print(f"Media = {notas.mean()}")
print(f"Minimo = {notas.min()}")
print(f"Maximo = {notas.max()}")
print(f"Desviacion Estadnar = {notas.std()}")
print("Sumarizacion Descriptiva: ")
print(notas.describe())
print(SEPARADOR)