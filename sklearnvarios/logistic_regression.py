# %%
import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pandas as pd
from collections import Counter

# %%
iris = datasets.load_iris()
iris.data

# %%
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df

# %%
df.plot(kind="hist")

# %%
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.9, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# %%
y_predict = model.predict(X_test)
Counter([p==t for p,t in zip(y_predict, y_test)])
# %%
model.score(X_test, y_test)

# %%
print(classification_report(y_test, y_predict, iris.target))

# %%
