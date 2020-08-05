import os
import pandas as pd
from sklearn import feature_extraction
from nltk import word_tokenize, WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

# %%
filename = "C:\\Leo\\NLP\\skill-test-armorblx\\03_tfidf_score\\jones_t_mails.csv"
df = pd.read_csv(filename)
df.head()
df = df.dropna()
df

# %%
X = df["content"]
X
# %%
stemmer = SnowballStemmer("english")

# %%
def lemmatizeme(text):
    words = word_tokenize(text)
    lemmatized = [stemmer.stem(word) for word in words]
    return lemmatized

def lemmatizeme(text):
    return text.split()

# %%
lemmatizeme("concern concerned concerning")
X = [" ".join(lemmatizeme(x)) for x in X]
X

# %%
#Vectorizer = feature_extraction.text.TfidfVectorizer(stop_words='english', min_df=2, ngram_range=(1,1), tokenizer=lemmatizeme)
CountVectorizer = feature_extraction.text.CountVectorizer(stop_words='english', tokenizer=lemmatizeme)
counted = CountVectorizer.fit_transform(X)

#%%
TfidfTransformer = feature_extraction.text.TfidfTransformer()
vectorized = TfidfTransformer.fit_transform(counted)

#%
# create dictionary to find a tfidf word each word
word2tfidf = dict(zip(CountVectorizer.get_feature_names(), TfidfTransformer.idf_))

for word, score in word2tfidf.items():
    print(word, score)


# %%
