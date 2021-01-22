#!/bin/usr/env python3
# CaliDriver.py
# This program is to clean the data from the parties and collisions table and to
# export it into a csv file

#################
# Import Packages
#################

import pandas as pd


##############################
# Read CSVs into one DataFrame
##############################

# Import CSV files into dataframes
print('begin')
partiesDf = pd.read_csv('parties.csv', low_memory=False)
print('Parties table read')
collisionsDf = pd.read_csv('collisions.csv', low_memory=False)
print('Collisions table read')
print('Data imported')

# Pull out the columns from collisionsDf that we're interested in
cleanDf1 = pd.DataFrame()
cleanDf1['case_id'] = collisionsDf['case_id']
cleanDf1['date'] = collisionsDf['collision_date']
print('CleanDf1 obtained')

# Pull out the columns from partiesDf that we're interested in
cleanDf2 = pd.DataFrame()
cleanDf2['case_id'] = partiesDf['case_id']
cleanDf2['party_age'] = partiesDf['party_age']
cleanDf2['party_sex'] = partiesDf['party_sex']
cleanDf2['party_sobriety'] = partiesDf['party_sobriety']
print('CleanDf2 obtained')

# Merge cleanDf1 and cleanDf2
cleanDf = pd.merge(cleanDf1, cleanDf2, on='case_id', sort=False)
# sort=F makes it faster and also doesn't reorder the data useful for when we
# want to look at the date breakdown
print('Data merged')

#######################
# Clean and Export Data
#######################

# Remove any rows where party_age = 998; 998 is an unknown age
# Remove any rows where party_sobriety is not B; B is under the influence
for i, row in cleanDf.iterrows():
    if row['party_age'] == '998' or row['party_sobriety'] != 'B':
        cleanDf.drop(index=i)

# Write the cleanDf into a new CSV file
cleanDf.to_csv('clean_data.csv')





###################
# Export Clean Data
###################