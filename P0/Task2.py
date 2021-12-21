"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#First off i will be using pandas , and i will create  dataframes for text and calls
from datetime import datetime
import pandas as pd

# lets creaate variables to dissect to dissect the the the two tables

#First off i will be using pandas , and i will create  dataframes for text and calls
# creates variables to store timestamp, calling numbers, receiving number, and call duration
# convert timestamps to datetime object, and convert durations to integer

times_stamp = [x[2] for x in calls]

calling_number = [x[0] for x in calls]

receiving_number = [x[1] for x in calls]

duration_seconds = [x[3] for x in calls]

#converting timestamp by creating an empty list and appending coverted time to the the list 
times_stamp2 =[]
for x in times_stamp:
    x = datetime.strptime(x,'%d-%m-%Y %H:%M:%S')
    times_stamp2.append(x)

# converting duration into integers
duration_seconds2 =[]
for x in duration_seconds:
    x = int(x)
    duration_seconds2.append(x)
    
#creating a dictionary to store the variables we just created for calls records
my_calls_dict ={'calling_number': calling_number,'receiving_number':receiving_number, 'times_stamp':times_stamp2,'duration_seconds':duration_seconds2 }

#building a dataframe
df = pd.DataFrame(my_calls_dict)

#checking our dataframe
df.head()

# grouping by phone calling number and sums of duration in seconds to find the longest time spend on the phone

grouped_df = df.groupby("calling_number")

#getting the  sums of durations per calling number
maximums = grouped_df.sum()

#resetting index since it is a dataframe as well
maximums = maximums.reset_index()

#extracting the maximum duraration row and storing in the variable longtime (dataframe as well)

long_time = maximums[maximums.duration_seconds == maximums.duration_seconds.max()]

# printing the message with phone number and maximum duration in seconds
for index, row in long_time.iterrows():
    print(row['calling_number'],"spent the longest time,", row['duration_seconds'],"seconds, on the phone during September 2016.")
    
# performed the same operation with receiving number but the value was 47046 wich is less than the calling number with the longest time



# Big O = O(10 N)

# There are 10 steps to solve this problem

#dropping costants 

#==> O(N)


















