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


##############################
# Read CSVs into one DataFrame
##############################

# Import CSV files into dataframes
partiesDf = pd.read_csv('/Users/tomcairns/Desktop/Random Projects/CaliCollisions/CaliCollisions/parties.csv', low_memory=False)
collisionsDf = pd.read_csv('/Users/tomcairns/Desktop/Random Projects/CaliCollisions/CaliCollisions/collisions.csv', low_memory=False)

# Pull out the columns from collisionsDf that we're interested in
cleanDf1 = pd.DataFrame()
cleanDf1['case_id'] = collisionsDf['case_id']
cleanDf1['date'] = collisionsDf['collision_date']

# Pull out the columns from partiesDf that we're interested in
cleanDf2 = pd.DataFrame()
cleanDf2['case_id'] = partiesDf['case_id']
cleanDf2['party_age'] = partiesDf['party_age']
cleanDf2['party_sex'] = partiesDf['party_sex']
cleanDf2['party_sobriety'] = partiesDf['party_sobriety']

# Merge cleanDf1 and cleanDf2
cleanDf = pd.merge(cleanDf1, cleanDf2, on='case_id', sort=False) # sort=F makes it faster and also doesn't reorder the data
# useful for when we want to look at the date breakdown


#############
# Clean Data
#############

# Remove any rows where party_age = 998 since that means unknown and thus useless info


# Remove any rows where party_sobriety != 'B'; that is the code for someone who had been drinking and is under the influence



###################
# Export Clean Data
###################