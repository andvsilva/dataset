#!/usr/bin/env python
# coding: utf-8

# In[97]:


import pandas as pd
import numpy as np


# In[98]:


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


# In[99]:


train.head()


# In[122]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold


# In[123]:


X_falso = np.arange(10)
X_falso


# In[124]:


np.random.seed(0)#para sempre ter a mesma sequência ou valor, gerar a divisão aleatória.
#controlar a aleatoriedade da divisão e poder comparar entre modelos entre validações.
train_test_split(X_falso, test_size=0.5) #random_state crie nas mesma condições de aleatoriedade 


# In[125]:


np.random.seed(0)
X_treino, X_valid, y_treino, y_valid= train_test_split(X,y, test_size= 0.5)


# In[126]:


X_treino.head() 


# In[127]:


X_treino.shape, X_valid.shape, y_treino.shape, y_valid.shape
# o y treino tem o mesmo número de exemplos de linha do que o x treino
# o y_valid tem o mesmo número de linhas que o X_valid
#o y é a verdade se a pessoa sobreviveu ou não. 


# In[128]:


modelo = RandomForestClassifier(n_estimators=100, n_jobs=-1,
                               random_state=0 )
modelo.fit(X_treino, y_treino)


# In[129]:


p = modelo.predict(X_valid)


# In[130]:


#Y_valid que é as resposta para esse conjunto de dados (X_valid)
y_valid ==p #retorna uma lista de verdadeiro e falsos


# In[131]:


np.mean(y_valid ==p)


# In[132]:


p = (X_valid["Sex_binario"] ==1).astype(np.int64)
np.mean(y_valid==p)
#prevendo para todas as mulheres que elas vão sobreviver
#a validação está consistente no que eu possa esperar receber dos dados
#no ambiente em que esse modelo será usado no mundo real? se sim
#a validação está correta.


# In[133]:


def transformar_sexo(valor):
    if valor == "female":
        return 1
    else:
        return 0
train["Sex_binario"] = train["Sex"].map(transformar_sexo)


# In[134]:


train.head()


# In[135]:


variaveis = ["Sex_binario", "Age"]


# In[136]:


X = train[variaveis]
y = train["Survived"]


# In[137]:


X.head()


# In[138]:


X = X.fillna(-1)


# In[139]:


modelo.fit(X,y)


# In[140]:


test["Sex_binario"] = test["Sex"].map(transformar_sexo)


# In[141]:


X_prev = test[variaveis]
X_prev = X_prev.fillna(-1)
X_prev.head()


# In[142]:


p = modelo.predict(X_prev)
p


# In[143]:


test.head()


# In[144]:


sub = pd.Series(p, index=test["PassengerId"], name="Survived")
sub.shape


# In[145]:


sub


# # Validação Cruzada

# In[146]:


X_falso


# In[147]:


kf = KFold(3, shuffle=True, random_state=)
for linhas_treino, linhas_valid in kf.split(X_falso):
    print("Treino:", linhas_treino)
    print("Valid:", linhas_valid)
    print()


# In[151]:


resultados = []
for rep in range(10):
    print("Rep:", rep)
    kf = KFold(5, shuffle=True, random_state=rep)
    
    for linhas_treino, linhas_valid in kf.split(X):
        print("Treino:", linhas_treino.shape[0])
        print("Valid:", linhas_valid.shape[0])

        X_treino, X_valid = X.iloc[linhas_treino], X.iloc[linhas_valid]
        y_treino, y_valid = y.iloc[linhas_treino], y.iloc[linhas_valid]

        modelo = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)
        modelo.fit(X_treino, y_treino)

        p = modelo.predict(X_valid)

        acc = np.mean(y_valid == p)
        resultados.append(acc)
        print("Acc:", acc)
        print()
        #print(X_treino.head())
        #print()


# In[152]:


len(resultados)


# In[153]:


np.mean(resultados)


# In[ ]:




