## Project 1: Linear Regression
## Author: Michael Lee
## Tutorial Review

# Downloading the Data - utilize 'urlretrieve' function from 'urllib.request'

medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve
urlretrieve(medical_charges_url, 'medical.csv')

# Create a Pandas dataframe using the downloaded file, to view and analyze data.

import pandas as pd
medical_df = pd.read_csv('medical.csv')
medical_df

# Check to DF to ensure it was installed

medical_df.info()
print(medical_df.describe())


# Exploratory Analysis and Visualization
# Install plotlty, matplotlib, and seaborn. Then import them into the the script

import plotly.express as px # High-level api
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# improvising the default style and the fonts in our charts
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10,6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

## Age
# Visulaize the distribution of age using a histogram with 47 bins (one for each year) and a box plot.
# Utilize plotly to make the chart interactive (Note: similar charts could be used with Seaborn)

medical_df.age.describe()

fig = px.histogram(medical_df,
                   x='age',
                   nbins=47,
                   title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show()
