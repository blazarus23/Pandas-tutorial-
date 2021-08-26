#### PANDAS TUTORIAL ####
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)

df = pd.read_csv('/Users/brendanlazarus/PycharmProjects/PandasTut/data/survey_results_public.csv', index_col = 'Respondent')
schema_df = pd.read_csv('/Users/brendanlazarus/PycharmProjects/PandasTut/data/survey_results_schema.csv', index_col = 'Column')
"""
## GET DF INFORMATION
print(df.shape) = (rows, columns) of dataset
print(df.info()) = provides range index, no. of columns, data types of columns etc

## PRINT DATA FROM COLUMNS
print(df['Country'] = prints the data from that column
print(df.columns) = gets the name of all the column names

## .ILOC
print(df.iloc[0]) = access data from a particular row location
print(df.iloc[0,1],[1]) = accesses rows 0 and 1 from column 1 * CAN'T use col names

## .LOC
print(df.loc[0]) = prints data from 1st row
print(df.loc[[0,1], 'Hobbyist']]) = searches df by labels (indexes). * CAN use col names
print(df['col_name'].value_counts()) = counts data occurrences in columns e.g. 'Yes' or 'No'
print(df['col_name'].unique()) = see all unique values in a column
print(df.loc[0:3, 'Hobbyist']) = gets data from first 3 rows ** inclusive **
print(df.loc[0:3, 'Hobbyist':'Employment']) = gets data from first 3 rows and selected columns

## INDEXES
df.set_index('col_name', inplace=True) = changes index to specified column. inplace saves changes to df
df.reset_index() = resets index back to default 
index_col = 'col_name' in the read_csv function sets index to that column (see above)
df.sort_index() = sort index alphabetically
df.sort_index(ascending=False) = sort index reverse alphabetical order

## FILTERING
filt = (df['col_name'] == 'string') = filtering data to access particular string
print(df.loc[filt, 'col_name]) = using loc means we can filter rows and columns
print(df[filt]['col_name]) = access data from filter and specific column only

filt = (df['col_name'] == 'string') & (df['col_name1'] == 'string1') = selecting 2 conditions with 'AND' 
filt = (df['col_name'] == 'string') | (df['col_name1'] == 'string1' = selecting 2 conditions with 'OR'
print(~filt) = the 'tilde' negates the filter and prints everything else 

## CHANGING COLUMN DATA
df.columns = ['first_name', 'last_name', 'email'] = changing column names using a list
df.columns = [x.upper() = for x in df.columns] = makes all column names UPPER CASE. Use lower for reverse
df.columns = df.columns.str.replace('_', ' ') = replaces underscores with a space
df.rename(columns = {"old_name": "new_name", "old_name": "new_name"}, inplace=True) = renaming multiple columns

## CHANGING ROW DATA
df.loc[2] = ['John', 'Smith', johnsmith@email.com'] = changes data in specific location for all rows
df.loc[2, ['col_name, 'col_name']] = ['new_name', 'new_name'] = change only specific columns

## MAKING CHANGES TO STRINGS
df['string'] = df['string'].str.lower() = changes the string to lower case
df['string'].apply(len) = gets the no. of characters of a string

def update_email(email):
    return email.upper()
    
df['email'] = df['email'].apply(update_email) = applies the changes in df using the function
df['email'] = df['email'].apply(lambda x: x.lower()) = lambda is an anonymous function

df.applymap(len) = gives you the length of every character in the dataframe. Different to .apply()
df['Hobbyist'] = df['Hobbyist'].replace({'Yes': True, 'No': False}) = replaces values with only 2 options
df['Hobbyist'] = df['Hobbyist'].replace({'Yes': True, 'No': False}) = replaces values in data series with more than 2 options

## CREATING NEW COLUMNS, DROPPING COLUMNS, SPLITTING COLUMNS
df['full_name'] = df['first'] + ' ' + df['last'] = creates new column with full name (and space between names)
df.drop(columns=['col_name']) = drops a column
df.drop(columns=['col_name', 'col_name2]) = drops multiple columns 

df['full_name'].str.split(' ') = separates data in column into 2 (default is space) 
df['full_name'].str.split(' ', expand=True) = expand assigns data into 2 different columns
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True) = assigns expanded data into new columns

## MAKING CHANGES TO ROWS OF DATA, ADDING IN ROWS
df.append({'first': 'Tony'}, ignore_index=True) = adding in row of data. ignore_index=True adds in incomplete data series
df.append(df2, ignore_index=True) = appends 2 data frames together. Warning may appear if columns don't align

df.drop(index=0) = drops a row of data (e.g. 1st row dropped)
df.drop(index=df[df['last'] == 'Doe'].index) = drops rows based on a condition (e.g. last name = to Doe)
** to make a look nicer and easier to write use:
filt = df['last'] == 'Doe'
df.drop(index = df[filt].index)

## SORTING VALUES OF DATA
df.sort_values(by='last') = sort ascending order
df.sort_values(by='last', ascending=False) = sort descending value
df.sort_values(by=['last', 'first]) = sorts by last name 1st then first name 2nd
df.sort_values(by=['last', 'first], ascending=[False, True]) = sorts values in specified asc/desc order
    # last name is descending, first name is ascending

## PRINTING LARGEST/SMALLEST  
df['SalaryUSD'].nlargest(10) = prints 10 largest numbers (but only shows the parameter)
df.nlargest(10, 'SalaryUSD') = prints 10 largest numbers showing whole df
df.nsmallest(10, 'SalaryUSD') = prints 10 smallest numbers showing whole df

## USING AGGREGATE FUNCTIONS 
df.median() = gets the median of variables 
df['SalaryUSD'].median() = gets the median of specified variable
df.describe() = provides summary statistics of variables 
df['SalaryUSD'].count() = count of values in column (ignores NaN)
df['Country'].value_counts() = counts the number of instances in a column (e.g. no. of Countries)
df['SocialMedia'].value_counts(normalize=True) = normalize provides % of 

## USING GROUPBY FUNCTION 
country_grp = df.groupby(['Country']) = groups data by specified column (e.g. Country)
country_grp.get_group('United States') = gets data for a specific group (e.g. Country)
country_grp['SocialMedia'].value_counts() = gets the social media for every country
country_grp['SocialMedia'].value_counts().loc['Australia'] = gets social media for 1 country (e.g. Australia)

country_grp['SalaryUSD'].median() = gets the median salary for every country
country_grp['SalaryUSD'].median().loc['Australia']  = gets the median salary for 1 country

country_grp['SalaryUSD'].agg(['median, 'mean']) = .agg means you can use multiple aggregate functions

## CLEANING DATA
df.dropna(axis='index', how='any') = default drop NaN values in a row
    axis = 'index' for rows or 'columns' for columns
    how = 'any' for a row with any missing values or 'all' for when all values are missing
df.dropna(axis='index', how='any', subset=['email']) = drop NaN values in a row for a specific column

df.replace('NA', np.nan, inplace=True) = replace custom missing values with specific string
df.replace('Missing', np.nan, inplace=True) = as line 127

df.isna() = finds NaN as boolean values in df
df.fillna('Missing') = changes NaN values to specified label (e.g. Missing or 0)

df['age'] = df['age'].astype(int) = converting a variable to an integer value
df['age'] = df['age'].astype(float) = converting a variable to an float value * USE WHEN NaN VALUES EXIST

# To convert different missing values to NaN in a df create a list first then pass it into the read csv code
na_vals = ['NA', 'Missing'] = create a list
df = pd.read_csv("file_name.csv", index_col = 'first_col', na_values = na_vals)

## DATES AND TIME SERIES DATA
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior = date time format codes
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects = pandas date offset codes

# to convert to datetime when reading in files. Make sure to import datetime as above
d_parser = lamba x: datetime.strptime(x, '%Y-%m-%d %I-%p')
data = pd.read_csv("file_name.csv", parse_dates=['Date'], date_parser=d_parser) 

date['Date'].min() = gets the earliest datetime
date['Date'].max() = gets the latest datetime
date['Date'].max() - date['Date'].min() = the time difference between 2 dates

data.loc[0, 'Date'].day_name() = to get the day name of a single index
data['Date'].dt.day_name() = to get the day name of all the indexes

filt = (data['Date'] >= '2020') = filtering data by year 2020
data.loc(filt)

filt = (data['Date'] >= '2019') & (data['Date'] < '2020') = filters the data for year 2019
filt = (data['Date'] >= pd.to_datetime('2019-01-01') & (data['Date'] < pd.to_datetime('2020-01-01')) = filters by exact date

# To filter through years much easier, set date to the index
data.set_index('Date')
data['2019'] = prints data from year 2019
data['2020-01':'2020-02'] = prints data from Jan & Feb 2020

data['2020-01':'2020-02']['Close'].mean() = gets average 'close' price for that time frame
data['2020-01-01']['High'].max() = get the highest value for the first day in Jan

df['High'].resample('D').max() = resamples the data and collates by day or week or month (see offset codes) 

data.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})
    = resampling by week and using multiple agg functions

### READING & WRITING DATA FROM DIFFERENT SOURCES
df.to_csv('file_name.csv') = outputs df to new csv file
to read excel files need to pip install:
    xlwt = write to older excel formats
    openpyxl = write to newer excel formats
    xlrd = read excel files
df.to_excel('file_name.xlsx') = outputs df to new excel file
"""

high_salary = (df['ConvertedComp'] > 70000)
#print(df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

""" Create a list of countries we want to see"""
countries = ['United State', 'India', 'United Kingdom', 'Germany', 'Canada']

""" Create a filter on the column that includes our list then print"""
filt = (df['Country'].isin(countries))
#print(df.loc[filt, 'Country'])

# create a filter that contains certain string
python_users = (df['LanguageWorkedWith'].str.contains('Python', na=False)) # na=False sets a fill value for NaN's
#print(df.loc[python_users, 'LanguageWorkedWith'])

# change column name
df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)

# change Hobbyist column values (Yes/No) to (True/False).
    # df['col_name'] = CODE sets the changes to the df
    # if your column has more than 1 value (e.g. Yes/No/Not sure) then use .replace
df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})

# sort df by country & salary in ascending and descending order
df.sort_values(by=['Country','SalaryUSD'], ascending=[True, False])
#print(df[['Country', 'SalaryUSD']].head(50))

# find the 10 largest salaries in df
#print(df['SalaryUSD'].nlargest(10))
#print(df.nlargest(10, 'SalaryUSD'))

# get the median salary
#print(df['SalaryUSD'].median())

# get the value count for a specific column
#print(df['SocialMedia'].value_counts())

# identify number of social media for 1 country
country_grp = df.groupby(['Country'])
#print(country_grp.get_group('United States')) # gets a specific group

# Another method to print data
#print(df.loc[countries_media]['SocialMedia'].value_counts())

# now to look at all the social media for every country
#print(country_grp['SocialMedia'].value_counts())

# to look at the data for one specific index
#print(country_grp['SocialMedia'].value_counts().loc['Australia'])

# Use multiple aggregates at once
#print(country_grp['SalaryUSD'].agg(['median', 'mean']).loc['Australia'])

# Identify the number of people in a country that uses Python
lang = df['Country'] == 'Australia'
# this will tell us the total number of people that use Python in 1 country
#print(df.loc[lang]['LanguageWorkedWith'].str.contains('Python').sum())

# CANNOT USE ABOVE WITH A SERIESGROUPBY (E.G. 'COUNTRY') USE APPLY METHOD INSTEAD
# This will give us the number of python users in ALL countries
#print(country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()))

# get the % of Python users from each country
# creates a variable with the number of respondents from each country
countries_count = df['Country'].value_counts()
#print(countries_count)

# creates variable with the number of python users from each country
countries_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
#print(countries_python)

# Concatinate/Merge the dataframes together. Setting the axis to 'columns' means the data won't concat by rows
total_python_users = pd.concat([countries_count, countries_python], axis='columns')
#print(total_python_users)

# rename columns to reflect new df
total_python_users.rename(columns ={"Country": "NumRespondents", "LanguageWorkedWith": "PythonUsers"}, inplace=True)

# create variable for the percentage of python users for each country
total_python_users['PctPythonUsers'] = (total_python_users['PythonUsers'] / total_python_users['NumRespondents']) * 100
#print(total_python_users)

# Find the average of years coding experience
#print(df['YearsCode'].unique())
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)
df['YearsCode'].replace('More than 50 years', 51, inplace=True)
df['YearsCode'] = df['YearsCode'].astype(float)
#print(df['YearsCode'].mean())
#print(df['YearsCode'].median())

### WORKING WITH DATES AND TIME SERIES DATA
d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p')
data = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)

# Convert to date time
#data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d %I-%p')

# To get the day name of a single index
#print(data.loc[0, 'Date'].day_name())

# To get the day name of all the indexes
#print(data['Date'].dt.day_name())

# creating a new column with the above code
data['DayOfWeek'] = data['Date'].dt.day_name()

# creating a filter to sort by year
recent_years = (data['Date'] >= '2020')
#print(data.loc[recent_years])

# set the index as the date to use the following filters
data.set_index('Date', inplace=True)

# get the avg close for the two months
avg_close = (data['2020-01':'2020-02']['Close'])
#print(avg_close.mean())

# get the highest value for the first day in Jan
#print(data.loc['2020-01-01']['High'].max())

# resamples
highs = (data['High'].resample('D').max())
#print(highs['2020-01-01'])

plt.plot(highs)
#plt.show()

#print(data)