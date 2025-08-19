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
