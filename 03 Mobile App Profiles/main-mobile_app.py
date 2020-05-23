
# %%---- Import CSV files as python objects


# ----------------------------------------------------------------------
# %% 1. Opening and Exploring the File
# ----------------------------------------------------------------------


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
        print(str(len(data)) + ' x ',end='')
        print(len(dataslice[0]))
        print("------------------")

# %%
#explore_data(iOS, start=10, end = 20, rows_and_cols = True)
explore_data(iOS, rows_and_cols =True)

# %%
explore_data(android, rows_and_cols=True)

# ==============
# %% Col Slicer 
# ==============


def col_slicer(data, colstart=0, colend=1):

    # create list comprehensions to filter columns
    sliced = [x[colstart:colend] for x in data]

    # output the sliced data 1 per line
    for row in sliced:
        print(row)

    print("Total number of rows: " + str(len(sliced)))


print(android_header[:4])
col_slicer(android[:5], 0, 3)


# ----------------------------------------------------------------------
# %% 2. Deleting Wrong data
# ----------------------------------------------------------------------

# Find the problematic row, confirm by checking the # of column
explore_data(android, 10472,10473, True)

# delete the row
del(android[10472:10473])

# check to see if the row is already deleted
explore_data(android, 10472,10473, True)

# ----------------------------------------------------------------------
# %% 3. Removing Duplicate Entries
# ----------------------------------------------------------------------

print(android_header[:11])

# Find the list of duplicates for 'Instagram'
for app in android:
    name = app[0]

    if name == 'Instagram':
        print(app[:11])


# %% todo: Count the total number of duplicates
#         - Create 2 list:

unique_apps = []
duplicate_apps = []
dupe_count = 0
unique_count = 0

for app in android:
    name = app[0]

    if name not in unique_apps:
        unique_apps.append(name)
        unique_count += 1
    else:
        duplicate_apps.append(name)
        dupe_count += 1

print("Total number of DUPLICATED  apps: " + str(dupe_count))
print("Total number of UNIQUE apps: "+ str(unique_count))


# ********
# %% todo: Create a dictionary review_max of app names and most number of reviews

reviews_max = {}


for app in android:
    name = app[0]
    reviews = float(app[3])

    if (name not in reviews_max):
        reviews_max[name] = reviews

    elif reviews > float(reviews_max[name]):
        reviews_max[name] = reviews


# show the list of app counts 
reviews_max

# check if it shows the highest number of apps
print(reviews_max['Instagram'])

# count the number of apps
print(len(reviews_max))

print(android_header[:4])
col_slicer(android[:5], 0, 4)

# ********
# %% todo: Create new list of clean apps only
# ********

clean_apps = []
listed_apps = []


for row in android:
    name = row[0]
    reviews = float(row[3])

    if (name not in listed_apps) and (reviews_max[name]==reviews):
        listed_apps.append(name)
        clean_apps.append(row)


# %%

clean_apps[:5]

# %%

print("\n")
print("=========================")
print("---- List of Clean Apps")
print(android_header[:4])
explore_data(clean_apps, 0, 5, True)

print("\n\n\n=======================")
print("---- List of Main App list")
explore_data(android, 0, 5, True)

# len(float)

# %%

# ---
print("\n\n\n --- Show 5 Columns Only" )
print(android_header[:5])
col_slicer(clean_apps[:10], 0, 5)


# ----------------------------------------------------------------------
# %% 4. Remove Non-English Apps
# ----------------------------------------------------------------------

# clean_apps[0][0]
# print(ord('_'))

# for char in clean_apps[0][0]:
#      print(ord(char))
# 
# print(chr(126))

# ********
# %% todo: Write a function to check if there's non english characters
# ********

def non_english(appname):

    for char in appname:

        if ord(char) > 127:
            print(char)
            return False
    print(char)
    return True



# non_english('Test')

non_english('Docs To Go™ Free Office Suite')
# non_english('爱奇艺PPS -《欢乐颂2》电视剧热播')
# non_english('Instachat �')

# ********
# %% todo: Tweak the function to only flag 3 or more than non-english chars
# ********

def non_englishv2(appname):

    non_eng_count = 0

    for char in appname:
        if ord(char) > 127:
            # print(char)
            non_eng_count += 1
            # print(non_eng_count)

    # can be added within the nested if
    # but saves resources by checking th condition only once
    if non_eng_count > 3:
        # print(char)
        return False
    else:
        # print(char)
        return True


# non_english('Test')

# non_englishv2('Docs To Go™ Free Office Suite')
non_englishv2('爱奇艺PPS -《欢乐颂2》电视剧热播')
# non_englishv2('Instachat �')


# ********
# %% todo: Segregate apps between non-english and english apps
# ********


english_apps =[]
non_english_apps = []

# explore_data(clean_apps, 0, 5, True)
for app in clean_apps:
    name = app[0]

    if non_englishv2(name):
        english_apps.append(app)
    else:
        non_english_apps.append(app)


# %%
print("\n-------------------")
print("English Android Apps: {:,}".format(len(english_apps)))
print("Non-english Android Apps: {:,}".format(len(non_english_apps)))
print("Total number of apps: {:,}".format(len(english_apps)+len(non_english_apps)))

# %%

# explore_data(non_english_apps)
print("\n\n\n-- List of NonEng Apps")
print(col_slicer(non_english_apps[:10], 0, 1))
# print(len(non_english_apps))

# ********
# %% todo:  iOS English Apsp Only
# ********

iOS_english = []
iOS_non_english = []



# explore_data(clean_apps, 0, 5, True)
for app in iOS:
    name = app[1]

    if non_englishv2(name):
        iOS_english.append(app)
    else:
        iOS_non_english.append(app)


# %% Double check the filtering
print(len(iOS_english))
print(len(iOS_non_english))
print(len(iOS_english)+len(iOS_non_english))
print(len(iOS))


# ----------------------------------------------------------------------
# %% 5. Isolate Free Apps
# ----------------------------------------------------------------------

print(android_header[:8])
col_slicer(english_apps[:1], 0, 8)
# android[0][6]

# object type of the price
type(android[0][7])

# ********
# %% todo: Android Free Apps
# ********






# method filtering by price
# thisis the approach used by DQ
android_free = []
android_paid = []

for app in english_apps:
    price = app[7]

    if price == '0':
        android_free.append(app)
    else:
        android_paid.append(app)


print(len(android_free))
print(len(android_paid))
print(len(android_free)+len(android_paid))

# ~ ~ ~ ~ ~ 
# %% Extra:

# determine free app has some problematic values in free/type labeling
for app in android_free:
    apptype = app[6]

    if apptype != 'Free':
        print(app)


#android_header[6]
# *******
# %% todo: iOS Free Apps
# *******

iOS_free = []

print(iOS_header)
explore_data(iOS_english)

for app in iOS_english:
    price = app[4]

    if price == '0.0':
        iOS_free.append(app)


print(len(iOS_free))
print(len(iOS))

# ----------------------------------------------------------------------
# %% 6. Most Common Apps by Genre
# ----------------------------------------------------------------------

print(android_header)
explore_data(android)

# %%
print(iOS_header)
explore_data(iOS)

# *******
# %% todo: Method 1: Create a function freq_table
# *******


def freq_table(dataset, index):

    table = {}
    total = 0


    for app in dataset:
        col = app[index]
        total += 1

        if col in table:
            table[col] += 1
        else:
            table[col] = 1


    # convert table to percentages
    for cat in table:
        table[cat] = (table[cat]/total)*100


    # print(type(display_table))
    sorted_cat =  {k:v for k,v in sorted(table.items(), key=lambda item: item[1], reverse=True)}

    for k, v in sorted_cat.items():
        print("{}: {:.2f}%".format(k, v))

# test function to show the category count
android_cat = freq_table(android, 1)


# ********
# %% todo: Method 2: Create a display_table function
# ********

def freq_table2(dataset, index):

    table = {}
    total = 0


    for app in dataset:
        col = app[index]
        total += 1

        if col in table:
            table[col] += 1
        else:
            table[col] = 1


    # convert table to percentages
    for cat in table:
        table[cat] = (table[cat]/total)*100


    # print(type(display_table))
    return table

android_cat2 = freq_table2(android, 1)
print(android_cat2)

def display_table(dataset, index):
    table = freq_table2(dataset, index)

    # initiliaize and emply list
    sorted_tab = []

    # convert the dict to list of tuples
    for k, v in table.items():
        sorted_tab.append((v, k))

    # sort the list of tuples
    sorted_tab = sorted(sorted_tab, reverse=True)

    for i in sorted_tab:
        print("{}: {:.2f}%".format(i[1], i[0]))

print("\n\n\n")
display_table(android, 1)




# ********
# %% todo: Method 3
# ********


def pivot_count(dataset, index, percent = False, sort = False):
    """
    Default output:
        - absolute number
        - output: dictionary
    Percentage:
        - converts the output as a percentage of the total number
        - output: dictionary
    Sort:
        - Sorts the output from highest to lowest
        - output:list

    """

    tally = {}
    total_counter = 0


    for app in dataset:
        col = app[index]
        total_counter += 1


        if col not in tally:
            tally[col] = 1
        else:
            tally[col] += 1



    if percent:
        for key in tally:
            tally[key] = round((tally[key]/total_counter) * 100, 2)


    if sort:
        tally =  sorted(tally.items(), key = lambda x: x[1], reverse=True)


    return tally




# %%

# ----------------------------------------------------------------------
# %% 7. Data Analysis by Geenre for Free Mobile Apps
# ----------------------------------------------------------------------



# *******
# %% todo: `Category` and `Genres` Using freq_table
# *******

# Android Category Count
freq_table(android_free, 1)

print("\n\n\n")

# Android Genre Count
# freq_table(android_free, -4)
# android_header


# ********
# %% todo: `prime_genre`
# *******

# examine the header index
iOS_header

# prime_genre count index_table
display_table(iOS_free, -5)


# ----------------------------------------------------------------------
# %% 8. App Popularity
# ----------------------------------------------------------------------



test=freq_table(android_free, 1)

# %%
# android_header

# android[0][5].replace(',','').replace('+', '')
# android[0][5]
# ccol_slicer(android_free[100:120], 5, 6)

# TEST RUNS
android[0][1]
type(float(android[0][5].replace(',','').replace('+', '')))

# %%


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# %% TODO: Android Avg Installs Per Category
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

install_count = {}
android_appcount = {}

for app in android_free:
    cat = app[1]
    installs = app[5]

    installs = float(installs.replace(',','').replace('+', ''))

    if cat not in install_count:
        install_count[cat] = installs
        android_appcount[cat] = 1
    else:
        install_count[cat] += installs
        android_appcount[cat] += 1

# Calcuate the Average Install per Cat
avg_install_perCat = {}

for k in install_count:

    # print("{} - {}".format(k, android_appcount[k]))
    #print(android_appcount[k])


    avg_install_perCat[k] = install_count[k]/android_appcount[k]


# Sort the output
avg_installs_sorted = sorted(avg_install_perCat.items(), key = lambda x: x[1], reverse=True)

print("\n\n")

for cat in avg_installs_sorted:
    print("{} : {:,.2f}".format(cat[0], cat[1]))





# %% --- OUTPUT AVG install per cat

import pprint

pp = pprint.PrettyPrinter()
pp.pprint(avg_install_perCat)


print("\n\n")
pp.pprint(avg_installs_sorted)



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# %% TODO: iOS Avg Ratings Per Category
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# %%
# TEST RUN, explore columns for data manipulation
# print(iOS_header[0:6])
# col_slicer(iOS[20:30],5, 6)

type(iOS_free[0][5])
type(iOS_free[0][5]) == str

iOS_header[-5]


# %%

# GATHER GENRE_RATING and Category App COunt
iOS_genre_rating = {}
iOS_genre_counter = {}

for app in iOS_free:
    genre = app[-5]
    rating_total = float(app[5])


    if type(rating_total) != float:
        print(genre)

    #print("{}: {}".format(genre,rating_total))

    if genre in iOS_genre_rating:
        iOS_genre_rating[genre] += rating_total
        iOS_genre_counter[genre] += 1
    else:
        iOS_genre_rating[genre] = rating_total
        iOS_genre_counter[genre] = 1

iOS_avg_ratings_perCat = {}

# GENERATE THE AVG RATINGS PER CAT
for cat in iOS_genre_rating:

    iOS_avg_ratings_perCat[cat] = iOS_genre_rating[cat]/iOS_genre_counter[cat]

iOS_avg_ratings_catsorted =  sorted(iOS_avg_ratings_perCat.items(), key = lambda x: x[1], reverse = True)



# OUTPUT the AVG RATINGS per CATEGORY for iOS
for ent in iOS_avg_ratings_catsorted:
    print("{} : {:,.2f}".format(ent[0], ent[1]))
















