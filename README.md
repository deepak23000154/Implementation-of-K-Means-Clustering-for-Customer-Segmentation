# Implementation-of-K-Means-Clustering-for-Customer-Segmentation

## AIM:
To write a program to implement the K Means Clustering for Customer Segmentation.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Jupyter notebook

## Algorithm
1. Data Preparation: Load data, handle missing values, and extract relevant features for clustering.

2. Determine Clusters: Use the Elbow Method to find optimal number of clusters based on WCSS.

3. K-Means Clustering: Fit the K-Means model with optimal clusters, predict cluster labels for data.

4. Visualization: Plot data points with distinct colors for each cluster to visualize clustering results.


## Program and Outputs:
```python
Program to implement the K Means Clustering for Customer Segmentation.
Developed by   : KIRAN G
RegisterNumber : 212223040095
```

<br>

```python
import pandas as pd
import matplotlib.pyplot as plt
```
<br>

```python
data = pd.read_csv("Mall_Customers.csv")
data.head()
```
<br>

![image](https://github.com/user-attachments/assets/906abd06-27b5-445f-a65f-49e6f1fb1579)

<br>

```python
data.info()
```
<br>

![image](https://github.com/user-attachments/assets/51267725-e943-4786-855b-c24de6ed01dc)

<br>

```python
data.isnull().sum()
```
<br>

![image](https://github.com/user-attachments/assets/e22e6ce0-f0dc-4e59-b90d-4367b0e7f067)

<br>

```python
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init="k-means++")
    kmeans.fit(data.iloc[:,3:])
    wcss.append(kmeans.inertia_)
```
<br>

```python
plt.plot(range(1,11), wcss)
plt.xlabel("No. of cluster")
plt.ylabel("wcss")
plt.title("Elbow method")
plt.show()
```
<br>

![image](https://github.com/user-attachments/assets/e36ea65f-44b1-47d1-ad52-bb84bfe31b8b)

<br>

```python
km = KMeans(n_clusters=5)
km.fit(data.iloc[:,3:])
y_pred = km.predict(data.iloc[:,3:])
y_pred
```
<br>

![image](https://github.com/user-attachments/assets/da81512b-8a07-42e8-9c21-58356021b2d2)

<br>

```python
data["clusters"]=y_pred
df0=data[data["clusters"]==0]
df1=data[data["clusters"]==1]
df2=data[data["clusters"]==2]
df3=data[data["clusters"]==3]
df4=data[data["clusters"]==4]
```
<br>

```python
plt.scatter(df0["Annual Income (k$)"],df0["Spending Score (1-100)"], color = "gold", label = "cluster 1")
plt.scatter(df1["Annual Income (k$)"],df1["Spending Score (1-100)"], color = "pink", label = "cluster 2")
plt.scatter(df2["Annual Income (k$)"],df2["Spending Score (1-100)"], color = "green", label = "cluster 3")
plt.scatter(df3["Annual Income (k$)"],df3["Spending Score (1-100)"], color = "blue", label = "cluster 4")
plt.scatter(df4["Annual Income (k$)"],df4["Spending Score (1-100)"], color = "red", label = "cluster 5")
plt.legend()
plt.show()
```
<br>

![image](https://github.com/user-attachments/assets/5eac60b2-7946-4155-bfba-fac8d3e9e742)

<br>

## Result:
Thus the program to implement the K Means Clustering for Customer Segmentation is written and verified using python programming.
