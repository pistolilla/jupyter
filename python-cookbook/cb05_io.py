import os

# %%
with open('large_files/test.txt', 'xt') as f:
    print("hello", file= f)

# %% Pathnames
# Get the path of the folder
path = 'C:\\Users\\usuario\\Anaconda3\\jupyter\\untitled'
print(path)
path = os.path.dirname(__file__)
print(path)

# %%
# Get the last component of the path
os.path.basename(__file__)

# %%
# Join path components together
os.path.join(os.path.dirname(__file__), 'newfolder', 'newfile.txt')

# %%
# Split the file extension
os.path.splitext(os.path.abspath(__file__))

# %% Existence of a File
os.path.exists(os.path.dirname(__file__) + '/../large_files')

# %% Get size
os.path.getsize(os.path.dirname(__file__) + '/cb02_strings.py')


# %% Get all regular files
[name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]

# %% Find (like bash)
import glob
pyfiles = glob.glob((os.path.dirname(__file__) + '/*.py'))
pyfiles

# %% Temporary file
import tempfile
with tempfile.TemporaryFile('wt+') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')
    # Seek back to beginning and read the data
    f.seek(0)
    print(f.read())

# %% Serializing object
import pickle
myObject = {"asdf":0}
f = open("myObject.pickle", "wb")
pickle.dump(myObject, f)
f.close() # important to close

# %%
