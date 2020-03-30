import itertools

# %% Manually Consuming an Iterator
items = [1, 2, 3]
it = iter(items) # Invokes items.__iter__()
while True:
    n = next(it, None) # Invokes items.__next__()
    if n == None:
        break
    print(n)

# %% Iterating in Reverse
a = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
[a for a in reversed(a)] # Invokes __reversed__()

# %% Taking a Slice of an Iterator
for x in itertools.islice(iter(a), 1, 5):
    print(x)

# %% Permutations
items = ['a', 'b', 'c']
[p for p in itertools.permutations(items)]

# %%
[c for c in itertools.combinations(items, 2)]

# %%
[c for c in itertools.combinations_with_replacement(items, 2)]

# %% Index-Value Pairs
my_list = ['a', 'b', 'c']
{idx:val for idx, val in enumerate(my_list)}

# %% Iterating Over Multiple Sequences Simultaneously
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
#[(x, y) for x, y in zip(xpts, ypts)]
list(zip(xpts, ypts))

# %% zip_longest
[(x, y) for x, y in itertools.zip_longest(xpts, [1] * 3 + ypts, fillvalue=float('nan'))]

# %% Efficient concatenation
[x for x in itertools.chain(xpts, ypts)]

# %% Merge sorted
import heapq
a = [1, 4, 7, 10]
b = [2, 5, 7, 11]
for c in heapq.merge(a, b):
    print(c)

# %%
