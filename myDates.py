#META 2/2/2018
#Working with Dates.  Plotting with Dates
#note: either display part 1 or part 0

import matplotlib.pyplot as plt
"""
#----------------------------------- 1. Dates with panda -------------------------------------------------------------
#
# date type and conversions
#
#---------------------------------------------------------------------------------------------------------------------
import pandas as pd

#pandas today
myToday = pd.datetime.today() #type datetime.datatime
print(type(myToday))
myToday2 = pd.datetime.today().strftime('%Y %m %d') #type string
print(type(myToday2))
myToday3 = pd.datetime.strptime(myToday2, '%Y %m %d')
print(type(myToday3))

print()
print('1. Dates with panda')

###load data with dates
#--APM dataset: hourly server metrics

#load and format data - pandas dataframe
data = pd.read_csv("data/myDates_server_metrics.csv")
print('data shape: ', data.shape)
print ('data columns: ', data.columns)
print('data types: ', data.dtypes)
print("*** Notice: columns with dates came in as type 'object' ***")


#convert type object to type datetime, using pandas date format
data['myDate_converted'] = pd.to_datetime(data['myDate'])
data['myDatetime_converted'] = pd.to_datetime(data['myDatetime'])
print(data['myDate_converted'].head(1))
print("type: ", data['myDate_converted'].dtype)
print(data['myDatetime_converted'].head(1))
print("type: ", data['myDatetime_converted'].dtype)


#Q: Can we plot with dates in such format?

#data prep - filtered
data_filtered = data[data.Host=='tdp03']
#x=data_filtered.index # replace with date
dates = data_filtered['myDatetime_converted']
y=data_filtered['IntegerMax']
print ("type for dates: ", dates.dtype)

#----------------------------------- 1a. Plotting with Dates ---------------------------------------------------------
#
# Visualizing the Data - plot with dates
#
#---------------------------------------------------------------------------------------------------------------------

print('1a. Plotting with dates')
print ("--Plot_dates() basic")
### Example 1a:1 - basic plot_dates()
plt.figure(figsize=[18,10])
plt.plot_date(dates, y, 'b-')
plt.title("GC Heap, Bytes in Use")
plt.xlabel("Date")
plt.ylabel("Max Bytes in Use")
plt.grid()

print ("Nice default plot using plot_dates() - with dates only, no hour")

print ("--Plot_dates() with plt.subplots()")
### Example 1a:2 - as before, but using fig and ax
#src https://matplotlib.org/examples/pylab_examples/date_demo_convert.html
#src https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes

fig, ax = plt.subplots(figsize=(18,10))
ax.plot_date(dates, y, 'b-')
ax.set_title("GC Heap, Bytes in Use")
ax.set_xlabel("Date")
ax.set_ylabel("Max Bytes in Use")
ax.grid(True)

print ("Nice plot using plt.subplots() - still with dates only, no hour")

print ("--Plot_dates() - display format date+hour")
### Example 1a:3 - as before, using fig and ax + display hour
from matplotlib.dates import DateFormatter

fig, ax = plt.subplots(figsize=(18,10))
ax.plot_date(dates, y, 'b-')
#add hour
ax.xaxis.set_major_formatter(DateFormatter("%Y/%m/%d %H:%M"))
fig.autofmt_xdate()
ax.set_title("GC Heap, Bytes in Use")
ax.set_xlabel("Datetime")
ax.set_ylabel("Max Bytes in Use")
ax.grid(True)

print ("Nice plot using plt.subplots() - with dates and hour")

"""
#----------------------------------- 0. Dates - even simpler ----------------------------------------------------------
#
# date type and conversions
#
#---------------------------------------------------------------------------------------------------------------------
print('0. Dates - even simpler')

### plot with dates: 2 numpy arrays
#refer https://stackoverflow.com/questions/11376080/plot-numpy-datetime64-with-matplotlib
import numpy as np
from datetime import datetime

print ("--Plot_dates() with type string")
### Example 0 - basic plot_dates() with strings
dates2=np.array(["2011-11-13", "2011-11-14", "2011-11-15", "2011-11-16", "2011-11-19"])
y2=np.array([1, 2, 3, 4, 5])
plt.plot_date(dates2, y2) #type str is totally fine turns out - draws blue dots
print("type: ", type(dates2[0]))
print ("Plot_dates() works even with dates as string.  No need to convert ty type 'datetime'")

print ("Issue: dates are not plotted to scale")
#function to convert from string to date
dates2[4]="2011-11-17"
def convertStr2Date(x):
    return x.astype(datetime)

dates2_converted = np.apply_along_axis(convertStr2Date, axis=0, arr=dates2)
print("type: ", type(dates2_converted[0]))
plt.plot_date(dates2_converted, y2) #still string for some reason?  redraws orange dots over blues
plt.title("Plot dates: with strings")
plt.xlabel("Date")
print ("... nor in the right order")
print ("So, plotting with string dates is only good if data is final and not requiring any changes")


print ("--Plot_dates() with type datetime")
### example 0a
#https://stackoverflow.com/questions/14946371/editing-the-date-formatting-of-x-axis-tick-labels-in-matplotlib

#from datetime import datetime
from matplotlib.dates import DateFormatter

dates3 = [datetime(2012, 1, i + 3) for i in range(10)]
y3 = [5, 6, 4, 3, 7, 8, 1, 2, 5, 4]
fig, ax = plt.subplots()
ax.plot(dates3, y3)
#limit to displaying Day only
myFmt = DateFormatter("%d")
ax.xaxis.set_major_formatter(myFmt)
ax.set_title("Plot dates: display day only")
ax.set_xlabel("Day")
#rotate date labels automatically
fig.autofmt_xdate()
print ("Plotting with type datetime: flexible day formatting!")

print ("--Plot_dates() with type int converted to datetime")
#example 0b
#https://stackoverflow.com/questions/28385184/how-to-set-the-xticklabels-for-date-in-matplotlib
import datetime as DT
import matplotlib.dates as mdates

dates4 = [20070102, 20070806, 20091208, 20111109, 20120816, 20140117, 20140813]
y4 = [-0.5, -0.5, -0.75, -0.75, -0.5, -1.25, -1.25]
print("type: ", type(dates4), type(dates4[0])) #type list of datetimes
dates4_formatted = [DT.datetime.strptime(str(int(date)), '%Y%m%d') for date in dates4]
print("type: ", type(dates4_formatted), type(dates4_formatted[0])) #type list of datetimes

fig, axes = plt.subplots(1, 1, figsize=(16, 9), dpi=100)

line1, = axes.plot(dates4_formatted, y4, lw=2, marker='*', color='r')
axes.legend([line1],['Values'],loc=1)
axes.grid()
axes.set_title("Plot dates: with custom X ticks")
axes.set_xlabel('Date')
axes.set_ylabel('Values')
#set y ticks - a custom list
yticks = [-2.0,-1.75,-1.5,-1.25,-1.0,-0.75,-0.5,-0.25,0.0]
axes.set_yticks(yticks)
axes.set_yticklabels(["$%.2f$" % y for y in yticks]);
#format date
xfmt = mdates.DateFormatter('%Y-%m-%d')
axes.xaxis.set_major_formatter(xfmt)
#set x ticks
axes.set_xticks(dates4_formatted)
plt.xticks(rotation=25)

print ("Plotting with type datetime: custom Xticks and up to scale")


plt.show()


# todo: read from myDates data files
"""
data['datetime_str'] = data['datetime'].apply(lambda x: datetime.strftime(x, '%Y %m %d %H %M %S'))
data['datetime_formatted'] = data['datetime_str'].apply(lambda x: datetime.strptime(x, '%Y %m %d %H %M %S'))

print (data.dtypes)
print (data.head())
"""