import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import warnings
warnings.filterwarnings('ignore')


# control the display in jupyter console
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_colwidth', 15)
pd.set_option('display.max_rows', 30)



# %% 1. Import CSV to Pandas and drop duplicates

apps = pd.read_csv("/home/barca/Python_Workouts/04 Android App Store Analysis/datasets/apps2.csv",\
        index_col = 0)

# show the apps imported
apps.head()

print("The total number of apps imported to dataset: {:,}".format(len(apps)))

apps.drop_duplicates(subset='App', inplace=True)
print("The total number of unique apps is: {:,}".format(len(apps)))

# %% Show 5 row samples
print("\n ---  Show 5 row samples -------")
print(apps.sample(5))

# ----------------------------------------------------------------------
# %% 2. Data Cleaning
# ----------------------------------------------------------------------

# *******
# %% todo: Filter the column size to show if it constains K or M
# *******

# first you need to remove nan rows
apps.dropna(subset=['Size'], inplace=True)
print("\n ---- Total number of apps after dropping na under Size")
print(len(apps))

# %%
apps[apps['Size'].str.contains('K')]


# *******
# %% todo: What are the datatypes of the columns
# *******

apps.info()



# -------
# #%%todo: Convert `Reviews` to int32
print(apps['Reviews'].dtype)
apps['Reviews'] = apps['Reviews'].astype('int32')
print(apps['Reviews'].dtype)


# -------
# %% todo: Convert `Rating` to `float32`
print(apps['Rating'].dtype)
apps['Rating'] = apps['Rating'].astype('float32')
print(apps['Rating'].dtype)

# -------
# %% todo: Convert `Price` column to float 32
# apps['Price'].dtype
# apps['Price'].astype('float32') #this shows error due to non-numeric chars


# ********
# %% todo: Characters to remove and under which columsn
# ********
cleancols = ['Size', 'Installs', 'Price']
delchars = [',', 'M', '+', '$']

for col in cleancols:

    for char in delchars:
        apps[col] = apps[col].str.replace(char,'')
        
    apps[col] = pd.to_numeric(apps[col])

# %%
apps.info()
apps.sample(5)


# ----------------------------------------------------------------------
# %% 3. Exploring App Categories
# ----------------------------------------------------------------------

# *******
# %% todo: Print the total number of categories
# *******


# using the unique method
print(len(apps['Category'].unique()))


# ********
# %% todo: Count the number of apps per Category
# ********
cat_count = apps['Category'].value_counts().sort_values(ascending=False)
print(cat_count)



# ********
# %% todo: Create an Interactive Visuazliation App Count per Category
# ********

data = go.Bar(x=cat_count.index, y=cat_count.values)

layout = go.Layout(
        title = dict(
            text = 'Apps Per Category',
            x = 0.5,
            xanchor = 'center',
            font = dict(
                size = 30,
                color = 'Blue'
                )
            ),
        yaxis = dict(
            title = 'Number of Apps'
            ),
        xaxis = dict(
            title = 'Category Names'
            )
        )

FigBar = go.Figure(data, layout)


pyo.plot(FigBar, filename = '/home/barca/Python_Workouts/04 Android App Store Analysis/viz/fib3-03-bar.html')



# ----------------------------------------------------------------------
# %% 4. Distribution of App Ratings
# ----------------------------------------------------------------------


# %% todo What is the average ratings of the apps

avg_rating = apps['Rating'].mean()
print(avg_rating)


# %% todo: Distribution of apps according ot their ratings


data = go.Histogram(x = apps['Rating'])



layout = go.Layout(
        shapes = [dict( 
            type = 'line',
            x0 = avg_rating,
            x1 = avg_rating,
            y0 = 0,
            y1 = 1000,
            line = dict(
                dash = 'dashdot'
                )
            )],
        title = dict(
            text = 'Distribution of App Ratings',
            x = 0.5,
            xanchor = 'center'
            ),
        yaxis = dict(
            title = 'Count of Apps'
            ),
        xaxis = dict(
            title = 'Ratings'
            )
        )



FigHist = go.Figure(data, layout)

pyo.plot(FigHist)



# ----------------------------------------------------------------------
# %% 5. Size and Price of an App
# ----------------------------------------------------------------------

# %% Large Category Analysis


# %% option #1 groupby
popcat_apps = apps.groupby('Category').filter(lambda x: len(x)>=250)

popcat_apps['Category'].value_counts()


# %% option # using isin method and numpy slicing

popcat_apps2 = apps[apps['Category'].isin(cat_count[cat_count >= 250].index)]

popcat_apps2['Category'].value_counts()

# %%
print(cat_count[cat_count > 250].index)



Rating_vs_Size = sns.jointplot(x=apps['Size'], y=apps['Rating'], kind = 'hex')
plt.show()
print("Rating vs Size JoinPlot")



# ********
# %% todo: Paid App Analysis 
# ********

paid_apps = apps[apps['Type']=='Paid']

paid_apps.sample(5)


# %% JointPlot of Paid Apps Rating vs Price

Rating_vs_rpice = sns.jointplot(x=paid_apps['Price'], y=paid_apps['Rating'])
plt.show()
print("Paid Apps: Rating vs Price Joint Plot")



# ----------------------------------------------------------------------
# %% 6. Relation between App Category and App Price
# ----------------------------------------------------------------------

# *******
# %% todo: Strip Plot of Specific Categories
# *******

popcat_list = ['GAME', 'FAMILY', 'PHOTOGRAPHY', 'MEDICAL', 'TOOLS', 'FINANCE', 'LIFESTYLE', 'BUSINESS']


stripcats = apps[apps['Category'].isin(popcat_list)]
stripcats.sample(5)

# make the chart larger
fig, ax = plt.subplots()
fig.set_size_inches(20, 8)


Category_Prices = sns.stripplot(y=stripcats['Category'], x=stripcats['Price'])
plt.title("Price Distribution by Category")


# --------
# %% todo: Print the Category, App, Price which are priced above $200 
# --------

apps.loc[:, ['Category', 'App', 'Price']][apps['Price']>=200]


# ----------------------------------------------------------------------
# %% 7. Filter out the "junk" apps
# ----------------------------------------------------------------------

# %% Slice out data, remove junk apps
clean_apps = stripcats[stripcats['Price'] <= 100]


# %% Redo StripPlot using updated dataset
fig, ax = plt.subplots()
fig.set_size_inches(20, 8)

sns.stripplot(x=clean_apps['Price'], y=clean_apps['Category'], jitter=True, linewidth = 1)
plt.show()



# ----------------------------------------------------------------------
# %% 8. Popularity of Paid Apps vs Free Apps
# ----------------------------------------------------------------------



FreeBox = go.Box(y=apps[apps['Type']=='Free']['Installs'], name = 'Free')

PaidBox = go.Box(y=apps[apps['Type']=='Paid']['Installs'], name = 'Paid')

layout = go.Layout(
        yaxis = dict(
            type = 'log',
            title = 'App Installs'
            ),
        title = dict(
            text = "Free vs Paid App Installs",
            x = 0.5,
            xanchor = 'center'
            )
        )


FigBox = go.Figure(data=[FreeBox, PaidBox], layout = layout)

pyo.plot(FigBox)





# ----------------------------------------------------------------------
# %% 9. Sentiment Analysis of User Reviews
# ----------------------------------------------------------------------


# %% import user_reviews csv as pandas df
user_reviews = pd.read_csv("/home/barca/Python_Workouts/04 Android App Store Analysis/datasets/user_reviews.csv")
user_reviews.sample(5)



# %% Merge columsn
apptypes_sentiments = apps.loc[:,['App', 'Type']].merge(user_reviews.loc[:, ['App', 'Sentiment_Polarity']], left_on = 'App', right_on = 'App')
apptypes_sentiments.sample(5)


# %%drop rows with na values 
apptypes_sentiments.dropna(how='any', inplace=True)
print(len(apptypes_sentiments))


# %% Create box plot

fig, ax = plt.subplots()
fig.set_size_inches(12, 8)

sns.boxplot(data=apptypes_sentiments, x='Type', y='Sentiment_Polarity')
plt.title("Sentiment Polarity: Paid vs Free Apps")


