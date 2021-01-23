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
partiesDf = pd.read_csv('parties.csv', usecols=['case_id', 'party_age', 'party_sex', 'party_sobriety'])
print('Parties table read')
collisionsDf = pd.read_csv('collisions.csv', usecols=['case_id', 'collision_date'])
print('Collisions table read')
print('Data imported')

# Merge partiesDf and collisionsDf
cleanDf = pd.merge(partiesDf, collisionsDf, on='case_id', sort=False) # sort=F makes it faster
print('Data merged')
print(cleanDf.head)

#######################
# Clean and Export Data
#######################

totalLength = len(cleanDf.index)
print('Total Length is: ', totalLength)

# Remove any rows where party_sobriety is not B; B is under the influence
cleanDf.drop(cleanDf[cleanDf['party_sobriety'] != 'B'].index, inplace=True)

# Remove any rows with unknown values in age or sex columns
cleanDf = cleanDf[cleanDf['party_age'].notna()]
cleanDf = cleanDf[cleanDf['party_sex'].notna()]

print(cleanDf.head)

###################
# Export Clean Data
###################

# Write the cleanDf into a new CSV file
cleanDf.to_csv('clean_data.csv')
print('Done')

