# %%
from sklearn.feature_extraction import DictVectorizer
import pandas as pd

# %%
x = [
    {"a": 3, "b": 3, "c": "hola"},
    {"a": 3, "b": 3, "c": "asdf"},
    {"z": 3, "b": 4, "c": "hfdsafola"},
    {"x": True, "b": 5, "c": "hofdsafla"}
]
x
# %%
vectorizer = DictVectorizer()
X = vectorizer.fit_transform(x)
X.todense()


# %%
xd = np.array(X.todense())
df = pd.DataFrame(xd, columns=vectorizer.feature_names_)
df

# %%
