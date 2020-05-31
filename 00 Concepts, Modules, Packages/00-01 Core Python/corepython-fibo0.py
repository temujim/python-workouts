# %% 1. Createa a script that will sum any number of integers included in a tuple

def sum_all(*args):

    sum = 0

    for i in args:
        sum += i

    return sum


sum_all(1,2, 5)



# %% 2. Write a fibo sequence up to 20 that starts with zero


a, b = 0, 1


for i in range(21):
    print("{} - {}".format(i, a))
    a, b = b, a+b


# %% 3. Create a fibo fucntion that accepts user input on how many items to do 

def fibo(n):

    a, b = 0, 1

    for i in range(n-1):
        a, b = b, a+b

    return b

fibo(20)


# %% 4. Create a script that creates a function to extract the root a number


def make_root(n):

    def actual_root(x):

        root = x**(1/n)

        return round(root)

    return actual_root


square_root = make_root(2)
cube_root = make_root(3)

# square_root(64)
cube_root(64)

# %% 5. Return the mean of all numbers in a tuple


def get_mean(*args):

    sum = 0

    for i in args:

        sum += i

    return sum/len(args)


get_mean(1, 2, 45, 56)
get_mean(1,2,3,4,5,6,7,8,9,10)


# %% 6. Create a function that return the largest and smallest n-elements in any list

def sorter(nlist, reverse=True, n=2):

    return sorted(nlist, reverse=reverse)[:n]

num1 = [1,2, 5, 6, 7, 87, 2]

sorter(num1)

# %% 7. Return a dictionary of count and Tally the values in list

y = ['sat', 'fri', 'fri', 'sat', 'sat', 'tues', 'wed', 'mon', 'sat', 'tues']

dict_count = {}


for i in y:
    
    if i in dict_count:
        dict_count[i] += 1
    else:
        dict_count[i] = 1

print(dict_count)


# %% 8. Loop through the previous exercise

for k, v in dict_count.items():

    print("On {}, there are about {} number of occurrence/s.".format(k, v))


# %% 9. Show an example of kwargs_loops - Use the "print format"method


def kwarloop(**kwargs):

    for k, v in kwargs.items():
        print("On {}, there are about {} number of occurrence/s.".format(k, v))

kwarloop(**dict_count)
#kwarloop(Mon = 2, Tues = 3, Weds=1)


# %% 10. Add zeros to make it consistent in length.

def constring(numstr):
    updated_string = numstr


    def add_zeros():
        nonlocal updated_string
        updated_string += '0'

    while len(updated_string) < 6:
        add_zeros()

    return updated_string

constring('1.2')
# constring('1245.2')

# %% 10.2 Implement using format method
def constring_f(numstr):

    updated_string = "{:0<6}".format(numstr)


    return updated_string

print(constring_f('1.2'))
print(constring('1.3'))



# %% 11. Provided Error handling of # 10


def constring2(numstr):

    try:
        updated_string = numstr
    
    
        def add_zeros():
            nonlocal updated_string
            updated_string += '0'
    
        while len(updated_string) < 6:
            add_zeros()

        return updated_string


    except TypeError:
        return 'Value should be instring'


constring2(1.2)


# %% 12. Create a function that takes two lists x and y and returns the sum of their max elemnets

def max_sum(x, y):

    return max(x) + max(y)

n1 = [1,2,5,7, 6, 12, 5]
n2 = [20, 21, 23, 5, 6, 23]


max_sum(n1, n2)



# %% 13. Create a function to convert yards to inches or feet

def ydconverter(ydval, inFeet=True):

    if inFeet==True:
        newval = ydval*3
    else:
        newval = ydval*36

    return newval

ydconverter(3, False)


# %% 14. Plot the cubes and squares up to 10 

import matplotlib.pyplot as plt
# print(plt.style.available)
plt.style.use('seaborn-darkgrid')

nums = list(range(0, 11))
squares = [i**2 for i in nums]
cubes = [i**3 for i in nums]
# print(squares)
# print(cubes)
plt.axis([0,11, 0, 1100])
plt.scatter(nums, squares,c='blue', s=20, edgecolors=None)
plt.scatter(nums, cubes, c='red', edgecolors='black')

plt.show()


# %% 15. COnvert Celsius to Fahrenheit

temp = 40

def CtoF(x):

    global temp
    temp = (x*(9/5))+32

    return temp

CtoF(temp)


# %% 16. Return a list with first 2 elements capitalized
fruits=['orange', 'grape', 'kiwi', 'apple', 'mango', 'fig', 'lemon']   


def caps2(x):

    def inner_caps(w):
        return w.capitalize()

    return [inner_caps(x[0]), inner_caps(x[1])]

caps2(fruits)


# %% 17. Capitalize the following using different methods

fruit_for = []

for fruit in fruits:
    fruit_for.append(fruit.upper())

print(fruit_for)

# %% via Lambda

lambda_for = map(lambda x: x.upper(), fruits)
print(list(lambda_for))


# %% % via Comprehensions

upper_comp = [fruit.upper() for fruit in fruits]
print(upper_comp)
