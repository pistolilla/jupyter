import os
import pandas as pd

# %%
dir = "C:\\Users\\usuario\\Desktop\\enron"

df = pd.DataFrame()
for path in os.listdir(dir):
    subdf = pd.read_csv(os.path.join(dir, path))
    #df.concat([subdf], axis=1)
    df = df.append(subdf, ignore_index=True)

# %%
df.head()

# %%
df.tail()

# %%
df=df.dropna()

# %%
from sklearn import linear_model, svm
from sklearn import feature_extraction
from sklearn import model_selection

# %%
X = df['content'].tolist()
y = df['sender'].tolist()
X
y

# %%
Vectorizer = feature_extraction.text.TfidfVectorizer(stop_words='english', min_df=2, ngram_range=(1,2))
X = Vectorizer.fit_transform(X)

# %%
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, stratify=y)

# %%
#Model = svm.LinearSVC()
Model = linear_model.LogisticRegression()
Model.fit(X_train, y_train)

# %%

Model.score(X_test, y_test)
y_pred = Model.predict(X_test)
y_pred

# %%
from sklearn import metrics
print(metrics.classification_report(y_test, y_pred))


# %%
df2 = pd.DataFrame([y_test, y_pred])

# %%
Vectorizer.get_feature_names

# %%

# %%
