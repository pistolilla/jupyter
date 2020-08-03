from collections import Counter, deque, OrderedDict
import heapq
from itertools import groupby, compress
import os

# %% Arbitrary Length
first, *tail = (1, 10, 7, 4, 5, 9)
tail

# %% Last N items
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)
q

# %% N Largest
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
heapq.nlargest(2, portfolio, key= lambda x: x['shares'])

# %% Ordered Dict
#d = OrderedDict()
d = {} # Starting from Python 3 all dicts are ordered, unless you delete a key
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d

# %% Zip
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

max_price = sorted(zip(prices.values(), prices.keys()), reverse=True)
max_price

# %% Remove duplicates from a sequence
def dedupe(items, applyf=None):
    seen = set()
    for item in items:
        val = item if applyf is None else applyf(item)
        if val not in seen:
            yield item
            seen.add(val)

with open(os.path.dirname(__file__) + '/../.gitignore','r') as f:
    for line in dedupe(f):
        print(line)

# %% Naming a slice
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[a]

# %% Counter
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under']
freqDist = Counter(words)
freqDist.most_common(4)

# %% Sorting a list of dictionaries
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# from operator import itemgetter
# sorted(rows, key=itemgetter('lname'))
sorted(rows, key=lambda x: x['lname'])

# %% Sorting objects
class User:
    def __init__(self, user_id:int, defensive:bool=True):
        if (defensive):
            assert type(user_id) is int # defensive programming
            assert isinstance(user_id, int) # same thing
        self.user_id = user_id
    def __repr__(self):
        return 'User<{}>'.format(self.user_id)

print(User(23))
sorted([User(1), User(3), User(4)], key=lambda x: x.user_id)

# %% Named parameters
User(2.3, defensive=False)

# %% Grouping a list of dictionaries
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows = sorted(rows, key=lambda x: x['date']) #most sort before grouping
for key, items in groupby(rows, key=lambda x: x['date']):
    print(key)
    for item in items:
        print(' ', item)

# %% Filtering sequences using generator expression

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)
pos

# %% Filtering integers
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

# %% Apply a mask in a collection
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
selectors = [n > 5 for n in counts]
print(selectors)
list(compress(addresses, selectors))

# %% Use of "any"
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
print(files)

# %% same as above (recursive)
for root, dirs, files in os.walk('.'):
    if any([name.endswith('py') for name in files]):
        print('There be python!')
    else:
        print('Sorry, no python.')
    print(files)


# %%
