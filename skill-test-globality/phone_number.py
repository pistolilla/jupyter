
# %%
from collections import deque
table = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

# %%

input = [0, 1]
res = []
queue = deque()

#do:
cursor = 0
number_at_cursor = input[cursor]
for letter in table[number_at_cursor]:
    queue.append(letter)

while len(queue) > 0:
    print(queue)
    s = queue.pop()

    if len(s) == len(input):
        print("yield:", s)
        res.append(s)
    else:
        cursor = len(s)
        number_at_cursor = input[cursor]
        for letter in table[number_at_cursor]:
            queue.append(s + letter)

res


# %%
