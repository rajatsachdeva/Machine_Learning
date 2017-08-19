# Machine Learning: Regression Intro
# Using continous data, like stock prices 

import pandas as pd
import quandl
import sys
sys.path.append('../authentication/')
import auth
import math

# Authenticate with quandl
auth.authenticat_with_quandl()

# Get the data from quandl 
df = quandl.get('WIKI/GOOGL')

# Check if we are able to get the data or not
# prints a table 
#print (df)

# recreate the data frames containing only ajusted columns 
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Prints data related to above columns only
#print(df)

# High Low percentage here 
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

# Daily percentage / Daily move
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# define a new dataframe / filter only required columns
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

#print(df.head())
# Here is Adj. Close column a feture or a Label ?
# Firstly what is difference b/w Feature and a Label
# Feature: 	A column of Data in input set
# Label: 	This is the output
# Reference: https://stackoverflow.com/questions/40898019/what-is-the-difference-between-feature-and-label

# In our case 'Adj. Close' is a feature

# Creating a Forecast column
forecast_col = 'Adj. Close'

# Fill empty entries with user defined meaningful value
# You can't work NAN data so need to replace the missing data
df.fillna(-9999, inplace=True)

# Predict out of 1% of database hence 0.01 factor is taken
Factor = 0.01
forecast_out = int(math.ceil(Factor * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())
print(df.tail())
