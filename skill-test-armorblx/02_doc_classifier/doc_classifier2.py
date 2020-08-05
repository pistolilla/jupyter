# %% imports
import os
import pandas as pd

# %%
dir = "C:/Leo/NLP/skill-test-armorblx/02_doc_classifier/enron"
df = pd.DataFrame()

for root, dirs, files in os.walk(dir):
    for name in files:
        fullname = os.path.join(dir, name)
        print(fullname)
        _df = pd.read_csv(fullname)
        df = pd.concat([df, _df])

df = df.dropna()


# %%
from sklearn import feature_extraction, model_selection, svm, linear_model, metrics

# %%
x = df["content"].tolist()
y = df["sender"].tolist()
x

# %%

Vectorizer = feature_extraction.text.TfidfVectorizer(min_df=2, ngram_range=(1,2))
x = Vectorizer.fit_transform(x)
x

# %%
X_train, X_test, y_train, y_test= model_selection.train_test_split(x, y, test_size=0.2)

# %%
svm_model = svm.LinearSVC()
svm_model.fit(X_train, y_train)
svm_model.score(X_test, y_test)

# %%
lr_model = linear_model.LogisticRegression()
lr_model.fit(X_train, y_train)
lr_model.score(X_test, y_test)

# %%
y_pred = svm_model.predict(X_test)
print(metrics.classification_report(y_test, y_pred))

# %%
df2 = pd.DataFrame({"test": y_test, "pred": y_pred})
df2[df2["test"] != df2["pred"]]



# %%
