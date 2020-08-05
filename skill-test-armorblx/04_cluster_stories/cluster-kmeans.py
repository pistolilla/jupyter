import os
from sklearn import cluster, feature_extraction, metrics
import matplotlib.pyplot as plt

# %%
#dir = "C:\\Users\\usuario\\Desktop\\stories"
dir = "C:\\Leo\\NLP\\skill-test-armorblx\\04_cluster_stories\\stories"
for root, dirs, files in os.walk(dir, topdown=False):
   for name in files:
      print(os.path.join(root, name))

# %%
corpus = []
for root, dirs, files in os.walk(dir):
    for name in files:
        with open(os.path.join(root, name), errors="ignore") as f:
            #print(f.read())
            corpus.append(f.read())

# %%
print(corpus[1])

# %%
Vectorizer = feature_extraction.text.TfidfVectorizer(stop_words='english', min_df=2, max_features=1000)
X = Vectorizer.fit_transform(corpus)

# %%
avgs = []
centroids = []
max_k = 30
for k in range(2, max_k):
    Model = cluster.KMeans(n_clusters=k)
    Model.fit(X)
    avgs.append(metrics.silhouette_score(X, Model.labels_))
    centroids.append(Model.cluster_centers_)

# %%
#plt.plot(avgs)
plt.scatter(range(2, max_k), avgs)

# %%
deltas = []
for i in range(len(avgs)-1):
    delta = avgs[i+1] - avgs[i]
    deltas.append((delta, i + 1))

# %%
from heapq import nlargest
nlargest(3, deltas, key=lambda x: x[0])


# %%
