# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
x = np.arange(10)
y = np.exp(np.arange(10))
z = np.arange(10) ** 2
plt.plot(x, x)

# %%
plt.figure()
plt.subplot(121)
plt.plot(x, y)
plt.subplot(122)
plt.scatter(x, z)

# %%
aver = plt.figure(figsize=(10,6))
plt.plot(x, y)

# %%
fig, ax = plt.subplots(figsize=(17, 9)) # set size
ax.plot(x, y, marker='o', linestyle='', color='red', ms=20, label=y, mec='none')
ax.plot(x, x, color='blue')
ax.set_aspect('auto')

# %%
data = np.random.randn(2,3)
data

# %%
