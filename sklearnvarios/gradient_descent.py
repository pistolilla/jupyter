# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
X = np.random.rand(100, 1)
X.shape

# %%
y = 4 + 3 * X + np.random.rand(100, 1)
y.shape
# %%
plt.plot(X, y, 'b.')

## Matrix approach
# %% adding a bias unit to X that is 1 for every vector in X
# like zip(ones, X)
def prepend_bias(X):
    return np.c_[np.ones((len(X), 1)), X]

X2 = prepend_bias(X)
X2

# %%
def prepend_bias(X):
    X2 = np.ones((len(X), 1))
    return np.concatenate((X2, X), axis=1)

X2 = prepend_bias(X)
X2

# %%
theta_best = np.linalg.inv(X2.T.dot(X2)).dot(X2.T).dot(y)
theta_best

## Using functions
# %%
def cost_func(theta,X,y):
    m = len(y)

    y_pred = X.dot(theta)
    loss = y_pred - y
    cost = m * (1/2) * np.sum(np.square(loss))
    return cost

def gradient_descent(X,y,theta,learning_rate=0.01,iterations=200):
    m = len(y)
    for i in range(iterations):
        y_pred = X.dot(theta)
        loss = y_pred - y
        gradient = X.T.dot(loss)
        theta = theta - learning_rate * (1/m) * gradient
        cost = cost_func(theta, X, y)
        #print(i, cost)
    return theta, cost

# %%
theta0 = np.random.randn(X.shape[1] + 1,1)
theta0

# %%
Xbias = prepend_bias(X)
theta, *_ = gradient_descent(Xbias,y,theta0, iterations=800)
print(theta)
print(_)

# %%
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# %%
diabetes = load_diabetes()
Xbias = prepend_bias(diabetes.data)
yreshaped = diabetes.target.reshape(len(Xbias), 1)
X_train, X_test, y_train, y_test = train_test_split(Xbias, yreshaped, test_size=0.33, random_state=42)

# %%
theta0 = np.random.randn(Xbias.shape[1],1)
theta0


# %%
theta, *_ = gradient_descent(X_train, y_train, theta0, learning_rate=0.1, iterations=1000)
theta.shape

# %%
y_predict = X_test.dot(theta)
y_predict

# %%
print(r2_score(y_test, y_predict))


# %%
