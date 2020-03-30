import re
import unicodedata

# %% Spiting with regex
line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*', line)

# %% Multiple endswith (tuple)
filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
[name for name in filenames if name.endswith(('.c', '.h'))]

# %% re match, findall
url = 'http://www.python.org'
pat = re.compile(r'https?:|ftp:')
print('match' if re.match(pat, url) else 'nop')

pat.findall("https: ftp: fttp")

# %% Searching and replacing
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text, flags=re.IGNORECASE)

# %% Multiline string and non capturing group (?:)
text2 = '''/* this is a
multiline comment */'''
comment = re.compile(r'/\*(?:.|\n)*?\*/')
comment.findall(text2)

# %%
m = re.match(comment, "no matching example")
message = "match" if m else "no match"
message

# %% Normalizing Unicode

s1 = 'Jalape\u00f1o' # one caracter
s2 = 'Jalapen\u0303o' # n + diacritic
print('{} = {} -> {}'.format(s1, s2, s1 == s2))
s1 = unicodedata.normalize('NFC', s1)
s2 = unicodedata.normalize('NFC', s2)
print('{a} = {b} -> {c}'.format(a=s1, b=s2, c=int(s1 == s2)))

# %% justifying strings
text = 'Hello World'
print(text.rjust(20,'='))
print(text.center(20,'*'))

# %% Reformatting text
import textwrap
s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, not around the eyes, don't look around the eyes, look into my eyes, you're under."
print(textwrap.fill(s, 40))

# %% html encode
s = 'Spicy Jalapeño'
s.encode('ascii', errors='xmlcharrefreplace')

# %% Tokenizing and tagging (old approach, pure regex)
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pattern.scanner('foo = 23 + 42 * 10')
[(m.lastgroup, m.group())for m in iter(scanner.match, None)]

# %%
