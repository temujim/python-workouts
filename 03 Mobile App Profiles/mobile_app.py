
# %%---- Import CSV files as python objects

from csv import reader as cvr

with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv") as file:
    iOS = list(cvr(file))
    iOS_header = iOS[0]
    iOS = iOS[1:]

with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/googleplaystore.csv") as file:
    android = list(cvr(file))
    android_header = android[0]
    android = android[1:]

# %% print iOS cols header
print(iOS_header)

# %%print android cols header
print(android_header)

# %%

# ---- Create function to view the data
def explore_data(data, start=0, end =5, rows_and_cols=False):
    dataslice = data[start:end]

    for row in dataslice:
        print(row)

    if rows_and_cols == True:
        print("\n------------------")
        print("Data Shape: ", end='')
        print(str(len(dataslice)) + ' x ',end='')
        print(len(dataslice[0]))
        print("------------------")

# %%
#explore_data(iOS, start=10, end = 20, rows_and_cols = True)
explore_data(iOS, rows_and_cols =True)

# %%
explore_data(android, rows_and_cols=True)


# ----------------------------------------------------------------------
# %% 2. Deleting Wrong data
# ----------------------------------------------------------------------

# Find the problematic row, confirm by checking the # of column
explore_data(android, 10472,10473, True)

# delete the row
del(android[10472:10473])

# check to see if the row is already deleted
explore_data(android, 10472,10473, True)



