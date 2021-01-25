# CaliCollisions

## Introduction:

The purpose of this project is to determine if there is a relationship between the adoption of Uber and the number of incidents of drunk driving collisions. 

## Methods:

The first file, CleanCaliData.py takes in the csv files obtained from the "California Traffic Collision Data from SWITRS" data set, created by Alex Gude and submitted to kaggle.com. In order to access this data, the tables first had to be extracted into csv files from a sqlite format. This was done using shell scripting (not shown in repository). The CleanDaliData.py file pulls out the columns of interest and removes rows of unnecessary data, and then exports this data into a new csv file called clean_data.csv.

The second file, Cali_driver.py is used to take the clean data and create a bar chart showing the number of drunk driving collisions per year between 2001 and 2020. 
