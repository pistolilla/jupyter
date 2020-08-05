# %%
import re, os
import itertools

# %%
path = "C:\\Leo\\NLP\\skill-test-armorblx\\04_cluster_stories\\stories\\f1"
filename = "3gables.txt"
filepath = os.path.join(path, filename)
filepath
# %%

corpus = []
with open(filepath) as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line:
            corpus.append(line)
        line = f.readline()

corpus[:50]

# %%
corpus_clean = [line for line in corpus if re.match(r'^[a-z].*', line, flags=re.IGNORECASE)]
corpus_clean[:50]

# %%
text = " ".join(corpus_clean)
# sent tokenizing (manual)
sentences = re.split(r'[\.\?\!] *', text)
sentences[:50]

# %%
# sent tokenizing (nltk)
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(text)
sentences[:50]

# %%
# removing punctuation
sentences_clean = [re.sub(r'[^\w ]', "", text.lower()) for text in sentences]
sentences_clean = [text.strip() for text in sentences_clean]
sentences_clean[:50]

# %%
import random
samples = random.sample(sentences_clean, 10)
samples

#%% manual tokenization
tokenized = [text.split() for text in samples]
tokenized

# %%
from nltk.tokenize import word_tokenize
tokenized = [word_tokenize(text) for text in samples]
tokenized

# %%
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\S+')
tokenized = [tokenizer.tokenize(text) for text in samples]
tokenized

# %%
from nltk.corpus import stopwords
swlist = stopwords.words("english")
swlist

# %%
aca = [(i,word) for i, sent in enumerate(tokenized) for word in sent if word not in swlist]
aca

# %%
for i, items in itertools.groupby(aca, key=lambda x: x[0]):
    print(i, list(items))

# %%
for _, items in itertools.groupby(aca, key=lambda x: x[0]):
    res = [item for _, item in items]
    print(res)


# %%
