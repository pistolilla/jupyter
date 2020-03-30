test = "I don't know the answer"

def getBigrams(sent, lefttoright=True):
    # tokenizing
    tokens = test.split()
    if not lefttoright:
        tokens = reversed(tokens)
    # get bigrams
    for i,token in enumerate(tokens):
        if i+1 < len(tokens):
            yield (tokens[i], tokens[i+1])

bigrams = [for bigram in getBigrams(test)]
bigramsRL = [for bigram in getBigrams(test, False)]

zip(bigrams, bigramsRL)
zip(unigram, nextunigram)