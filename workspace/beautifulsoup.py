# %%
from urllib import request
from bs4 import BeautifulSoup
import re

# %%
url = "https://en.wikipedia.org/wiki/Natural_language_processing"
page = request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
soup.title

# %%
def extract_text(url):
    page = request.urlopen(url)
    soup = BeautifulSoup(page)
    lines = map(lambda x: x.text, soup.find_all("p"))
    return lines

# %%
list(extract_text(url))

# %%
links = soup.find_all("a")
links

# %%
[link.get("href") for link in links]

# %%
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)

# %%
soup.find_all(re.compile("li|ul"))

# %%
