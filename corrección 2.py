#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

datos = pd.read_csv('dataframe.csv',sep=',')


# In[3]:


datos


# In[4]:


names = set(datos['LanguageName'])


# In[5]:


names


# In[6]:


palabras = set(datos['WordModernName1'])


# In[7]:


palabras


# In[8]:


palabras_elegidas = ['zorro'] ## puedes agregar más


# In[9]:


dict_datos = {L:{} for L in names}


# In[10]:


for L in names:
    for word in palabras_elegidas:
        D = datos[datos['LanguageName']==L]
        try:
            dict_datos[L][word]=list(D[D['WordModernName1']==word]['Phonetic'])[0]
        except IndexError:
            dict_datos[L][word]='unk'


# In[11]:


dict_datos


# In[12]:


import itertools
pares_localidades = list(itertools.product(list(dict_datos.keys()), list(dict_datos.keys())))


# In[13]:


pares_localidades


# In[14]:


## aquí guardas las distancias

distancias = {L:{LL:0 for LL in list(dict_datos.keys())} for L in list(dict_datos.keys())}


# In[15]:


get_ipython().system('pip install jellyfish')


# In[18]:


import jellyfish

def funcion_distancia(string1,string2):
    return jellyfish.levenshtein_distance(string1,string2)


# In[19]:


## tienes q recorrer pares_localidades

for par in pares_localidades:
    distancias[par[0]][par[1]]=funcion_distancia(dict_datos[par[0]]['zorro'],dict_datos[par[1]]['zorro'])


# In[20]:


distancias


# In[22]:


DF = pd.DataFrame.from_dict(distancias)


# In[23]:


DF


# In[26]:


DF.to_excel('distancias.xlsx')


# In[ ]:




