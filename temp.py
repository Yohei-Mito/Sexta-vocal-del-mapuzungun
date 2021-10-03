
# Librerías para unir los csv en un solo dataframe y también para manipularlos.

import pandas as pd

import glob

import os


all_csv = glob.glob("/Users/Eduardo/Documents/Universidad/MAGISTER LINGÜÍSTICA UCHILE/SEGUNDO SEMESTRE 2021/LINGüíSTICA COMPUTACIONAL/Datos/*.csv")


len(all_csv) # para verificar el tamaño de la lista.


csv_list = []

for csv in all_csv:
    
    datos = pd.read_csv(csv)
    
    nombre = os.path.basename(csv)
    
    datos["source_csv"] = nombre # nueva columna conteniendo el nombre del fichero leido.
    
    csv_list.append(datos)


df = pd.concat(csv_list, ignore_index = True) # axis = 0 o axis = 1

df.head(n=100) # para mirar los datos iniciales
df.tail(n=100) # para mirar los datos finales


# Elimina las columnas con información no útil.

dataframe = df.drop(columns=['WordModernName2','WordProtoName1','WordProtoName2','SpellingAltv2', 'NotCognateWithMainWordInThisFamily'])


# Exporta el dataframe en un archivo csv en el directorio definido con anterioridad.

dataframe.to_csv('dataframe.csv')