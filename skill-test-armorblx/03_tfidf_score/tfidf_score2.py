# %%
import pandas as pd
from sklearn.feature_extraction import text
import os

# %%
dir = os.path.dirname(__file__)
file = os.path.join(dir, "jones_t_mails.csv")
file

# %%
df = pd.read_csv(file)
df

# %%
notblank = df["content"].apply(lambda x: len(str(x)) > 3)
df = df[notblank]

# %%
X = df["content"]

# %%
TfIdfVectorizer = text.TfidfVectorizer()
TfIdfVectorizer.fit(X)

# %%
idfdf = pd.DataFrame({"names" : TfIdfVectorizer.get_feature_names(), "idf" : TfIdfVectorizer.idf_})
idfdf.sort_values(by=["idf"], ascending=False)
# %%
