import pandas as pd
import os

df = pd.read_csv("Sales_Data/Sales_April_2019.csv")
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)

files = [file for file in os.listdir("Sales_Data")]

## create empty df to store all new concatinated data
all_months = pd.DataFrame()

for file in files:
    df = pd.read_csv("Sales_Data/"+ file)
    all_months = pd.concat([all_months, df])

#remove first column in data frame
# what the code is saying df.iloc[row_start:row_end , col_start, col_end]
#all_months = df.iloc[:, 0:]
all_months.to_csv('all_data.csv', index=False)
all_data = pd.read_csv("all_data.csv")

## clean all the data! drop rows of NaN

nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')

#print (all_data.head(10))

## augment data with additional columns
# add month column
## find 'or' and delete it

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] == all_data['Month'].astype('int32')

## converting columns to the correct type

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

# add another column for total sale values
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

# add a city column using .apply() method
# writing a function that grabs the specific data you want. Example grabbing the City and State information
def get_city (address):
    return address.split(',')[1]

def get_state (address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' ' + get_state(x))

#rearrange column to fit appropriately

#cols = list(all_data.columns.values)
#all_data = all_data[cols[0:5] + [cols [-1]] + cols [5:]]

## Task 1: what was the best month for sales? how much was earned that month?

results = all_data.groupby('Month').sum()
import matplotlib.pyplot as plt

#gives range for months, always put extra number for exclusiveness e.g. 13 for 12 months
#months = range(1,13)

#plt.bar(months, results['Sales'])
#plt.show()

# customising graphs
"""
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()
"""
#print (month_data)

## Task 2: what city had the highest number of sales?
import matplotlib.pyplot as plt

results = all_data.groupby('City').sum()

# to ensure data aligns use the (df for df) code
cities = [city for city, df in all_data.groupby('City')]
""""
plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation='vertical', size=6)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City name')
plt.show()
"""

## Task 3: what time should we display ads to maximise likelihood of customer buying products?

# convert date/time into date/time object to easily access parts of date (hour, minute etc)
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute

# plot the data on a line graph
import matplotlib.pyplot as plt

hours = [hour for hour, df in all_data.groupby('Hour')]
"""
plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.grid()
plt.show()
"""

## Take 4: What products are most often sold together?
# how to identify duplicated data, keep=False makes sure you keep all the duplicates
#df = all_data[all_data['Order ID'].duplicated(keep=False)]

# create new column to combine duplicated data
#df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

# drop out instances of the same pair (e.g. rows 2 and 3)
#df = df[['Order ID', 'Grouped']].drop_duplicates()

# using these tools going to count the final number of pairs that exist in df
""""
from itertools import combinations
from collections import Counter

count = Counter()
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

pairs = count.most_common(10)
print (pairs)
"""

## Task 5: what product sold the most? And why?

product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']
#print (product_group)

import matplotlib.pyplot as plt

products = [product for product, df in product_group]
""""
plt.bar(products, quantity_ordered)
plt.xticks(products, rotation='vertical', size=8)
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.show()
"""
## add second y-axis to prove hypothesis of why?
# use subplots

prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color='b')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price of Product', color='r')
ax1.set_xticklabels(products, rotation='vertical', size=8)
#plt.show()




#print (prices)


