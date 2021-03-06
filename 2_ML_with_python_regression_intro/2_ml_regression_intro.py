# Machine Learning: Regression Intro
# Using continous data, like stock prices 

import pandas as pd
import quandl

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

print(df)
