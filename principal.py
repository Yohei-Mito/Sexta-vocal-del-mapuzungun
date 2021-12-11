
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

dataframe = df.drop(columns=['LanguageId','WordId','WordModernName2','WordProtoName1','WordProtoName2','SpellingAltv2', 'NotCognateWithMainWordInThisFamily'])


# Exporta el dataframe en un archivo csv en el directorio definido con anterioridad.

dataframe.to_csv('dataframe.csv')



# función para medir distancia de Levenshtein "manualmente"


def LevenshteinD(word1, word2):
    m = len(word1)
    n = len(word2)
    table = [[0] * (n+1) for _ in range (m+1)]

    for i in range(m+1):
        table[i][0] = i
    for j in range(n+1):
        table[0][j] = j
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
   
    return table [-1][-1]
        
        
        


## CODIGO DE JAVIER PARA PASAR LOS DATOS DEL DATAFRAME A UN DICCIONARIO


import pandas as pd

datos = pd.read_csv('dataframe.csv',sep=',')

datos

names = set(datos['LanguageName'])

names

palabras = set(datos['WordModernName1'])

palabras

palabras_elegidas = ['persona_que_ensenya'] ## puedes agregar más
          
dict_datos = {L:{} for L in names}

for L in names:
    for word in palabras_elegidas:
        D = datos[datos['LanguageName']==L]
        try:
            dict_datos[L][word]=list(D[D['WordModernName1']==word]['Phonetic'])[0]
        except IndexError:
            dict_datos[L][word]='unk'

dict_datos


import itertools
pares_localidades = list(itertools.product(list(dict_datos.keys()), list(dict_datos.keys())))

pares_localidades


## aquí guardas las distancias

distancias = {L:{LL:0 for LL in list(dict_datos.keys())} for L in list(dict_datos.keys())}


def funcion_distancia(string1,string2):
    m = len(string1)
    n = len(string2)
    table = [[0] * (n+1) for _ in range (m+1)]

    for i in range(m+1):
        table[i][0] = i
    for j in range(n+1):
        table[0][j] = j
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])

    return table [-1][-1]


## tienes q recorrer pares_localidades

for par in pares_localidades:
    distancias[par[0]][par[1]] = funcion_distancia(dict_datos[par[0]]['persona_que_ensenya'],dict_datos[par[1]]['persona_que_ensenya'])



distancias

get_ipython().system('pip install jellyfish')


   
        
        
        
        