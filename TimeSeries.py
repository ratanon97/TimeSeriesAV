#-------------------------------------------------------------------------------
#Time Series Forecasting Using Python
#https://courses.analyticsvidhya.com/courses/take/creating-time-series-forecast-using-python/texts/6133032-getting-the-system-ready-and-loading-data
#-------------------------------------------------------------------------------
#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import re
from datetime import datetime    # To access datetime 
from pandas import Series        # To work on series 
#-------------------------------------------------------------------------------
#Set working directory 
print(os.getcwd())
os.chdir("C:\\Users\\KOMSUN\\Documents\\GitHub\\TimeSeriesAV\\Data Sources")
#-------------------------------------------------------------------------------
#Data Preparation
#Create training and test set objects
train=pd.read_csv("Train_SU63ISt.csv") 
test=pd.read_csv("Test_0qrQsBZ.csv")
train_original=train.copy() #Make a copy to not lose the original dataset
test_original=test.copy()
#Checking the data structures of the dataset
train.columns
test.columns #Check index of columns
#ID is the unique number given to each observation point.
#Datetime is the time of each observation.
#Count is the passenger count corresponding to each Datetime.
train.dtypes
test.dtypes #Check data types for each column
train.shape
test.shape #Return a tuple of the number of rows and columns
#Feature Extraction
#Hypothesis 1: There will be an increase in the traffic as the years pass by.
#Extract the time and date from the Datetime, convert the Datetime column into a Datetime format
train['Datetime'] = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
test['Datetime'] = pd.to_datetime(test.Datetime,format='%d-%m-%Y %H:%M') 
test_original['Datetime'] = pd.to_datetime(test_original.Datetime,format='%d-%m-%Y %H:%M') 
train_original['Datetime'] = pd.to_datetime(train_original.Datetime,format='%d-%m-%Y %H:%M')
#Extract the year, month, day and hour
for i in (train, test, test_original, train_original):
    i['year']=i.Datetime.dt.year 
    i['month']=i.Datetime.dt.month 
    i['day']=i.Datetime.dt.day
    i['Hour']=i.Datetime.dt.hour 
#Hypothesis 2: Traffic on weekdays will be more as compared to weekends/holidays.
train['day of week']=train['Datetime'].dt.dayofweek #Implement day of week
temp = train['Datetime'] #Values of 5 and 6 represents that the days are weekend.
def applyer(row):
    if row.dayofweek == 5 or row.dayofweek == 6:
        return 1
    else:
        return 0 
temp2 = train['Datetime'].apply(applyer) 
train['weekend']=temp2
#Plot Time Series
#sns.set_style("darkgrid")
#fig, ax = plt.subplots() #Put the whole graph in a "subplot" but will still give a normal graph #HACK
#fig.set_size_inches(11.7,8.27)
train.index = train['Datetime'] # indexing the Datetime to get the time period on the x-axis. 
df=train.drop('ID',1)           # drop ID variable to get only the Datetime on x-axis. 
ts = df['Count'] 
plt.figure(figsize=(16,8)) 
plt.plot(ts, label='Passenger Count') 
plt.title('Time Series') 
plt.xlabel("Time(year-month)") 
plt.ylabel("Passenger count") 
plt.legend(loc='best')
