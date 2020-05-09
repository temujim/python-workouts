##
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid') #set grid style for chartplots
import warnings
warnings.filterwarnings('ignore')


# Config to set the display opton of DF on QTConsole
pd.set_option('display.max_colwidth', 15)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 25)

apps = pd.read_csv("~/python/Workouts_Notes/Projects/Android_App/datasets/apps.csv", index_col=0)
# print(apps.head())

# drop duplicates

print("\n--------- 1. Print the 5 samples of the header -----")
apps = apps.drop_duplicates(subset='App')
print(apps.sample(5))


# ----------------------------------------------------------------------  
# %% 2. Data Cleaning
# ----------------------------------------------------------------------  

cleancols = ['Installs', 'Price', 'Size']
delchars = ['$', ',', '+', 'M', 'k', ]



print("=========================================================")
print("OUTPUT:")
print("=========================================================")

# print(apps[apps['Size'].isin(['19M', '20M'])])
apps = apps.dropna()
print("\n-----------= Apps that contained M in Size =--------------------\n")
print(apps[apps['Size'].str.contains("M")].head())
print("\n----------------------------------------------------------------\n")

for col in cleancols:

    for char in delchars:
        apps[col] =  apps[col].str.replace(char,'')

    apps[col] = pd.to_numeric(apps[col])

print("\n\n -------- 2 Show values if it is already in numeric form ---\n")
print(apps.info())



# ----------------------------------------------------------------------  
# %% 3. Exploring App Categories using Plotly
# ----------------------------------------------------------------------  

# Print the total number of unique categories

print(len(apps['Category'].unique()))

print("\n ---------  Average ratings of the apps")
cat = apps['Category'].value_counts()
print(cat)

data = go.Bar(x=cat.index, y=cat.values)

layout = go.Layout(
    title = dict(
        text = 'Number of Apps per Categories',
        x = 0.5,
        xanchor = 'center'
    ),
    yaxis = dict(
        title = "Count"
    ),
    xaxis = dict(
        title = "Category"
    )
)

Fig = go.Figure(data,layout)
pyo.plot(Fig, filename="android-app-barplot.html")

# Option for PyQT display instead of browser
# # -- does not work,  I'm unable to install Orca
# import plotly.io as pio
# 
# # pio.renderers.default = "browser"
# # png_renderer = pio.renderers["png"]
# # png_renderer.width = 500
# # png_renderer.height = 500
# # pio.renderers.default = "png"
# # 
# data = go.Bar(x=cat.index, y=cat.values)
# 
# def show_in_window(fig):
#     import sys, os
#     import plotly.offline
#     from PyQt5.QtCore import QUrl
#     from PyQt5.QtWebEngineWidgets import QWebEngineView
#     from PyQt5.QtWidgets import QApplication
# 
#     plotly.offline.plot(fig, filename='name.html', auto_open=False)
# 
#     app = QApplication(sys.argv)
#     web = QWebEngineView()
# #     file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name.html"))
#     file_path = os.path.abspath(os.path.join("/home/barca/", "name.html"))
#     web.load(QUrl.fromLocalFile(file_path))
#     web.show()
#     sys.exit(app.exec_())
# 
# 
# layout = go.Layout(
#         title = dict(
#             text = "Number of Apps per Categories",
#             x = 0.5,
#             xanchor = 'center'
#             ),
#         yaxis = dict(
#             title = "Number of Apps"
#             ),
#         xaxis = dict(
#             title = "Category Names")
#         )
# 
# FigBar = go.Figure(data, layout)
# # pyo.plot(FigBar, filename='FigBar.html')
# 
# # FigBar.show()
# show_in_window(FigBar)



# ----------------------------------------------------------------------  
# %% 4. Distribution of App Ratings 
# ----------------------------------------------------------------------  

print("\n ---------  4. App Ratings -------------")
avg_rating = apps['Rating'].mean()
print(avg_rating)

data = go.Histogram(x=apps['Rating'])

layout = go.Layout(
    title = dict(
        text = "App Rating Distribution",
        xanchor = 'center',
        x = 0.5
    ),
    xaxis = dict(
        title = "App Ratings"
    ),
    yaxis = dict(
        title = "Count"
    ),
    shapes = [dict(
        type = 'line',
        x0 = avg_rating,
        x1 = avg_rating,
        y0 = 0,
        y1 = 1000,
        line = dict(
            dash = 'dashdot'
        )
    )]

)

FigDist = go.Figure(data, layout)
pyo.plot(FigDist, filename='app-histplot.html')


# ########### 5. Size and price of an app

popcat_apps = apps.groupby('Category').filter(lambda x: len(x) >= 250)


# ----------------------------------------------------------------------  
# %% 5. Size and Price of an App
# ----------------------------------------------------------------------  
print("\n --------- 5. Size and Price of an app -----------")


print(popcat_apps.sample(5))
print(len(popcat_apps))

rating_VS_size = sns.jointplot(x=popcat_apps['Size'], y=popcat_apps['Rating'],kind='hex')
plt.title("App Ratings Vs Size")
plt.show()
print("Apps vs Ratings Graph")

## Paid App Analysis

paid_apps = apps[apps['Type'] == 'Paid']
print("\n------- List of Paid Apps --------")
print(paid_apps.sample(5))
print(len(paid_apps))

rating_VS_Price = sns.jointplot(x=paid_apps['Price'], y=paid_apps['Rating'])
plt.title('Rating vs Price')

plt.show()
print('Rating vs Price Graph')

# ----------------------------------------------------------------------  
# %% 6. Relationship between app category and Price
# ----------------------------------------------------------------------  

# Set Plot Size
fig, ax = plt.subplots()
fig.set_size_inches(20,8)

#  Option 1: Gather the 6 Categories only, this shows about 7 categories
# top6_cats = apps[apps['Category'].isin(popcat_apps['Category'].unique())]

# Option 2: Show only 7
top6_catlist = ['FAMILY', 'GAME', 'TOOLS', 'PERSONALIZATION', 'LIFESTYLE', 'MEDICAL']
top6_cats = apps[apps['Category'].isin(top6_catlist)]
print("\n ------ #6 Price vs Apps")
print(top6_cats.sample(10))

# Seaborn STRIPPLOT
price_vs_Cat = sns.stripplot(x=top6_cats['Price'], y=top6_cats['Category'])

plt.show()
print("Price and Category Relationship")

# ---
# %% Print the Category, App Price for apps priced above 200
# Gather the 3 columsn only
apps[['Category','App','Price']].head()

# %% now gather the 3 columns with the price filter
#modify qtconsole column width to show app name info
pd.set_option('display.max_colwidth', 30)

junk_apps = apps[['Category','App','Price']][apps['Price'] >= 200]
print(junk_apps)

# ----------------------------------------------------------------------  
# %% 7. Filter out "junk" apps
# ----------------------------------------------------------------------  

# readjust df colwidth
pd.set_option('display.max_colwidth', 15)

# apps_under_100
apps_under_100 = popcat_apps[popcat_apps['Price'] <= 100]
# Gather the values to plot
# print(apps_under_100['Price'].values)
# print(apps_under_100['Category'].values)

# Set Plot Size
fig, ax = plt.subplots()
fig.set_size_inches(20,8)

# Stripplot using under apps_under_100
cat_VS_price_under100 = sns.stripplot(x=apps_under_100['Price'].values, y=apps_under_100['Category'].values)

plt.show()
print("Category vs Price For Apps Under 100")

# ----------------------------------------------------------------------  
# %% 8. Popularity of paid apps vs free apps
# ----------------------------------------------------------------------  

# -- Works but not effective since the colors is not different
# # apps['Type'].values
# # apps['Installs'].values
# data = go.Box(x=apps['Type'].values, y=apps['Installs'].values)

paid_trace = go.Box(y=apps[apps['Type']=='Paid']['Installs'], name = 'Paid Apps')
free_trace = go.Box(y=apps[apps['Type']=='Free']['Installs'], name = 'Free Apps')



#
layout = go.Layout(
        title = dict(
            text = 'Free vs Paid App Downloads',
            x = 0.5,
            xanchor = 'center'
            ),
        yaxis=dict(
            type='log',
            autorange = True,
            title = 'Downloads'),
    )
#
FigBox = go.Figure(data=[paid_trace, free_trace], layout=layout)
pyo.plot(FigBox)


# ----------------------------------------------------------------------  
# %% 9. Sentiment Analysis of User Reviews
# ----------------------------------------------------------------------  

# Import User Reviews as DF
df_reviews = pd.read_csv("Python_Workouts/04 Android App Store Analysis/datasets/user_reviews.csv")
print("\n --------------- User Reviews Dataframe")
print(df_reviews.head())


# %% App Type Pd Series

# Merge `df_review` with `apps` dataframe
df_apptype_sentiments = apps[['App', 'Type']].merge(df_reviews, left_on='App', right_on='App')

# drop NA values
df_apptype_sentiments.dropna(how="any", inplace=True)
print(df_apptype_sentiments.sample(20))

# %%
# configure chart size
fig, ax = plt.subplots()
fig.set_size_inches(15,10)

boxplot_apptype_sentiments = sns.boxplot(data=df_apptype_sentiments, x='Type', y='Sentiment_Polarity')
plt.title("Sentiment Analysis by App Type", fontsize=16)
plt.show()


print("Android Apps Sentiment Analysis by App Type")

