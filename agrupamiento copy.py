# Imports 
import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import KMeans

# Leer usuario 
data = pd.read_csv('')
X = np.array(data)

# Consstantes del sistema
number_of_clusters = 6

#Aplicar el algoritmo Kmeans a DATA
kmeans = KMeans(
	n_clusters=6,
	init='k-means++',
	n_init=10,
    max_iter=300,
	random_state=2
	)

kfit = kmeans.fit(X)
print(kfit)

freeze_centroids = kmeans.cluster_centers_
print(freeze_centroids)
print(freeze_centroids.shape)

# Salvar los centroides como un archivo pickle localmente
with open('freezed_centroids.pkl','wb') as f:
    pickle.dump(freeze_centroids, f)
    print('Los centroides fueron guardados como un archivo pickle localmente.')