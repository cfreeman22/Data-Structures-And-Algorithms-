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
    
    
from operator import itemgetter
from datetime import datetime
import itertools
import operator

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

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
call_records = []
for calling_num, receiving_num, times_stamp, duration_seconds in zip(calling_number, receiving_number, times_stamp2, duration_seconds2):
    record = {'calling_num':calling_num, 'receiving_num':receiving_num,'times_stamp':times_stamp,'duration_seconds':duration_seconds}
    call_records.append(record)

    
# Let group the calls and sum the durations in seconds for every calling number
#first lest sort it for easy grouping
sorted_calls = sorted(call_records, key=operator.itemgetter('calling_num'))

grouped_list = []
for key, items in itertools.groupby(sorted_calls, operator.itemgetter('calling_num')):
    grouped_list.append(list(items))    
    
    
    
    
# let's extract calling number group by call duration and get the longest time
duration = []
for item in grouped_list:
    call_num = item[0]['calling_num']
    size = len(item)
    total =0 
    for k in range(size):
        total += (item[k]['duration_seconds'])
    duration.append((call_num, total))
    
    
# longest time

long = max(duration,key=operator.itemgetter(1))

print(f"{long[0]} spent the longest time, {long[1]} seconds, on the phone during September 2016.")


# performed the same operation with receiving number but the value was 47046 wich is less than the calling number with the longest time

# Big O = O(8 N)
# Big O (n^2)
# There are 10 steps to solve this problem

#dropping costants 

#==> O(N^2)




























