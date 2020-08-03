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






## Example 2
# %%
from sklearn.datasets import make_classification
from sklearn.pipeline import Pipeline
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

# %%
X, y = make_classification(n_classes=3, n_informative=10, n_clusters_per_class=1)
print(X.shape)
print(y.shape)
Counter(y)

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# %%
model = Pipeline([
    #("SVD", TruncatedSVD(5)),
    #("Normalizer", Normalizer()),
    ("LogReg", LogisticRegression())
    #("SVM", LinearSVC())
])
model.fit(X_train, y_train)


# %%
y_predict = model.predict(X_test)

# %%
print(classification_report(y_test, y_predict))

# %%
train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, train_sizes=np.linspace(0.01, 1.0, 50), cv=5)


# %%
# Create means and standard deviations of training set scores
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
# Create means and standard deviations of test set scores
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# %%
# Draw lines
plt.plot(train_sizes, train_mean, '--', color="#111111",  label="Training score")
plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

# Draw bands
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

# Create plot
plt.title("Learning Curve")
plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), plt.legend(loc="best")
plt.tight_layout()
plt.show()

# %%
