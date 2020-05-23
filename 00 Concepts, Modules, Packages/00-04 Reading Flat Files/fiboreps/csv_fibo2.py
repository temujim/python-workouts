# import csv 

# %% 1. Read text files using python built-in functions

file = open("/home/barca/Python_Workouts/00 Concepts, Modules, Packages/00-00 datasets/brics.csv")
print(file.read())
file.close()

# %% Read text for each line and read first 3 lines

file = open("/home/barca/Python_Workouts/00 Concepts, Modules, Packages/00-00 datasets/brics.csv", newline='')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# %% 3 Read text files using context managers (read first 5 lines)

with open("/home/barca/Python_Workouts/00 Concepts, Modules, Packages/00-00 datasets/brics.csv", newline='\n') as f:
    print(f.readline())
    print(f.readline())


# %% 4. Using CSV Reader file oen close, read flat files and read 3 lines

import csv


file = open("/home/barca/Python_Workouts/00 Concepts, Modules, Packages/00-00 datasets/brics.csv")
csv_read = csv.reader(file)
print(next(csv_read))
print(next(csv_read))
print(next(csv_read))
print(type(next(csv_read)))
file.close

# %% Using CSV Reader file open close, read flat file and print all lines

from csv import reader

file = open("/home/barca/Python_Workouts/00 Concepts, Modules, Packages/00-00 datasets/brics.csv")
csv_list = list(reader(file))
# print(csv_list)

for line in csv_list:
    print(line)

file.close()

# %% 6. Using CSV Reader and with context managers, read line 10-20 Import readeronly with alias "cvr"


from csv import reader as cvr

with open("/home/barca/Python_Workouts/04 Android App Store Analysis/datasets/apps.csv") as f:
    csv_list = list(cvr(f))

    for line in csv_list[0:11]:
        print(line)


