"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#First off  i will create  dictionaries for text and calls
from datetime import datetime
from operator import itemgetter


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


# extracting the last call by apply a builtin function max()

last_call = max(call_records, key=itemgetter('times_stamp'))


# printing the last record of call from the dataframe

print("Last record of calls,",last_call['calling_num'],"calls", last_call['receiving_num'],"at time", last_call['times_stamp'],",","lasting",last_call['duration_seconds'],"seconds")

# We will repeat the same thing for text dataset


calling_num_text = [x[0] for x in texts]

receiving_number_text = [x[1] for x in texts]

times_text = [x[2] for x in texts]

#converting text times to date time object
times_stamp_text =[]
for x in times_text:
    x = datetime.strptime(x,'%d-%m-%Y %H:%M:%S')
    times_stamp_text.append(x)


#creating a dictionary to store the variables we just created for texts records
text_records = []
for calling_num, receiving_num, times in zip(calling_num_text, receiving_number_text, times_stamp_text):
    record = {'calling_num':calling_num, 'receiving_num':receiving_num, 'times_stamp':times}
    text_records.append(record)
    
#looking for texting time



#extracting first text with time

#first_text = min(times_stamp_text)

first_text = min(text_records, key=itemgetter('times_stamp'))


#printing the message
print("First record of texts,",first_text['calling_num'],"texts", first_text['receiving_num'],"at time", first_text['times_stamp'])




# Big O = O(15 N)

# There are 15 steps to solve this problem

#dropping costants

#==> O(N)
