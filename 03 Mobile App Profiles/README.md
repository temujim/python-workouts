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


## 1. Opening and Exploring the File


**To do:**
- [X] Import following CSV files as python objects:
    - [X] Separate the header and the data
    - [X] `AppleStore.csv` as `iOs` and `iOS_header` 
    - [X] `googleplaystore.csv` as `android` and `android_header`
- [X] Create a function to read the files anywhere (start, start)
    - [X] Arguments needed are: `start`, `end`, optional argument `rows_and_cols` 
        - [X] Default Arguments: start = 0, end = 5
        - [X] `rows_and_cols` defaul arg is False, to show the number of cols & rows
- [X] (TO ADD) add col slicing

## 2. Deleting the Wrong data

To do: 
- [X] Check what row is problematic
- [X] Confirm the row number
- [X] Delete
- [ ] (TO ADD) Error detection, for error
- [ ] (TO ADD) Remove duplicate apps in iOS data

## 3. Removing Duplicate Entries

To do:
- [X] As a sample, find list of duplicates for 'Instagram'
- [X] Count the total number of duplicates & print the list of duplicated apps
- [X] Create 2 list: unique_apps & duplicated_apps
- [X] Create a dictionary `review_max` of app names and most number of installs
- [X] Create a new list of clean apps only, should total 9659, retain the most number of installs
- [ ] (TODO) How about the iOS dataset? (Currently not considered)


## 4. Remove Non-English Apps
- [X] Write a function that takes in a string and returns `False` if there's any character in the string that doesn't bbelong to the set of common English, otherwise return true
- [X] Use your function to check these names:
    - [X] 'Instagram'
    - [X] '爱奇艺PPS -《欢乐颂2》电视剧热播'
    - [X] 'Docs To Go™ Free Office Suite'
    - [X] 'Instachat �'
- [X] Tweak the function to Only flag as false if characters constains more than 3
- [X] Segregate apps between non_english and english apps
- [ ] (TODO) how about the iOS dataset?



## 5. Isolate Free Apps
- [X] Create new list of free apps only, `android_free`. App count should be: 8,864
- [X] Create `iOS_free` dataset. App count should be: 3,222
**Note:** Use this dataset from here on, analysis should be limited to free apps only


## 6. Function: Most Common Apps by Genre
- [X] Create a function named `freq_table` that takes two inputs: `dataset` & `index` & SORT
    - [X] Method 1: Return values as sorted percentages, use lambda
        - [X] Create display_table function to Convert via into a list
        - [X] Use Lambda directly from freq_table function
        - [X] Print format to clean the decimals
    - [X] Method 2: Create a display_table function to convert into a list in sorting
        - [X] Use the freq_table within display table function
        - [X] Convert into a list to sort and output cleanly 
    - [X] Use the function to display `Category`, `Genres`, `prime_genre`

## 7. Data Analysis by Genre for Free Mobile Apps
- Android:
    - [X] freq_table for `Category` & `Genres`
    - [X] Most Popular Apps
    - [ ] Pattern
- iOS:
    - [X] display_table for `prime_genre`
    - [X] Most Popular Apps
    - [ ] Pattern
    - 

## 8. Installs per Category
- [X] Android: Average Installs per Category
- [X] iOS: Average Number of Ratings per Category



## TO DO:
- HIGH: Installs / App
- LOW: Avg App Rating per Category







