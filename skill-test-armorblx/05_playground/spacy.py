# %% 
import os, random
import spacy
# %%
path = "C:\\Leo\\NLP\\skill-test-armorblx\\04_cluster_stories\\stories\\f1"
filename = "gables_forLM.txt"
filepath = os.path.join(path, filename)
filepath

# %%
with open(filepath) as f:
    lines = f.readlines()

# %%
samples = random.sample(lines, 10)
samples

# %%
nlp = spacy.load("en")

# %%
doc = nlp(samples[0])
doc

[token.lemma_ for token in doc]
# %%
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])
# %%
