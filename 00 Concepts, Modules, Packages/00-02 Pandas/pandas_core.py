# import pandas fiboworkout 8
# Planned date: 5/5, executed 5/9

# %%
import pandas as pd

# ********
# %% todo: Adding new column in dataframe
# ********

# %% import data to pandas

brix_df = pd.read_csv("/home/barca/Python_Workouts/00 Concepts, Modules, Packages/00-00 datasets/brics.csv", index_col = 0)
brix_df

# print("test")

# ********
# %% todo: A-ii. Do a for loop of the index and Country, Capital Values
# ********


for index, col in brix_df.iterrows():

    print("{} - {}, {}".format(index, col['country'], col['capital']))

# ********
# %% todo: A-iii.  Do a for loop to upper the country values
# ********

for index, col in brix_df.iterrows():
    print(col['country'].upper())

# ********
# %% todo A-iv. Show the value of capital to BR index
# ********

brix_df



# %% pull the 'Brasilia'

brix_df['capital']['BR']


# - - - -
# %% todo: Pull out the data as a series
# - - - -
print(brix_df.loc['BR',['capital']])
type(brix_df.loc['BR',['capital']])


# - - - -
# %% todo: Pull out 'Brasilia' as a dataframe
# - - - -
print(brix_df.loc[['BR'], ['capital']])
type(brix_df.loc[['BR'], ['capital']])


# ********
# %% todo: v.  Get the value of the capital columns
# ********

# - - - -
# %% todo: 1st approach
brix_df['capital']


# - - - -
# %% todo: 2nd approach
brix_df.loc[:, 'capital']

# - - - -
# %% todo: 3rd approach
brix_df.iloc[:, 0]

#
# ********
# %% todo: vi.  putll out the BR rows
# ********

brix_df

# - - - -
# %% todo: approach 1
brix_df.loc[:]['BR']
'''
This is not possible direct df slicing is like a dictionary.
This will be explain in-depth under #2 sample

'''


# - - - -
# %% todo: approach 2

brix_df.loc['BR']

# - - - -
# %% todo: appraoch 3
brix_df.iloc[0]

# %%

# ********
# %% todo: vii.  Add a colum with all the letter of countery capitalized using for loop
# ********

for row, col in brix_df.iterrows():
    brix_df.loc[row, 'COUNTRY'] = col['country'].upper()

print(brix_df)


# ********
# %% todo: A. APPLY DATAFRAME
# ********


# %% todo: capitalize all letters under capital

brix_df['CAPITAL'] = brix_df['capital'].str.upper()
print(brix_df)

 
# %% todo: count the characters of capital and add a new column
# modify the display of dataframe
# pd.set_option('display.max_colwidth', 15)
pd.set_option('display.max_columns', 0)
# pd.set_option('display.large_repr', 0)

brix_df['lenCap'] = brix_df['capital'].apply(lambda x: len(x))
brix_df





# ----------------------------------------------------------------------
# %% 2. CREATE A DATAFRAME
# ----------------------------------------------------------------------

# ********
# %% todo: i. Create a 3x3 dictionary
# ********

# dictionary of list
d = {'col1': [1, 2, 3],
     'col2': [4, 5, 6],
     'col3': [7, 8, 9]}

print(d)


# - - - -
# %% todo: i-a Query col
# - - - -

d['col3']

# %%

d['col1']


# - - - -
# %% todo: i-a Query col
# - - - -

d['col3'][1]


# *******
# %% todo:  ii Create a dataframe    
# *******


df_d = pd.DataFrame(d)
df_d

# - - - -
# %% todo: ii-a Query col3
# - - - -


df_d['col3']

# - - - -
# %% todo: ii-b Query '5
# - - - -

df_d['col3'][1]


# *******
# %% todo:  ii Update the index names
# *******

df_d.index = ['row1', 'row2', 'row3']

#  show the updated dataframe
df_d

# - - - -
# %% todo: ii-a. Pull out number 5 using col and index names
# - - - -

df_d['col3']['row2']

# %% ii-b: pull out rows using a pandas method,  col names
df_d.loc['row2']['col3']

'''
note that in label or location-based indexing, the ROW is the first callable and not the COLUMN:
    Which is unlike the dictionary and pure dataframe calling method, which calls the column first

in Summary:
    Label and Location-based indexing: ROW x COL    hence: df.loc[row][col]
    DF and Dictionary Indexing:        COl x ROW    hence: df[col][row]
'''

# %% iii-c: pull value using col names version using location-based indexing method
df_d.iloc[1][2]


# *******
# %% todo:  iii. Understanding DataTypes
# *******

# - - - -
# %% todo: iii-a Single dataype
# print(df_d.iloc[1][2])
print(df_d.iloc[1,2])
type(df_d.iloc[1][2])



# - - - -
# %% todo: iii-b series
print(df_d.iloc[2])
type(df_d.iloc[2])



# - - - -
# %% todo: iii-c dataframe
df_d.iloc[:, [0,2]]

# %%

#df_d.iloc[[0,1], [1,2]]
df_d.iloc[0:2, 1:3]
type(df_d.iloc[0:2, 1:3])

# %% grab row1 & row, and col1 and col3
df_d.iloc[[0, 2], [0, 2]]

# %% grab row1 & row2, and col1 and col3

df_d.iloc[:2, [0, 2]]




# - - - -
# %% todo: use label-based slcing for the first 2 samples
# - - - -

df_d.loc[['row1', 'row3'], ['col1', 'col3']]


# %%
df_d.loc[:'row2', ['col1', 'col3']]
