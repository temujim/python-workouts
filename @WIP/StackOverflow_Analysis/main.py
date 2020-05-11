import pandas as pd

# Config to set the display opton of DF on QTConsole
pd.set_option('display.max_colwidth', 10)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 25)

stackflow = pd.read_csv("Python_Workouts/@WIP/StackOverflow_Analysis/datasets/2019/survey_results_public.csv")
stackflow.head()

stackflow.columns
stackflow.describe()
stackflow.info()

# %% 
stackflow['Country'].value_counts()


# %% 

stackflow['EduOther'].value_counts()


# %% 
# stackflow.dropna(subset='EduOther',inplace=True)
online_learners= stackflow[stackflow['EduOther'].notna()]


# %% 
online_learners['EduOther'].value_counts()

# %%
print("-------------------------------\n")
print("Other Education")
online_learners.info()

# %% Actual Learners

actual = online_learners[online_learners['EduOther'].str.contains('online course')]
actual.info()
