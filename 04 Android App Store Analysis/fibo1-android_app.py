import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_colwidth', 15)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_rows', 20)

# ----------------------------------------------------------------------
# %% 1. Import Google Store Data
# ----------------------------------------------------------------------

apps = pd.read_csv("/home/barca/Python_Workouts/04 Android App Store Analysis/datasets/apps.csv", index_col=0)
apps

apps.drop_duplicates(subset = 'App')
# apps.dropna(inplace=True)
print("\nThe total number of apps is: " + str(len(apps)))

print("\n--- Show sample of 5 apps")
print(apps.sample(5))

# ----------------------------------------------------------------------
# %% 2. Data Cleaning
# ----------------------------------------------------------------------

# drop rows if Size col is NA
# apps.dropna(subset=['Size'])

# show the rows with M in Size colums
# apps[apps['Size'].str.contains('M')]

# characters to delete and cols to clean
delchars = [',', '$', '+', 'M', 'k']
cleancols = ['Installs', 'Size', 'Price']

for col in cleancols:

    for char in delchars:
        apps[col] = apps[col].str.replace(char, '')

    apps[col] = pd.to_numeric(apps[col])



# ----------------------------------------------------------------------
# %% 3. Exploring App Categories
# ----------------------------------------------------------------------

# %% todo: Print the total number of unique categories
len(apps['Category'].unique())

# %% todo: Count the number of apps in each category and sort in Desc ord
cat_count = apps['Category'].value_counts().sort_values(ascending=False)

# %% todo: Create an Interactive Visualization: App per Count Category

# create charttrace
data = go.Bar(x=cat_count.index, y=cat_count.values)

# set config
layout = go.Layout(
        title = dict(
            text='Apps per Category Count',
            x = 0.5,
            xanchor = 'center'
            ),
        yaxis = dict(
            title = 'Number of Apps'
            ),
        xaxis = dict(
            title = 'Category Names'
            )
    )


# create figure
FigBar = go.Figure(data, layout)

# plot
pyo.plot(FigBar, filename = "/home/barca/Python_Workouts/04 Android App Store Analysis/viz/03-bar.html")


# ----------------------------------------------------------------------
# %% 4. Distribution of App ratings
# ----------------------------------------------------------------------

# %% todo: avg ratings of app
avg_rating = apps['Rating'].mean()
print(avg_rating)

# ------------------------------
# %% todo: Distribution of apps according to ratings



# trace histogram
data = go.Histogram(x=apps['Rating'])


# Set Configuration, avg line
layout = go.Layout(
        shapes = [dict(
            x0 = avg_rating,
            x1 = avg_rating,
            y0 = 0,
            y1 = 1000,
            type = 'line',
            line = dict(
            dash = 'dashdot')
            )],
        title = dict(
            text = 'App Rating Distribution',
            x = 0.5,
            xanchor = 'center'
            ),
        yaxis = dict(
            title = 'Number of Apps'
            ),
        xaxis = dict(
            title = 'App Ratings'
            )
        )


# Create Figure
#FigHist = go.Figure(data,layout)
FigHist = go.Figure(data, layout)

# output plot
pyo.plot(FigHist, filename="/home/barca/Python_Workouts/04 Android App Store Analysis/viz/04-Hist.html")

# 

# ----------------------------------------------------------------------
# %% 5. Size and Price of Apps
# ---------------------------------------------------------------------- 

# Method one
print(cat_count[:6])

pop_top6cat_apps_only = apps[apps['Category'].isin(cat_count[:6].index)]
# %%
pop_top6cat_apps_only['Category'].unique()

# %% Method 2

pop_cat_apps_only = apps.groupby('Category').filter(lambda x: len(x)>=250)
print(pop_cat_apps_only)
pop_cat_apps_only['Category'].value_counts( )

# %% Joint Plot

rating_VS_size = sns.jointplot(x=pop_cat_apps_only['Size'], y=pop_cat_apps_only['Rating'], kind='hex')
plt.show()

# %% todo: Paid App Analysis: Rating vs Price

paid_apps = apps[apps['Type']=='Paid']
# print(paid_apps.sample(5))



rating_VS_price = sns.jointplot(x=paid_apps['Price'], y=paid_apps['Rating'])
plt.show()
print("Paid Apps: Rating vs Price Joint Plot")


# ----------------------------------------------------------------------
# %% 6. Relationship between app category and price
# ----------------------------------------------------------------------


# pd.set_option('display.max_rows', 50)
# print(cat_count)

pop_cat_list = ['GAME', 'FAMILY', 'PHOTOGRAPHY', 'MEDICAL', 'TOOLS', 'FINANCE', 'LIFESTYLE', 'BUSINESS']

popcats = apps[apps['Category'].isin(pop_cat_list)]
popcats['Category'].value_counts()


# %% todo: Createa a stripplot
# make the chart larger
fig, ax = plt.subplots()
fig.set_size_inches(20, 8)
price_per_popcat = sns.stripplot(y=popcats['Category'], x=popcats['Price'])
plt.title("Price per Category")
plt.show()
print("Price per Category")

# %% todo: Print the Category, App, Price for Apps that are priced above 200

pd.set_option("display.max_colwidth", 30 )
apps[['Category', 'App', 'Price']][apps['Price']>=200]

# ----------------------------------------------------------------------
# %% 7. Filter out Junk apps
# ----------------------------------------------------------------------


# Retain apps price 100 below only in popcats

# count the curren tnumber of popcats
print(len(popcats))
#popcats.sample(5)

# remote the junk apps
clean_popcats = popcats[popcats['Price']<=100]
print(len(clean_popcats))

# Update the strip plot
fig, ax = plt.subplots()
fig.set_size_inches(20,8)
clean_strip = sns.stripplot(y=clean_popcats['Category'], x=clean_popcats['Price'])

# ----------------------------------------------------------------------
# %% 8. Popularity of Paid Apps vs Free APps
# ----------------------------------------------------------------------


free_apps = apps[apps['Type'] == 'Free']
print(free_apps)

print(free_apps['Price'])

# paidtrace
box_paid = go.Box(y=paid_apps['Installs'], name = 'Paid')

box_free = go.Box(y=free_apps['Installs'], name = 'Free')




# Set Viz Config
layout = go.Layout(
        yaxis = dict(
            type = 'log'
            )
        )


# Create Box Plot
FigBox = go.Figure(data=[box_paid, box_free], layout=layout)


# output plot
pyo.plot(FigBox)


# ----------------------------------------------------------------------
# %% 9. Sentiment Analysis of User Review
# ----------------------------------------------------------------------

user_reviews = pd.read_csv("/home/barca/Python_Workouts/04 Android App Store Analysis/datasets/user_reviews.csv")
print(user_reviews.sample(5))



app_type_sentiments = apps[['App','Type']].merge(user_reviews[['App','Sentiment_Polarity']], left_on='App', right_on='App')
print(app_type_sentiments.sample(5))

# total number of rows
print(len(app_type_sentiments))

# count the number of na's under 'Sentiment Polarity'
print(app_type_sentiments['Sentiment_Polarity'].isna().sum())


# dropna
app_type_sentiments.dropna(inplace=True)
len(app_type_sentiments)

# update size
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# create a static box type, for free vs paid, sentiment polarity
free_paid_sentiments = sns.boxplot(data=app_type_sentiments, x='Type', y='Sentiment_Polarity')
plt.title("Sentiment Analysis: Free vs Paid", fontsize = 15, weight = 'bold')
plt.show()

