# Redading text file using python builtin fucntions

file = open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv", mode='r')
print(file.read())
file.close()


# ----------------------------------------------------------------------
# %% 2. Print the first 3 lines
# ----------------------------------------------------------------------

file = open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv", mode='r', newline='')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


# ----------------------------------------------------------------------
# %% 3. Read line the line using content managers
# ----------------------------------------------------------------------

with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv") as f:
    print(f.readline())
    print(f.readline())



# ----------------------------------------------------------------------
# %% 4. Using CSV reader fileopen close, read 3 lines
# ----------------------------------------------------------------------

import csv

file = open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv")
csvfile = csv.reader(file)
print(next(csvfile))
print(next(csvfile))
print(next(csvfile))
file.close()


# ----------------------------------------------------------------------
# %% 5. Using CSV reader file open close, read flat file only
# ----------------------------------------------------------------------

from csv import reader


file = open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv")
csvfile = list(reader(file))
print(csvfile)
file.close()

# ----------------------------------------------------------------------
# %% 6. using CSV reaer and with context managers, read line 10-20
# ----------------------------------------------------------------------

from csv import reader as cvr

with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv") as file:
     newfile = list(cvr(file))

     for line in newfile[10:20]:
         print(line)

