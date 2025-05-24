#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Name: DEEPAK R")
print("Reg No:212223040031")


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Mall_Customers.csv")


# In[2]:


data.head()


# In[3]:


data.info()


# In[4]:


data.isnull().sum()


# In[5]:


from sklearn.cluster import KMeans
wcss = []


# In[6]:


for i in range(1,11):
  kmeans = KMeans(n_clusters = i, init = "k-means++")
  kmeans.fit(data.iloc[:, 3:])
  wcss.append(kmeans.inertia_)


# In[7]:


plt.plot(range(1, 11), wcss)
plt.xlabel("No. of Clusters")
plt.ylabel("wcss")
plt.title("Elbow Method")


# In[8]:


km = KMeans(n_clusters = 5)
km.fit(data.iloc[:, 3:])


# In[9]:


y_pred = km.predict(data.iloc[:, 3:])
y_pred


# In[10]:


data["cluster"] = y_pred
df0 = data[data["cluster"] == 0]
df1 = data[data["cluster"] == 1]
df2 = data[data["cluster"] == 2]
df3 = data[data["cluster"] == 3]
df4 = data[data["cluster"] == 4]
plt.scatter(df0["Annual Income (k$)"], df0["Spending Score (1-100)"], c = "red", label = "cluster0")
plt.scatter(df1["Annual Income (k$)"], df1["Spending Score (1-100)"], c = "black", label = "cluster1")
plt.scatter(df2["Annual Income (k$)"], df2["Spending Score (1-100)"], c = "blue", label = "cluster2")
plt.scatter(df3["Annual Income (k$)"], df3["Spending Score (1-100)"], c = "green", label = "cluster3")
plt.scatter(df4["Annual Income (k$)"], df4["Spending Score (1-100)"], c = "magenta", label = "cluster4")
plt.legend()
plt.title("Customer Segments")

