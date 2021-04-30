# %%
import os
import pandas as pd

# %% creating files

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
group_pinfo = [
    {
        "ID" : 1,
        "Name" : "Cage",
        "Age" : "23",
        "Sex" : "Male"
    },
    {
        "ID" : 2,
        "Name" : "Alexa",
        "Age" : "21",
        "Sex" : "Female"
    },
    {
        "ID" : 3,
        "Name" : "Cart",
        "Age" : "53",
        "Sex" : "Male"
    },
    {
        "ID" : 4,
        "Name" : "Zoey",
        "Age" : "48",
        "Sex" : "Female"
    },
    {
        "ID" : 5,
        "Name" : "Bigbird",
        "Age" : "28",
        "Sex" : "Male"
    }
]
group_binfo = [
    {
        "ID" : 1,
        "Role" : "Leader",
        "Hobby" : "Twitter",
    },
    {
        "ID" : 2,
        "Role" : "Vocal",
        "Hobby" : "walking",
    },
    {
        "ID" : 3,
        "Role" : "Base",
        "Hobby" : "Photo"
    },
    {
        "ID" : 4,
        "Role" : "Guitar",
        "Hobby" : "Mechanics"
    },
    {
        "ID" : 5,
        "Role" : "Guitar",
        "Hobby" : "Flying"
    },
    {
        "ID" : 6,
        "Role" : "Pandero",
        "Hobby" : "nothing"
    }
]

df1 = pd.DataFrame(group_pinfo)
df2 = pd.DataFrame(group_binfo)
df1.head(3)

# %%
df1.to_csv(os.path.join(THIS_DIR, 'group_pinfo.csv'), index=None)
df2.to_csv(os.path.join(THIS_DIR, 'group_binfo.csv'), index=None)

# %%

# %% 10. Output N lines from the beginning
df1.head(4)

# %% 11. Number of records
len(df1)

# %% 12: Combine two files (inner join) by using ID (first column) as a key

joined = pd.merge(df1, df2, on="ID")
joined

# %% 13: Convert commas to spaces.
df1.to_csv(sep=" ", index=False)

# %% 14: Column Extraction. Save the "group_pinfo.csv" with only the name column extracted from each line as col1.txt
df1[["Name"]].to_csv()

# %% 15: Insert the following record between the lines of ID=1 and ID=2 in "group_pbinfo.csv":
# %% 6, Toshi, 54, Male, Vocal, Cooking
dftmp = pd.DataFrame([[6,"Toshi",54,"Male","Vocal","Cooking"]], columns=joined.columns)
pd.concat([joined, dftmp], axis='columns')

# %% 16: Split the file in two.
middle_point = len(df1) // 2
print(df1[:middle_point])
print(df1[middle_point:])

# %% 17: Find the type of string (set of different strings) in the "role" column
list(df2["Role"].unique())
# %% 19. Find the frequency of occurrence of elements in a particular column and arrange them in order of frequency of occurrence
df2["Role"].value_counts()

# %% 18. Output the result of sorting only the record rows except the header row of "group_pinfo.csv" into the descending order of numbers in the [age] column
# Please display all rows of the output.
df1.sort_values(by=["Age"], ascending=[False])

