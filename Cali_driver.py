#!/bin/usr/env python3
# Cali_driver.py
# This program is to graph the cleaned data and run statistical analyses
# to check for significance

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates


#############
# Import Data
#############

# Read the CSV file into a dataframe
df = pd.read_csv('clean_data.csv')
print('Read clean_data.csv')

# Make a new column for the years
df['Year'] = pd.DatetimeIndex(df['collision_date']).year
print('Created new column')
print(df.head)

# Count the number of drunk driving collisions each year
year_df = df['Year'].value_counts()
print('Counted the number of drunk driving collisions')

# Convert to a dictionary
collision_dict = year_df.to_dict()
print('Converted to dictionary')
print(collision_dict)


##############
# Create Graph
##############

x_values = list(collision_dict.keys())
y_values = list(collision_dict.values())

# Create bar chart
fig, ax = plt.subplots()
ax.bar(x_values, y_values)
ax.set_xticks(x_values)
ax.set_xticklabels(ax.get_xticks(), rotation = 70)
plt.show()


######################
# Statistical Analysis
######################

# Then it's a matter of running stats to check significance. Going to have to think about
# which test to run