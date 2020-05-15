
# import csv

# with open('~/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csvl', newline='') as csvfile:

# ----------------------------------------------------------------------
# %% 1. Read text files
# ----------------------------------------------------------------------
filename = "/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv"
file = open(filename, mode='r')
print(file.read())
file.close()


# ----------------------------------------------------------------------
# %% 2. Read first 3 lines of a flat file
# ----------------------------------------------------------------------


filename = "/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv"
file = open(filename, mode='r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


# ----------------------------------------------------------------------
# %% 3. Using context managers to read the first 5 lines
# ----------------------------------------------------------------------

with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv", newline='') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())

# ----------------------------------------------------------------------
# %% 4. Read files using using file open, file close
# ----------------------------------------------------------------------
import csv

file = open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv")
csv_file = csv.reader(file)

print(next(csv_file))
print(next(csv_file))
print(next(csv_file))

file.close




# ----------------------------------------------------------------------
# %% 5. Using CSV reader fileopen close, read flat file and print all lines
# ----------------------------------------------------------------------

# import reader module only
from csv import reader

# open file
file = open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv")

# convert file to a csv reader object
csvfile = reader(file)

# convert reader object to list so it can be easily readable
list_csvfile = list(csvfile)

# print list
print(list_csvfile)

# ----------------------------------------------------------------------
# %% 6. Read files using CSV Readers and context Managers
# ----------------------------------------------------------------------

from csv import reader as cvr

with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv") as f:
    read_csv = list(cvr(f))
    for row in read_csv[:5]:
        print(row)

print(len(read_csv))



