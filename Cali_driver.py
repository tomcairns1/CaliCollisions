#!/bin/usr/env python3
# Cali_driver.py
# This program is to graph the cleaned data and run statistical analyses
# to check for significance

import pandas as pd 
import matplotlib.pyplot as plt


#############
# Import Data
#############

df = pd.read_csv('clean_data.csv')

# Want to bin the dates by year and have counts of drunk driving collisions for each

# Then I can create a bar chart that shows the number of drunk driving incidents every year

# Then it's a matter of running stats to check significance. Going to have to think about
# which test to run