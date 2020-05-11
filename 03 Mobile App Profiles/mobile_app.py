import csv

# with open('~/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csvl', newline='') as csvfile:

filename = "/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv"
file = open(filename, mode='r', encoding='utf8')
print("\nShow file here")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print("\n - END -")
file.close()


