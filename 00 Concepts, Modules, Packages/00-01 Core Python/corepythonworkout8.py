## 1. Create a script that will sum any numbers of integers

def sum_all(*args):
    sum = 0

    for i in args:
        sum += i

    return sum 


## 2. Write a fibo sequence up to 20 that starts with zero

a, b = 0, 1

for i in range(20):

    print("{} - {}".format(i+1, a))

    a, b = b, a + b

## 3. Create a fibo script that accepts the user input on how mny 
##      items to do and then returns a fibo digiti.

def fibo(n):

    a, b = 0, 1

    for i in range(n-1):

        a, b = b, a+b

    return a

## 4. Create a script that creates a function to extract the root of a number 

def create_root(n):

    def actual_root(x):
        root = x**(1/n)
        return root

    return actual_root

square_root = create_root(2)
cube_root = create_root(3)

## 5. Return the mean of all numbers numbers in a tuple

def get_mean(*args):
    sum = 0

    for i in args:
        sum += i

    return sum/len(args)

## 6. Create a function that returns the largest and smallest n-elements in any list

def sorter(numlist, largest=True, n=2):

    return sorted(numlist, reverse=largest)[:n]

nlist = [1, 2, 3, 5, 5, 6, 19, 97, 42, 53]

## 7. Return a dictionary of count and Tally the values in list

days = ['sat', 'sat', 'sun', 'mon', 'tues', 'thurs', 'tues', 'sat']

dict_count = {}

for i in days:
    if i in dict_count:
        dict_count[i] += 1
    else:
        dict_count[i] = 1

print(dict_count)

## 8. Loop through the value of previous exercises

for k, v in dict_count.items():
    print("There are about {} occurrence on {}".format(v, k))


## 9. Show an example of kwargs loops.

def kwarloop(**kwargs):

    for k, v in kwargs.items():
        print("There are about {} occurences on {}".format(v, k))


# kwarloop('Mon' = 2, 'Tues' = 3)
kwarloop(Mon=2, Tues=3)

## 

## 10. Add zeros to make it consistent in length

def constring(numstr):
    updated_string = numstr + '0'

    def add_zeros():
        nonlocal updated_string
        updated_string += '0'

    while len(updated_string) <= 6:
        add_zeros()

    return updated_string

## 11. Provide Error Hanlding of the Add Zeros'

def constring(numstr):
    try:
        updated_string = numstr + '0'
    
        def add_zeros():
            nonlocal updated_string
            updated_string += '0'
    
        while len(updated_string) <= 6:
            add_zeros()
    
        return updated_string
    except TypeError:
        return 'Value should be a string'



## 12. Create a function that takes two list as a function 

def maxsum(x, y):
    return max(x) + max(y)

nlist = [1, 2, 3, 5, 5, 6, 19, 97, 42, 53]
nlist2 = [2, 5, 6, 7, 78, 1, 4]

## 13.  Create a function to convert yards to inches

def ydconverter(ydval, inFeet = True):
    if inFeet==True:
        newval = ydval*3
    else:
        newval = ydval*26

    return newval


## 14. Plot the cubes an dsquares up to 10 

import matplotlib.pyplot as plt

num = list(range(0, 10))
squared = [i**2 for i in num]
cubed = [i**3 for i in num]

plt.scatter(num, squared, c='blue', edgecolors='white', s=20)
plt.scatter(num, cubed, c='red', edgecolors='black')
#plt.style.use('classic')
plt.style.use('bmh')
plt.axis([0, 11, 0, 1100])
plt.show()

## 15. Convert Celsius to Fahrenheit

temp = 40

def CtoF(x):
    global temp
    temp = (x*(9/5)) + 32

    return temp

print(CtoF(temp))
print("\n---- new Value ----")
print(temp)


## 16. Return a list with first 2 elements capitalized

fruits = ['orange', 'grape', 'kiwi', 'apple', 'mango', 'fig', 'lemon']

def caps(li):

    def inner(w):
#        nonlocal w
        return w.upper()
#        w.upper()

    return [inner(li[0]), inner(li[1])]

caps(fruits)

## 17. Capitalize the following using different methods

## loop

fruitloop = []

for i in fruits:
    fruitloop.append(i.upper())

print(fruitloop)


## lambda

fruitmap = map(lambda x: x.upper(), fruits)
print(list(fruitmap))

## comprehensions

fruitcomp = [i.upper() for i in fruits]
print(fruitcomp)




##






## 
