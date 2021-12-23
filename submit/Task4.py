"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from datetime import datetime
import operator
import itertools

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# lets creaate variables to dissect to dissect the two tables

#First off i will be using lists of dictionaries for text and calls
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

    
# list for tex numbers
calling_num_text = [x[0] for x in texts] # O(n)

receiving_num_text = [x[1] for x in texts] # O(n)

times_text = [x[2] for x in texts] # O(n)

#converting text times to date time object
times_stamp_text =[]
for x in times_text:
    x = datetime.strptime(x,'%d-%m-%Y %H:%M:%S')
    times_stamp_text.append(x) # O(n)

#creating a dictionary to store the variables we just created for texts records    
text_records = []
for calling_num, receiving_num, times_stamp in zip(calling_num_text, receiving_num_text, times_stamp_text):
    record = {'calling_num':calling_num, 'receiving_num':receiving_num, 'times_stamp':times_stamp}
    text_records.append(record)

    
# sorted list for texts and calls records     
sorted_texts = sorted(text_records, key=operator.itemgetter('calling_num'))

sorted_calls = sorted(call_records, key=operator.itemgetter('calling_num'))


# checking if telemarketers numbers are found in the receiving key of the calls Dictionary , as well as the entire text 

# lets filter the calls list for all numbers starting with 140 and store it in the marketters list

marketers = [x for x in sorted_calls if x['calling_num'].startswith('140')]

receiving_calls_140 = [x for x in sorted_calls if x['receiving_num'].startswith('140')] # O(n)

#receiving_calls_140 # No records found in the receiving key of dictionaries in the calls list

#checking if any number starting with 140 is sending text

sending_text_140 =[x for x in sorted_texts if x['calling_num'].startswith('140')] # O(n)

#sending_text_140 #No records found for this category as well

#checking if any number starting with 140 is Receiving text

receiving_text_140 = [x for x in sorted_texts if x['receiving_num'].startswith('140')] # O(n)

#receiving_text_140 # No record found for this category 

# Getting the list with all numbers starting with 140 into a list named all_marketers 
all_marketers = [key['calling_num'] for key in marketers]


# creating a function to print unique a list of unique Possible telemarketers numbers

def unique(x):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for num in x:
        # check if exists in unique_list or not
        if num not in unique_list:
            unique_list.append(num)
    # print list
    print("These numbers could be telemarketers: ",'\n'.join(map(str, sorted(unique_list)))) 
    


unique(all_marketers)



# Big O = O(21 N)

# There are 21 steps to solve this problem

#dropping costants 

#==> O(N)

























