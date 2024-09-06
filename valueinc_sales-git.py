# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:00:46 2024

@author: falih
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

# this is my cheat sheet for data cleaning process using pandas


data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';') # there are semicolon in the csv column

data2 = pd.read_csv('transaction.csv') # to compare with uncleaned dataframe
data2 = pd.read_csv('transaction.csv',sep=';')

data.info()

## playing around with variables

# working with calculations

# finding aggregate values price/transactions

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# math operations on tableau

ProfitPerItem = 21.11 - 11.73

ProfitPerItem = SellingPricePerItem - CostPerItem 

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

# costpertransaction calculation in column

CostPerItem * NumberOfItemsPurchased

#variable =dataframe['column_name]


CostPerItem = data['CostPerItem']

NumberOfItemsPurchased = data['NumberOfItemsPurchased']

SellingPricePerItem = data['SellingPricePerItem']


CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# adding new column to a dataframe 



data['CostPerTransaction'] = CostPerTransaction

data['ProfitPerItem'] = data['SellingPricePerItem'] - data['CostPerItem']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


# data.info()

data['Markup_Percent'] = ((data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']) * 100


data['Markup_Rounded'] = round(data['Markup_Percent'],2)



# combining data fields

# my_name = 'Falih'+' '+'M'

# to joining string column we need to change datatype first

# format query to change DataFrame datatype
data['Year'] = data['Year'].astype(str) # change year column to str
data['Day']= data['Day'].astype(str) # change day column to str
data['Month'] = data2['Month'].astype(str) # change year column to str

# joining the columns to get orderdate column
data['OrderDate'] = data['Year']+ '-' + data['Month'] + '-' + data['Day'] + ' ' + data['Time']

# convert into datetime using pandas

data['OrderDate'] = pd.to_datetime(data['OrderDate'])

# check data type
# data['OrderDate'].info()
    
# date_time2 = pd.DataFrame(date_time)


# method 2 joining in datetime data type


# change the data type to datetime using pandas library

data['OrderDate'] = pd.to_datetime(data['Year']+ '-' + data['Month']+ '-' + data['Day'] + ' ' + data['Time'])


# using iloc to see a specific column

data.iloc[0:4]
data.iloc[-5:] # see last 5 rows
data.head()# brings first five rows
data.iloc[:,2] # brings all rows on the 2nd column

data.iloc[4,2] # brings from data fourth row, second column 


# using split to split client keywords field

# new_var : column.str.split('sep',expand = True) -- this is split format for python


split_col = data['ClientKeywords'].str.split(',',expand = True)


# creating new column in client keywords

data['ClientAge'] = split_col[0]

data['ClientJob'] = split_col[1]

data['ClientExp'] = data['ContractLength'] = split_col[2]


# replace function to remove square brackets in split_col


data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['ContractLength']= data['ContractLength'].str.replace(']','')


# using lower function to change uppercase to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

data.iloc[:,3]

# merging (join) files or table

# bringing other data files

season = pd.read_csv('value_inc_seasons.csv')

season = pd.read_csv('value_inc_seasons.csv',sep=';') # to remove the semicolon value

# merging (joining) files

# merging_files : merge_df = pd.merge(df_old, df_new, on = 'key or column')

data = pd.merge(data, season, on= 'Month') # the 'Month' from seasons file doesnt carried over

# dropping columns, 1 is for column, 0 is for zero

data.info() # checking columns

data = data.drop('ClientKeywords',axis = 1)

data = data.drop('ClientExp',axis=1)

data = data.drop('Day',axis = 1)

data = data.drop('Year',axis = 1)

data = data.drop('Month',axis = 1)

data = data.drop('Markup_Percent',axis = 1)

data = data.drop('Time',axis = 1)




# return number of columns in dataframe

no_of_columns = len(data.columns)

# rearrange DataFrame column
# default = data.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],17]
data = data.iloc[:,[0,1,2,3,4,13,17,5,6,7,8,9,10,11,12,14,15,16]]

# exporting to CSV


# data.to_csv('ValueInc_Cleaned.csv', index = False) # kolom index doesnt included in csv exported file

# doodling around with matplot and groupby

# profit grouped by client age and job

profit_by_job_age = data.groupby(['ClientJob','ClientAge'])['ProfitPerTransaction'].sum()

# plot to bar chart

profit_by_job_age.plot.bar()

# count distinct users by age

count_dist = len(data['UserId'].unique())

user_by_age = data.groupby(['ClientJob','ClientAge'])['UserId'].nunique() #format to count distinct user ids
user_by_age.plot.bar()

# scatterplot sales vs profit

ypt = data['ProfitPerTransaction']
xpt = data['SalesPerTransaction']
plt.scatter(xpt,ypt, color = 'blue')
plt.ylabel("Profit") 
plt.xlabel("Sales") 
plt.show()