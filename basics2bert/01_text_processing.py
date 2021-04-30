# %%
import re
from collections.abc import Iterable
from collections import defaultdict, Counter

# %% 1 calculate the number of tweets containing the string "#pytorch"
tw_strings = ["""
I wrote a book titled "Python Data Analysis for Newbies.
for Kindle Unlimited". Please have a look if u are newbies to data analysis using Python.
https://amzn.to/2Fzbx
#Python
#Numpy
#Pandas
#Programming
""",
"""
I'm going to start the hottest #deeplearning library called #pytorch tutorial
from today.
I'll write the pytorch tips here for the reminder.
First, let's import torch.
This is as easy as importing tensorflow/chainer/caffe2.
""",
"""
In my #colab environment, torch version was 1.6.0.
""",
"""
I'm going to start the hottest #deeplearning library called #pytorch tutorial
from today.
I'll write the pytorch tips here for the reminder.
Second, let's output the version of torch.
This is as easy as tensorflow/numpy.
---
torch.__version__
---
""",
"""
Check if the cuda is available.
#GPU is successfully activated in my #Colab environment.
I used to be a #keras user, but now changing to #pytorch as I need to use
#huggingface for for my work.
That's it for the first day using #pytroch.
Thanks for watching.
"""]

def how_many(needle:list, key:str):
    return len([x for x in needle if key in x])

print(how_many(tw_strings, "#pytorch"))

# %% 2. Output the number of characters in each of my five tweets in order
def count_chars(listx:list):
    return [len(x) for x in listx]

count_chars(tw_strings)
# %% store only the string following the "hashtag(#)" in the list, and return it to us. Duplicate strings of the same string should be deleted and stored in the order of appearance of the original tweet (index order of the list).

def hashtags(listx:list):
    hashes = {}
    for t in listx:
        for x in re.findall(r"#(\S+)\b", t):
            hashes.update({x:True})
    return hashes.keys()

def hashtags(listx:list):
    hashes = {x.lower() for t in listx for x in re.findall(r"#(\S+)\b", t)}
    return hashes

hashtags(tw_strings)
# %% 6. Create a function that creates a bi-gram from the given sequence (string, list, etc.). Then use this function to take the first tweet out of the five tweets, get the character bi-gram, and display it in list form where the tuple is an element.

def bigrams(x:Iterable):
    return zip(x[:-1], x[1:])

list(bigrams(tw_strings[0]))

# %% 7. Extend the function in 06. by defining a function that returns an n-gram when you give a string and n(n in n-gram) as arguments, and display the string "I want the new corona vaccine quickly."

def ngrams(A:Iterable, n:int):
    for i in range(len(A) - n + 1):
        yield(tuple(A[i: i + n]))

sent = "I want the new corona vaccine quickly."
list(ngrams(sent.split(), 3))
# %% 8. display the top 10 trigrams and their frequency in descending order

remove_symbols = ['\n', '.', '=', '#', '(', ')', '-', '/', ':', '?', ' 、', ' 「', ' 」', '_', '!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def ngrams_clean(A:sent, n:int):
    A = "".join([a.lower() for a in A if not a in remove_symbols]).split()
    return ngrams(A, n)

ngramslist = defaultdict(int)
for tweet in tw_strings:
    for ngrm in ngrams_clean(tweet, 3):
        ngramslist[ngrm] += 1

#res = [(key, value) for key, value in ngramslist.items()]
sorted(list(ngramslist.items()), key=lambda x:x[1], reverse=True)[:10]
# %% using counter

ngramslist = [ngrm for tweet in tw_strings for ngrm in ngrams_clean(tweet, 5)]
counter = Counter(ngramslist)
counter.most_common(10)

# %% 9. Find the set of 8-grams contained in "I want to connect with a fledgling engineer" and "I want to connect with a full-stack engineer" as s1 and s2, respectively. Then, find the union, product, and difference sets of s1 and s2.

sent1 = "I want to connect with a fledgling engineer"
sent2 = "I want to connect with a full-stack engineer"

def ngrams_set(sent, n):
    for i in range(len(sent) - n + 1):
        yield sent[i:i + n]

s1 = set(ngrams_set(sent1, 8))
s2 = set(ngrams_set(sent2, 8))

#s1 | s2
#s1 & s2
s1 - s2



# %%
