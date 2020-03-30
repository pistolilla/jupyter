import json
from urllib import request
from xml.etree import ElementTree
import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt

# %% JSON Data
data = {
    'name' : 'ACME',
    'shares' : None,
    'price' : True
}
json.dumps(data)

# %% Parsing Simple XML Data
# Download the RSS feed and parse it
xml = request.urlopen('http://planet.python.org/rss20.xml')
doc = ElementTree.parse(xml)
# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    print(item.findtext('title'))
    print(item.findtext('pubDate'))
    print()

# %% Interacting with a Relational Database
db = 'large_files/test.db'
conn = sqlite3.connect(db)
conn.execute('CREATE TABLE IF NOT EXISTS portfolio (symbol TEXT, shares INTEGER, price REAL)')

# %%
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
c = conn.cursor()
c.executemany('INSERT INTO portfolio VALUES (?,?,?)', stocks)
conn.commit()

# %%
for row in conn.execute('SELECT * FROM portfolio'):
    print(row)
conn.close()

# %%
csvfile = os.path.dirname(__file__) + '/../large_files/rodent_baiting/rats.csv'
rats = pd.read_csv(csvfile)
# rats[0:5]
rats.head(5)

# %%
rats['Current Activity'].unique()

# %%
selector = rats['Current Activity'] == 'Dispatch Crew'
selector.head()

# %%
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
crew_dispatched.head()

# %%
dates = crew_dispatched.groupby('Completion Date')
dates_size = dates.size()
dates_size

##### Mi cosecha
# %%
rats[["Status"]].head()

# %%
vc = rats["Wards"].value_counts()
dict(vc.head())

# %%
vc = rats["Wards"].value_counts(normalize=True)
sum([x for x in dict(vc).values()])

# %%
foo = rats.sort_values(by=["Number of Premises with Garbage", "Number of Premises Baited"], ascending=[False, True])
foo.head()

# %%
foo = rats.nlargest(n=5, columns = ["Number of Premises with Rats"])
foo

# %% Plots
foo = rats.iloc[0:50]
foo[["Number of Premises with Garbage"]].plot(figsize=(9,7))

# %%
foo[["Number of Premises with Garbage", "Number of Premises with Rats"]].plot(figsize=(9,7))

# %%
foo[["Number of Premises with Rats"]].plot(figsize=(9,7), kind='hist', bins=10)

# %% Group By
gbo = rats.groupby("Most Recent Action")
gbo

# %%
gbo.groups

# %%
gbo.mean()

# %%
gbo[["ZIP Code"]].mean()

# %%
rats.groupby("Most Recent Action")[["Number of Premises with Garbage"]].sum()

# %%
rats.groupby("Most Recent Action")[["Number of Premises with Garbage"]].agg(["sum", "mean", "count"])

# %%
rats.groupby(["Type of Service Request", "Most Recent Action"])[["Number of Premises with Garbage"]].sum()

# %%
