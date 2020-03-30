

# %% Informational Metadata
def add(x:int, y:int) -> int:
    return x + y

help(add)

# %% Anonymous functions (lambdas)
add = lambda x, y: x + y
add(3, 4)

# %%
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
sorted(names, key=lambda name: name.split()[-1].lower())

# %% Wraping functions
# https://realpython.com/primer-on-python-decorators/
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("before")
        res = func(*args, **kwargs)
        print("after")
        return res
    return wrapper

@decorator
def whooa():
    '''
    Function description goes here!
    '''
    print("hola")

whooa()
print(whooa.__name__)
help(whooa)

# %%
