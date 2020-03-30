import numpy as np
import random

# %% Formating data
x = 1234.56789
# Two decimal places of accuracy
print(format(x, '0.2f'))
print("The answer is: {:0.2f}".format(x))
# Inclusion of thousands separator
print(format(x, '0,'), format(x, '0,.1f'), sep='\t\t')

swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))

# %% Infinity and NaNs
print(float('-inf'))
print(float('nan'))

# %% Numerical Arrays
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

# %%
# Fast creation
grid = np.zeros(shape=(10,10), dtype=float)
grid += 10
grid

# %%
# random creation
newgrid = np.random.rand(3, 2)
newgrid

# %%
# Selecting subregions
a = np.arange(1, 17).reshape(4, 4)
print(a)
print(a[:,1])
print(a[2,:])

# %%
# Broadcast a row vector
b = [100, 101, 102, 103]
print(a + b)
# Broadcast a column vector
b = np.array(b).reshape(4, 1)
print(a + b)

# %%
# Conditional assignment on an array
np.where(b > 100, b, 0)

# %% Matrix and linear algebra
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m.T

# %% Picking things at random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
random.shuffle(values)
print(values)
random.sample(values, 3)

# %%
random.seed(42)
random.randint(0,100)

# %%
random.seed(None)
random.random()

# %%
