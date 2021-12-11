#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

datos = pd.read_csv('dataframe.csv',sep=',')


# In[4]:


datos


# In[5]:


names = set(datos['LanguageName'])


# In[6]:


names


# In[7]:


palabras = set(datos['WordModernName1'])


# In[8]:


palabras


# In[51]:


palabras_elegidas = palabras #['zorro','tres'] ## puedes agregar más


# In[52]:


dict_datos = {L:{} for L in names}


# In[53]:


for L in names:
    for word in palabras_elegidas:
        D = datos[datos['LanguageName']==L]
        try:
            dict_datos[L][word]=list(D[D['WordModernName1']==word]['Phonetic'])[0]
        except IndexError:
            dict_datos[L][word]='unk'


# In[54]:


dict_datos


# In[55]:


import itertools
pares_localidades = list(itertools.product(list(dict_datos.keys()), list(dict_datos.keys())))


# In[56]:


pares_localidades


# In[57]:


## aquí guardas las distancias

distancias = {L:{LL:0 for LL in list(dict_datos.keys())} for L in list(dict_datos.keys())}


# In[58]:


get_ipython().system('pip install jellyfish')


# In[59]:


import jellyfish

def funcion_distancia(string1,string2):
    #return 1-jellyfish.jaro_winkler_similarity(string1,string2)
    return jellyfish.levenshtein_distance(string1,string2)/max(len(string1),len(string2))


# In[60]:


## tienes q recorrer pares_localidades

for par in pares_localidades:
    D = 0
    words1 = dict_datos[par[0]]
    words2 = dict_datos[par[1]]
    words1and2 = list(set(words1) & set(words2))
    for word in words1and2:
        D += funcion_distancia(dict_datos[par[0]][word],dict_datos[par[1]][word])
    distancias[par[0]][par[1]]=D/len(words1and2)


# In[61]:


distancias


# In[62]:


DF = pd.DataFrame.from_dict(distancias)


# In[63]:


DF


# In[64]:


DF.to_excel('distancias.xlsx')


# In[ ]:





# In[ ]:




