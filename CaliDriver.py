#!/bin/usr/env python3
# CaliDriver.py

'''
This data set is for car collisions in california from 2001-2020
We're looking to see if the number of drunk driving crashes decreased after Uber became a thing
Also look at the demographics, like based on age brackets or sex, etc
'''

#################
# Import Packages
#################

import pandas as pd
import matplotlib


##########################################
# Read CSV into a DataFrame and clean data
##########################################

df = pd.read_csv('/Users/tomcairns/Desktop/Random Projects/CaliCollisions/CaliCollisions/parties.csv', low_memory=False)

print(head(df))


###################
# Export Clean Data
###################