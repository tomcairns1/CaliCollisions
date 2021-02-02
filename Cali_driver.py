#!/bin/usr/env python3
# Cali_driver.py
# This program is to graph the cleaned data and run statistical analyses
# to check for significance

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
from scipy import stats


#############
# Import Data
#############

# Read the CSV file into a dataframe
df = pd.read_csv('clean_data.csv')

# Make a new column for the years
df['Year'] = pd.DatetimeIndex(df['collision_date']).year

# Count the number of drunk driving collisions each year
year_df = df['Year'].value_counts()

# Convert to a dictionary
collision_dict = year_df.to_dict()


##############
# Create Graph
##############

x_values = list(collision_dict.keys())
y_values = list(collision_dict.values())

# Create bar chart
fig, ax = plt.subplots()
ax.bar(x_values, y_values)

# Axes and chart labels
ax.set_xticks(x_values)
ax.set_xticklabels(ax.get_xticks(), rotation = 70)
ax.set_ylabel('Drunk Driving Collisions')
ax.set_xlabel('Year')
plt.axvline(x=2009.5, color='red', label='Founding of Uber')
plt.title('Drunk driving collisions in California per year')

# Display chart
plt.legend()
plt.show()


######################
# Statistical Analysis
######################

# Split the data into lists of pre and post uber (founded in 2009, in Cali in 2010)
pre_uber = list(filter(lambda elem: elem[0] < 2010, collision_dict.items()))
pre_uber = [i[1] for i in pre_uber]
post_uber = list(filter(lambda elem: elem[0] in range(2010, 2020), collision_dict.items()))
post_uber = [i[1] for i in post_uber]

# Run a t-test on the data
stats = stats.ttest_ind(pre_uber, post_uber)
print(f'The t-statistic is: {round(stats.statistic, 3)}')
print(f'The p-value is: {round(stats.pvalue, 3)}')
