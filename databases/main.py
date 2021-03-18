import pandas as pd # Se importa la librería pandas

inf=pd.read_csv("weatherAUS.csv") # Se declara una variable inf que va dirigida a pandas como lectura de archivos
print(inf.head()) # Se imprime lo que hay al principio del documento
print("--------------------------------------------------") #Espacio
print(inf.describe()) # Se imprimen los datos estadísticos importantes de varias columnas


