import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
import warnings
warnings.filterwarnings('ignore')

# ----------------------------------------------------------------------
# %% 1. Import and Remove duplicates
# ----------------------------------------------------------------------

# control the display range of dataframe output in QTConsole
pd.set_option("display.max_colwidth", 15)
pd.set_option("display.max_columns", 0)
pd.set_option("max_rows",7)

# import the apps.csv file as datfarame
apps = pd.read_csv("~/Python_Workouts/04 Android App Store Analysis/datasets/apps.csv", index_col=0)

print(apps)

# drop duplicate apps
apps = apps.drop_duplicates(subset = 'App')

# print the total number of apps
print("\n------------------------------------")
print("Total number of apps: " + str(len(apps)))

# look at 5 sample rows
print("\n---- 5 Sample Data Rows --------------")
print(apps.sample(5))


# ----------------------------------------------------------------------
# %% 2. Data Cleaning
# ----------------------------------------------------------------------

# -- Filter Column Size to show it contains 'K' or 'M'
# Drop columns which contains NA
# apps.dropna(how='any', inplace= True)
# 
# print("\n------Rows which contains specific characters")
# print(apps[apps['Size'].str.contains('M')])

# -- List the character to remove
delchars = [',', '$', '+', 'M', 'k']
cleancols = ['Size', 'Installs', 'Price']


for col in cleancols:

    for char in delchars:
        apps[col] = apps[col].str.replace(char, '')

    # convert  the column to numeric
    apps[col] = pd.to_numeric(apps[col])

# check if the colum is converted to numeric
print("\n-------- Check the datatype of the columns")
print(apps.info())


# ----------------------------------------------------------------------
# %% 3. Exploring App Categories
# ----------------------------------------------------------------------

# print the total of unique categories
len(apps['Category'].unique())

# Count the number of apps in each category
pd.set_option("display.max_rows", 60) # set df display  to max 60 rows
cat = apps['Category'].value_counts().sort_values(ascending=False)


# Create an Interactive Visualization APp Count per Category

data = go.Bar(x=cat.index, y=cat.values)

layout = go.Layout(
        title = dict(
            x = 0.5,
            xanchor = 'center',
            text = 'Number of Apps in Android Store per Category'
            ), 
        xaxis = dict(
            title = 'Category'
            ),
        yaxis = dict(
            title = 'Count'
            )
        )

Figbar = go.Figure(data, layout)

pyo.plot(Figbar, filename = "bar-graph.html")

# ----------------------------------------------------------------------
# %% 4. Distribution of App Ratings
# ----------------------------------------------------------------------

# What is the avarage rating of all apps
avg_rating = apps['Rating'].mean()

# Distribution of Apps according to their ratings


data = go.Histogram(x=apps['Rating'])

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
            text = 'App Rating Distribution',
            x = 0.5,
            xanchor = 'center'
            ),
        xaxis = dict(
            title = 'App Rating'
            ),
        yaxis = dict(
            title = 'Count'
            )
        )

FigHist = go.Figure(data, layout)
# FigHist = go.Figure(data)


pyo.plot(FigHist, filename = 'rating_dist.html')


# ----------------------------------------------------------------------
# %% 5. Size and Price of an App
# ----------------------------------------------------------------------

# gather list of categories 250 apps and above
cat250up = cat[cat>=250]

# only retain apps that below to 250 up app count
large_cats = apps[apps['Category'].isin(cat250up.index)]

# %% Another method of filter the apps to number of categories
large_cat_lambda = apps.groupby('Category').filter(lambda x: len(x) >= 250)
print(large_cat_lambda)

len(large_cat_lambda)
cat_grp = apps.groupby('Category')
print(cat_grp)
len(cat_grp)

# %%

# print(cat_grp['App'])
cat_grp['Type'].value_counts().loc['TOOLS']

# %%-----------------------------------------------------------------


rating_vs_size = sns.jointplot(x=apps['Size'], y=apps['Rating'], kind = 'hex')
plt.show()
print('App Rating vs Size')

# %% Paid App Analysis
paid_apps = apps[apps['Type']=='Paid']

rating_vs_price = sns.jointplot(y=paid_apps['Rating'], x=paid_apps['Price'])
plt.show()

# ----------------------------------------------------------------------
# %% 6. Relationshiop between App Category and App Price
# ----------------------------------------------------------------------

large_cats['Category'].value_counts()
top6_cats = cat[:6]
top6_appcats = apps[apps['Category'].isin(top6_cats.index)]

# make the chart larger
fig, ax = plt.subplots()
fig.set_size_inches(20, 8)

cat_vs_price = sns.stripplot(y=top6_appcats['Category'], x=top6_appcats['Price'])
plt.show()
print("Category vs Price Strip Plot")

# %%  Prince the category, App and Prce for Apps that are price above 20
print("\n--------- Apps price above $200 ---------------------")
print(apps[['Category', 'App', 'Price']][apps['Price'] >= 200])

# ----------------------------------------------------------------------
# %% 7. Filter out "junk" apps
# ----------------------------------------------------------------------

fig, ax = plt.subplots()
fig.set_size_inches(20,8)
clean_apps = large_cats[large_cats['Price']<= 100]
cat_vs_price_clean = sns.stripplot(y=clean_apps['Category'], x=clean_apps['Price'])
plt.show()
print("Category vs Price Strip Plot - CLEAN")

# ----------------------------------------------------------------------
# %% 8. Popularity of Paid Apps vs Free Apps
# ----------------------------------------------------------------------


# %%
free_apps = apps[apps['Type']=='Free']

free_apps['Installs'].values
# %%

# paid_trace = go.Box(x=paid_apps['Type'].index, y=paid_apps['Installs'].values)
# free_trace = go.Box(x=free_apps['Type'].index, y=free_apps['Installs'].values)
paid_trace = go.Box(y=paid_apps['Installs'], name = "Paid Apps")
free_trace = go.Box(y=free_apps['Installs'], name = "Free Apps")

layout = go.Layout(
        title=dict(
            text = 'Price Visualization of Paid vs Free Apps',
            x = 0.5,
            xanchor = 'center'
            ),
        yaxis = dict(
            type = 'log'
            )
        )

FigBox = go.Figure(data=[free_trace, paid_trace], layout = layout)

pyo.plot(FigBox)

# ----------------------------------------------------------------------
# %% Sentiment Analysis of User Review
# ----------------------------------------------------------------------


# Import User Reviews as dataframe

user_review = pd.read_csv("~/Python_Workouts/04 Android App Store Analysis/datasets/user_reviews.csv")
print("\n")
print(user_review.head(3))
print("\n")
print(apps.head(3))

app_reviews = apps[['App','Type']].merge(user_review[['App','Sentiment_Polarity']], left_on='App', right_on='App')
app_reviews.dropna(inplace=True)

fig, ax = plt.subplots()
fig.set_size_inches(12, 8)
sns.boxplot(data=app_reviews, x='Type', y='Sentiment_Polarity')
plt.title("Sentiment Analysis: Free vs Paid")
plt.show()
