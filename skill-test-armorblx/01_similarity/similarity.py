# %%
import re
from sklearn import feature_extraction
import numpy as np
import scipy

# %%
# Some test examples
t1 = "The quick, brown fox jumps over the lazy dog."
t2 = "The quick brown fox jumps over the lazy wolf!"
t3 = "a rose is a rose is a rose"
corpus = [t1, t2, t3]
corpus

# %%
tokenized = [re.split(r'\s+', str.lower()) for str in corpus]
tokenized

# %%
vectorizer = feature_extraction.text.CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words='english')

# %%
def get_sim(search, compare):
    sim = [(1 - scipy.spatial.distance.cosine(search, compare))]
    return sim

# %%
def rank(search, corpus):
    vectorizer.fit(corpus + [search])
    for t2 in corpus:
        v1 = vectorizer.transform([search])
        v1 = np.mean(np.array(v1[0].todense()), axis=0)
        v2 = vectorizer.transform([t2])
        v2 = np.mean(np.array(v2[0].todense()), axis=0)
        sim = get_sim(v1,v2)
        s2 = vectorizer.inverse_transform(list(v2))
        yield (sim, t2, s2)

# %%
for res in sorted(rank("The quick brown fox jumps over a lazy cat", corpus), reverse=True):
    print(res)

# %%
