#CaliCollisions

## Introduction:

The purpose of this project is to determine if there is a relationship between the adoption of Uber and the number of incidents of drunk driving collisions. 

## Methods:

The data was created by the California Highway Patrol, but compiled into a SQL database by Alex Gude and uploaded to the open dataset website, kaggle.com.

The first file, CleanCaliData.py takes in the csv files obtained from the "California Traffic Collision Data from SWITRS" data set, created by Alex Gude and submitted to kaggle.com. In order to access this data, the tables first had to be extracted into csv files from a sqlite format. This was done using shell scripting (not shown in repository). The CleanDaliData.py file pulls out the columns of interest and removes rows of unnecessary data, and then exports this data into a new csv file called clean_data.csv.

The second file, Cali_driver.py is used to take the clean data and create a bar chart showing the number of drunk driving collisions per year between 2001 and 2020 and runs a t-test to compare the number of drunk driving collisions between 2001 and 2009, and 2010 through 2019. The data for 2020 was not used as the pandemic caused an outlier in the number of drunk driving collisions in California. 

## Results:

From the bar chart we can see a steady increase in the number of drunk driving collisions before 2010, followed by a decrease in 2010. There was a slight increase in the number of drunk driving collisions following 2010 before dropping in 2020, likely due to the role of the pandemic.

After running a two-sided t-test on the data, a significant difference in the number of drunk driving collisions between 2001 and 2009 and 2010 and 2019 was found. The p-value was found to be 0.001, less than the alpha value of 0.05. This indicates that the number of drunk driving collisions decreased after 2009, which correlates to when the ride-sharing app, Uber, was founded and popularized in California. 

## Discussion:

This data is exciting in that it shows there was a decrease in the number of drunk driving collisions per year after 2009. However, it cannot be overstated that this is merely correlative data and may not be related to the increased popularity of ride-sharing apps. Other reasons for the decrease could be fewer people owning cars, improvement in education around how drinking impairs driving, among others. 

Another point of interest can be seen in the bar chart. The increase in drunk driving incidents between 2010 and 2019 is concerning and may indicate that ride-sharing has not been a factor in reducing collisions. Ride-sharing apps have become more popular in recent years [2] so we would expect the number of drunk driving collisions to decrease over these years. More research should be conducted to investigate these results.

## References

[1] Gude, A. (2020). "California Traffic Collision Data from SWITRS" [data file]. California Highway Patrol [producer]. Kaggle [distributor]. https://www.kaggle.com/alexgude/california-traffic-collision-data-from-switrs

[2] Jiang, J. (2020, July 22). More Americans are using ride-hailing apps. Retrieved February 01, 2021, from https://www.pewresearch.org/fact-tank/2019/01/04/more-americans-are-using-ride-hailing-apps/
