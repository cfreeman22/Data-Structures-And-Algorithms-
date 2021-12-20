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

# extracting the last call from the dataframe by apply a builtin function max()

last_call = df.times_stamp.max()

#extracting last records
last_record = df[df.times_stamp == last_call]

#extracting calling number from the table
last_record[['calling_number']]

#printing the last record of call from the dataframe
for index, row in last_record.iterrows():
    print("Last record of calls,",row['calling_number'],"calls", row['receiving_number'],"at time", row['times_stamp'],",","lasting",row['duration_seconds'],"seconds")
    
    
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
my_text_dict ={'calling_number': calling_num_text,'receiving_number':receiving_number_text,'times_stamp':times_stamp_text }

#looking for texting time

# building our dataframe for text from the text dictionary 

text_df = pd.DataFrame(my_text_dict)

#extracting first text with time

first_text = min(times_stamp)

first_text = text_df.times_stamp.min()

#isolating the row for the fisr text record

first_text_record = text_df[text_df.times_stamp == first_text]

#printing the message
for index, row in first_text_record.iterrows():
    print("First record of texts,",row['calling_number'],"texts", row['receiving_number'],"at time", row['times_stamp'])















