## Panda Exercise

Changelog:
---
5/20/2020:
    - fibo8 workout
    - pandas exercise in addin dataframe for dictionaries


1. [O] Adding a new column in a panda dataframe.
    - [O] A. FOR LOOP
        - [X] i.   Import data to pandas
            -- file: /python/datacamp/Notes/datasets/brics.csv
        - [X] ii.  Do a for loop fo the index & Country & Capital values
        - [X] iii. Do a for loop to upper the country values
        - [X] iv.  Show the value of capital to BR index. What is the datatype?
            - [X] a.  Pull the same data as a series, with 'capital' as the primary index
            - [X] b.  Pull the same data as a dataframe
        - [X] v.   Get the value of the capital columns using 3 aproaches (output should be a series)
        - [X] vi.  Get the value of the BR rows..Can you pull the data using the same 3 approaches
        - [ ] vii.  Add a new columnn with all the letter of country capitalized using loop
    - [X] B. APPLY DATAFRAME (not necessary with recent versions of panda)
        - [X] i.   Add column adding a new capitalizeda all latters for CAPITAL using apply metho
        - [X] ii.  Next iteration would be to add a column that counts the number of characters "a" under capital
2. Createa a dataframe: dictinoary of list
    - [X] i.   From Raw Dictionaries: 3x3, headers col1 to col3,
        - [X] a.  From dictionary, query col3
        - [X] b.  From dictionary, pull out '8'
        - [X] (NOTE) list of dictionary method in importing
        - [X] a.  From dataframe, pull out query col3
        - [X] b.  From dataframe, pull out '8'
    - [X] ii. Rename index names from index integer to: index row1 to row2
        - [X] a. from dataframe, pull out '8' using col and index names without using any method
        - [X] b. from dataframe, pull out '8' pandas method of label-based indexing
        - [X] c. from dataframe, pull out '8' pandas method of index-based slicing
    - [X] iii. Understanding the datatypes
        - [X] a. single data type (str,int)
            - [X] Pull out number 8 within one list only
            - [X] What is the data type?
        - [X] b. series data type 
            - [X] Pull out row3 only
            - [X] What is the datatype
        - [X] c. dataframe
            - [X] Pull out row1 & row2, col2 & col3
            - [X] What is the datatype
                - [X] Other ways of slicing:
                    - [X] grab row 1& row3, col1 & col3
                    - [X] grab row1 and row2, col1 and col3
                    - [X] Use label-based slicing for the first 2 samples
3. Other ways of creating dataframes:
    - List of Dictionaries
    - Numpy
5. [ ] [SOON] DF SLICING
