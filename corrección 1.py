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


# In[7]:


palabras = set(datos['WordModernName1'])


# In[8]:


palabras


# In[34]:


palabras_elegidas = ['zorro'] ## puedes agregar más


# In[35]:


dict_datos = {L:{} for L in names}


# In[36]:


for L in names:
    for word in palabras_elegidas:
        D = datos[datos['LanguageName']==L]
        try:
            dict_datos[L][word]=list(D[D['WordModernName1']==word]['Phonetic'])[0]
        except IndexError:
            dict_datos[L][word]='unk'


# In[37]:


dict_datos


# In[40]:


import itertools
pares_localidades = list(itertools.product(list(dict_datos.keys()), list(dict_datos.keys())))


# In[41]:


pares_localidades


# In[42]:


## aquí guardas las distancias

distancias = {L:{LL:0 for LL in list(dict_datos.keys())} for L in list(dict_datos.keys())}


# In[43]:


def funcion_distancia(string1,string2):
    ## tu función!!!
    return 0


# In[44]:


## tienes q recorrer pares_localidades

for par in pares_localidades:
    distancias[par[0]][par[1]]=funcion_distancia(dict_datos[par[0]]['zorro'],dict_datos[par[1]]['zorro'])


# In[45]:


distancias


# In[ ]:




