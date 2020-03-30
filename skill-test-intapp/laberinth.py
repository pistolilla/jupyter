# %%
import numpy as np

a = np.array(range(20))
a = a.reshape([4,5])
a

# %%
def getStrip(coll, row=True, first=True):
    axis = int(not row)
    shape = np.shape(coll)

    if first:
        n = 0
    else:
        n = shape[axis]

    if row:
        strip = coll[max(n - 1, 0),:]
    else:
        strip = coll[:,max(n - 1, 0)]

    remaining = np.delete(coll, max(n - 1, 0), axis=axis)
    return list(strip), remaining

getStrip(a, True, True)
# %%
getStrip(a, True, False)
# %%
getStrip(a, False, True)
# %%
getStrip(a, False, False)

# %%

row = True
first = True
left_to_right = True

b = a
i = 0
while len(b.flatten()) > 0:
    strip, b = getStrip(b, row, first)
    if not left_to_right:
        strip = reversed(strip)
    print(*strip)
    row = not row
    if i % 2 == 0:
        first = not first
    else:
        left_to_right = not left_to_right
    i += 1

# %%
