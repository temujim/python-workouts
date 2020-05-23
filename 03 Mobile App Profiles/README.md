# Profitable App Profiles for the Mobile Store Markets 

This project aims to analyze a csv file without using Pandas.

Research the specs:
- Category
- Free or Paid
    - if Free: What Category
    - if Paid: What Category
- App Size
- Target Installs
- Target Avg Rating


The Exercise is taken from DataQuest as a Guided Project

* The basics of programming in Python (arithmetical operations, variables, common data types, etc.)
* List and for loops
* Conditional statements
* Dictionaries and frequency tables
* Functions
* File reader


TODO:
1. [ ] Go through the findings and pattern
2. [ ] Remove the unncessary scripts
3. [ ] Clean the Core File for better referene
4. [ ] MUST: MIGRATE PIVOT_COUNT and PIVOT_SUM functions to core file

OOP Barebones CSV File Analyzer:
1. Explore Data
2. Col Slicer
3. Find Rows 
4. Remove Duplicates 
5. Remove unclean rows
6. Remove non-english characters
7. Count Columns
8. Count Percentage Columns
9. Sum Columns (VLookup Equivalent for Sum)


--

FiboRuns:
0 - May 21, 2020
1 - May 22-23, 2020
    - Added Error detection under #2
    - Created a script to do #2
    - Under #5 Free App isolation, investigated which app rows are problematic
    - Added Method 3 under #6 to sort, calculate abs and percentage

## 1. Opening and Exploring the File


**To do:**
- [X] Import following CSV files as python objects:
    - [X] Separate the header and the data
    - [X] `AppleStore.csv` as `iOs` and `iOS_header` 
    - [X] `googleplaystore.csv` as `android` and `android_header`
- [X] Create a function to read the files anywhere (start, start), name `explore_data`
    - [X] Arguments needed are: `start`, `end`, optional argument `rows_and_cols` 
        - [X] Default Arguments: start = 0, end = 5
        - [X] `rows_and_cols` defaul arg is False, to show the number of cols & rows
- [X]  add col slicing
**Note: Key file Output, android**

## 2. Deleting the Wrong data

To do: 
- [X] Check what row is problematic
- [X] Confirm the row number
- [X] Delete
- [X] (TO ADD) Error detection, for error
- [X] (TO ADD) Remove duplicate apps in iOS data

## 3. Removing Duplicate Entries

To do:
- [X] As a sample, find list of duplicates for 'Instagram'
- [X] Count the total number of duplicates & print the list of duplicated apps
- [X] Create 2 list: unique_apps & duplicated_apps
- [X] Create a dictionary `review_max` of app names and most number of reviews
- [X] Create a new list of clean apps only, should total 9659, retain the most number of installs
      The `installs` instruction needs to be revisited, as this is very vague, should be reviews
- [ ] (TODO) How about the iOS dataset? (Currently not considered)
*Note:* Key file Output, android_clean - 9,659


## 4. Remove Non-English Apps
- [X] Write a function that takes in a string and returns `False` if there's any character in the string that doesn't bbelong to the set of common English, otherwise return true
- [X] Use your function to check these names:
    - [X] 'Instagram'
    - [X] '爱奇艺PPS -《欢乐颂2》电视剧热播'
    - [X] 'Docs To Go™ Free Office Suite'
    - [X] 'Instachat �'
- [X] Tweak the function to Only flag as false if characters constains more than 3
- [X] Segregate apps between non_english and english apps
    - [X] Number of android eng apps should be:  9614 and non-english apps should be: 45
- [ ] (TODO) how about the iOS dataset?
Note: Key file Output, eng_apps: 9,614 and non_eng 45


## 5. Isolate Free Apps
- [X] Create new list of free apps only, `android_free`. App count should be: 8,864 & 750 android paid apps
      Note: 8,863 free apps is manageable, depending on the columns used.
      - [X]  Try determining which app is causing the problem
- [ ] Create `iOS_free` dataset. App count should be: 3,222
**Note:** Use this dataset from here on, analysis should be limited to free apps only


## 6. Function: Most Common Apps by Genre
- [.] Create a function named `freq_table` that takes two inputs: `dataset` & `index` & SORT
    - [ ] Method 1: Return values as sorted percentages, use lambda
        - [ ] Create display_table function to Convert via into a list
        - [ ] Use Lambda directly from freq_table function
        - [ ] Print format to clean the decimals
    - [ ] Method 2: Create a display_table function to convert into a list in sorting
        - [ ] Use the freq_table within display table function
        - [ ] Convert into a list to sort and output cleanly 
    - [X] Method 3: Create function with option to output dictionary abs values, pecetagen and sorted output
- [ ] Use the function to display `Category`, `Genres`, `prime_genre`

## 7. Data Analysis by Genre for Free Mobile Apps
- Android:
    - [X] freq_table for `Category` & `Genres`
        - [X] OUTPUT:  
            - Android Category Percentage | FAMILY:18.19%, GAME:10.55%, TOOLS:7.78%
            - Android Genre Percentage | Tools: 8.45% , Entertainment: 6.07%, Education: 5.35%
    - [ ] Pattern
- iOS:
    - [ ] display_table for `prime_genre`
    - [ ] Pattern

## 8. Installs per Category
- [X] Create `pivot_sum` function
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
- [X] Android: Average Installs per Category
    - [X] Output:
            COMMUNICATION : 38,456,119.17
            VIDEO_PLAYERS : 24,727,872.45
            SOCIAL : 23,253,652.13
- [ ] iOS: Average Number ow.js Ratings per Category
    - [ ] Output:
            Navigation : 86,090.33 
            Reference : 74,942.11 
            Social Networking : 71,548.35
            


## TO DO:
- HIGH: Installs / App
- LOW: Avg App Rating per Category







