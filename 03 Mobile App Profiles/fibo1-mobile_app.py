

# ----------------------------------------------------------------------
# %% 1. Opening and Exploring the files
# ----------------------------------------------------------------------

from csv import reader as cvr

# %% android data
with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/googleplaystore.csv") as android_f:
    android_f_list = list(cvr(android_f))
    android_header = android_f_list[0]
    android = android_f_list[1:]

print(android_header)
print(android[:10])

# %% ios data
with open("/home/barca/Python_Workouts/03 Mobile App Profiles/datasets/AppleStore.csv") as ios_f:
    ios_f_list = list(cvr(ios_f))
    ios_header = ios_f_list[0]
    ios = ios_f_list[1:]

print(ios_header)
print(ios)


# %% todo: Create a function to read the files


def explore_data(data, start = 0, end = 5, rows_and_cols = True):

    sliced_data = data[start:end]
    nrow = len(data)
    ncol = len(sliced_data[0])

    for row in sliced_data:
        print(row)

    if rows_and_cols == True:
        print("{} x {}".format(nrow, ncol))


explore_data(android, 10, 15, True )

# %% todo: col slicer

def col_slicer(data, colstart=0, colend = 6, rows_and_cols = True):

    for line in data:
        print(line[colstart:colend])


print(android_header[:6])
col_slicer(android[:10])



# ----------------------------------------------------------------------
# %% 2. Check What Row is problematic
# ----------------------------------------------------------------------

i = 0
problematic_rows = []
deleted_rows = []
for line in android:
    i += 1
    if len(line) != len(android_header):
        problematic_rows.append(i-1)
        deleted_rows.append(line)
        android.remove(line)

    
print(problematic_rows)


# %% proint problematic row
explore_data(android, 10472, 10475)

# %% 
explore_data(android, 10473, 10474)

# %%
print(deleted_rows)

# %% 
explore_data(android)


# %% ios error checking

i = 0
problematic_rows_ios = []
deleted_rows_ios = []
for line in ios:
    i += 1
    if len(line) != len(ios_header):
        problematic_rows_ios.append(i-1)
        deleted_rows_ios.append(line)
        ios.remove(line)


print(problematic_rows_ios)
print(deleted_rows_ios)


# ----------------------------------------------------------------------
# %% 3. Removing the Duplicate Entries
# ----------------------------------------------------------------------

# *******
# %% todo: find list of duplicates of 'Instagram'
# *******
print(android_header)
i = -1

for app in android:
    i += 1

    if app[0] == 'Box':
        print("{} - {}".format(i, app))

# %%
explore_data(android, 2545, 2546)

# %%
explore_data(android, 2604, 2605)


# %%
android_header

# *******
# %% todo: count the total number of duplicates and print the list of duplicated apps
# *******

unique_apps = []
duplicated_apps = []
n_dupes = 0

for app in android:
    name = app[0]

    if name in unique_apps:
        duplicated_apps.append(name)
        n_dupes += 1
    else:
        unique_apps.append(name)


# %%
print(n_dupes)
print(len(unique_apps))
print(duplicated_apps[200:210])


# *******
# %% todo: Create a list of review_max
# *******


reviews_max = {}
i = 0
e = 0
android_clean =[]

for app in android:
    name = app[0]
    #reviews = int(app[3].replace('+','').replace(',', ''))
    reviews = int(app[3])


    if name in reviews_max and reviews_max[name] < reviews:
        reviews_max[name] = reviews
    elif name not in reviews_max:
        reviews_max[name] = reviews




# %%
col_slicer(android[0:10], 3, 4)

# %%
type(int(android[0][3].replace('+','').replace(',', '')))


# %%
type(int(android[0][3]))
android_header

# %%
reviews_max

# %%
print("{:,}".format(int(reviews_max['Instagram'])))

# %%
reviews_max['Instagram']


# %%
len(android)


# %%
len(reviews_max)

# *******
# %% todo: android_clean
# *******

android_clean = []
android_added = []


for app in android:
    name = app[0]
    reviews = int(app[3]) 

    if name not in android_added and reviews==reviews_max[name]:
        android_added.append(name)
        android_clean.append(app)

len(android_clean)

# %%
type(android[0][3])


# ----------------------------------------------------------------------
# %% 4. Remove Non-English Apps
# ----------------------------------------------------------------------


# built-in python method to determine string representation
ord("q")


def is_english(appname):

    for char in appname:
        if ord(char) > 127:
            print(char)
            return False
            break

    print(char)
    return True
            
# %%

is_english("Test")

# %%



is_english("- [ ] '爱奇艺PPS -《欢乐颂2》电视剧热播")

# %%

is_english('Instachat �')

# %%

is_english('Docs To Go™ Free Office Suite')


# ********
# %% todo: Tweak the function to only flag if it contains more than 3 chars
# ********

def is_english2(appname):

    ne_counter = 0

    for char in appname:
        if ord(char) > 127:
            ne_counter += 1

            if ne_counter == 4:
                # print(char)
                return False
                break
    
    # print(char)
    return True
 

# ~ ~ ~ ~ ~ ~ ~ ~ ~ Test Script ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 





# %%

is_english2("Test")

# %%

is_english2("- [ ] '爱奇艺PPS -《欢乐颂2》电视剧热播")

# %%

is_english2('Instachat �')


# %%

is_english2('Docs To Go™ Free Office Suite')


# %% todo: Segregate Apps between non_english and english apps


eng_apps = []
ne_apps = []


for app in android_clean:
    name = app[0]

    if is_english2(name):
        eng_apps.append(app)
    else:
        ne_apps.append(app)



# %%

eng_apps[:10]

# %%
ne_apps[:10]


# %%

print(len(eng_apps))
print(len(ne_apps))
print(len(eng_apps)+len(ne_apps))




# ----------------------------------------------------------------------
# %% 5. Isolate Free Apps
# ----------------------------------------------------------------------


# explore_data(android_clean)

print(android_header[:8])
col_slicer(android_clean[:10], 0, 8)

android_header[6]
# %%


# %%


android_free = []
android_paid = []


for app in  eng_apps:
    app_type = app[6]

    if app_type == 'Free':
        android_free.append(app)
    else:
        android_paid.append(app)


print(len((android_free)))
print(len((android_paid)))
print(len((android_free))+len((android_paid)))
# %%


i= -1
for app in android_paid:
    i += 1
    price = app[7]

    if price == '0':
        print(i)
        print(app)


# %%

print(android_header)

# %%
explore_data(android_paid, 641, 642)



# ----------------------------------------------------------------------
# %% 6. Function: Most Common Apps by Genre
# ----------------------------------------------------------------------




# %% Method 3


def pivot_count(dataset, index, percent = False, sort = False, pretty=False):
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
    pretty:
        

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
        print("\n---  Percentage of Total Count ---")
        for key in tally:
            tally[key] = round((tally[key]/total_counter) * 100, 2)


    if sort:
        tally =  sorted(tally.items(), key = lambda x: x[1], reverse=True)

    if pretty:
        if percent:
            for row in tally:
                print("{}: {:,}%".format(row[0],round(row[1],2)))
        else:
            for row in tally:
                print("{}: {:,}".format(row[0],round(row[1],2)))
        return None


    return tally




# %%

android_header

test =  pivot_count(android_free, 1)

print(test)


# %%
pivot_count(android, 0, sort=True)[:10]


# %%
pivot_count(android, 1, percent=True, sort=True, pretty=True)

# %%
pivot_count(android, 1, percent=False, sort=True, pretty=True)

# %%
pivot_count (android, 1, sort=True)

# %% genre android
print(android_header)
# pivot_count(android, -4, percent=True, sort=True, pretty=True)
# pivot_count(android_free, -4, percent=True, sort=True, pretty=True)


# ----------------------------------------------------------------------
# %% 7. Data by Genre for Free MObile Apps
# ----------------------------------------------------------------------

# gather the number of installs per category


android_installs = {}


for app in android_free:
    installs = int(app[5].replace(',','').replace('+', '').strip())
    cat = app[1]


    if cat in android_installs:
        android_installs[cat] += installs
    else:
        android_installs[cat] = installs


print(android_installs)
print("\n")

sorted_cat_installs = sorted(android_installs.items(), key=lambda x: x[1], reverse=True)

for line in sorted_cat_installs:
    print("{}: {:,}".format(line[0], line[1]))


android_installs['FAMILY']


# print(logged)

# %%
android_header[5]

# %%
'FAMILY' in android_installs



# %%

def pivot_sum(data, key, value, avg=False, sort=False, pretty=False):
    '''
    Input needs data, key, value
        - value: needs to be of numerical value, the script will 
            attempt to scrape out common characters
        - key: the column which you needs to be calculated
    Default:
        - outputs the sum of the "value" column
        - ouputs: dictionary:
    avg:
        - calculates the average per occurence
        - outputs: dictionary
    sort:
        - outputs: list
    prety:
        - print outs the calculation
    '''

    sum_table = {}
    freq_counter = pivot_count(data,key)


    for row in data:

        k = row[key]
        v = row[value]
        v = int(v.replace(',','').replace('+','').replace('$', '').strip())

        if k in sum_table:
            sum_table[k] += v
        else:
            sum_table[k] = v

    if avg:
        for ent in sum_table:
            sum_table[ent] = sum_table[ent]/freq_counter[ent]

    if sort:
        sum_table = sorted(sum_table.items(), key = lambda x: x[1], reverse=True)

    if pretty:
        print("\n --- Average ----")
        for line in sum_table:
            print("{} : {:,}".format(line[0],round(line[1],2)))
        return None



    return sum_table


pivot_sum(android_free, 1, 5, True, True, True)


# %%
pivot_sum(ios, -5, 5, True, True, True)

# %%

ios_header







