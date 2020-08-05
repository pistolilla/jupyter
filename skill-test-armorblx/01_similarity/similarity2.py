# %%
# Some test examples
t1 = "The quick, brown fox jumps over the lazy dog."
t2 = "The quick brown fox jumps over the lazy wolf!"
t3 = "a rose is a rose is a rose"
corpus = [t1, t2, t3]


# %%
from sklearn import feature_extraction, model_selection
from scipy import spatial
import numpy as np
# %%
Vectorizer = feature_extraction.text.CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words="english")


# %%
def rank (search, corpus):
    result = []
    # fitting
    Vectorizer.fit(corpus + [search])
    # transforming search
    tv = Vectorizer.transform([search])
    tv = np.array(tv.todense())[0]

    for x in corpus:
        xv = Vectorizer.transform([x])
        xvector = np.array(xv.todense())[0]
        distance = 1 - spatial.distance.cosine(tv, xvector)
        print(Vectorizer.inverse_transform(xv))
        result.append((distance, x))

    result = sorted(result, reverse=True)
    return result

rank("the rosa jumps over a dog", corpus)