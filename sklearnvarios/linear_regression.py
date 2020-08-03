# %%
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
import matplotlib.pyplot as plt

# %%
diabetes = load_diabetes()
diabetes.target.shape

# %%
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df

# %%
plt.plot(df["age"], diabetes.target) #nonsense

# %%
X_train, X_test, y_train, y_test = train_test_split(df, diabetes.target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# %%
model.score(X_test, y_test)

# %%
mean_squared_error(y_test, y_pred)

# %%
from sklearn.datasets import make_regression

# %%
X, y = make_regression()
print(X.shape)
print(y.shape)

# %%
