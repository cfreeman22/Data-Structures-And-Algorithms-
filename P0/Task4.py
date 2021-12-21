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
#First off i will be using pandas , and i will create  dataframes for text and calls
from datetime import datetime
import pandas as pd

# lets creaate variables to dissect to dissect the the the two tables

#First off i will be using pandas , and i will create  dataframes for text and calls
# creates variables to store timestamp, calling numbers, receiving number, and call duration
# convert timestamps to datetime object, and convert durations to integer

times_stamp = [x[2] for x in calls] # O(n)

calling_number = [x[0] for x in calls] # O(n)

receiving_number = [x[1] for x in calls]# O(n)

duration_seconds = [x[3] for x in calls]# O(n)

#converting timestamp by creating an empty list and appending coverted time to the the list 
times_stamp2 =[]
for x in times_stamp:
    x = datetime.strptime(x,'%d-%m-%Y %H:%M:%S')  # O(n)
    times_stamp2.append(x)

# converting duration into integers
duration_seconds2 =[]
for x in duration_seconds:
    x = int(x)
    duration_seconds2.append(x) # O(n)
    
#creating a dictionary to store the variables we just created for calls records
my_calls_dict ={'calling_number': calling_number,'receiving_number':receiving_number, 'times_stamp':times_stamp2,'duration_seconds':duration_seconds2 } # O(n)

#building a dataframe
df = pd.DataFrame(my_calls_dict)


# datarame for tex numbers
calling_num_text = [x[0] for x in texts] # O(n)

receiving_number_text = [x[1] for x in texts] # O(n)

times_text = [x[2] for x in texts] # O(n)

#converting text times to date time object
times_stamp_text =[]
for x in times_text:
    x = datetime.strptime(x,'%d-%m-%Y %H:%M:%S')
    times_stamp_text.append(x) # O(n)
    
    
#creating a dictionary to store the variables we just created for texts records
my_text_dict ={'calling_number': calling_num_text,'receiving_number':receiving_number_text,'times_stamp':times_stamp_text } # O(n)

#looking for texting time

# building our dataframe for text from the text dictionary 

text_df = pd.DataFrame(my_text_dict)


# checking if telemarketers numbers are found in the receiving column of the calls, as well as the entire text dataframe

# lets filter the calls dataframe for all numbers starting with 140 and store it in the market dataframe

market = df[df.calling_number.str.startswith('140')] # O(n)

# Checking if there is any phone numbers in the receiving columns starting with 140

receiving_calls2 = df[df.receiving_number.str.startswith('140')] # O(n)

receiving_calls2 # No records found in the receiving Column of the calls dataframe

#checking if any number starting with 140 is sending text

sending_text =text_df[text_df.calling_number.str.startswith('140')] # O(n)

sending_text #No records found for this category as well

#checking if any number starting with 140 is Receiving text

receiving_text = text_df[text_df.receiving_number.str.startswith('140')] # O(n)

receiving_text # No record found for this category 

# Getting the column with all numbers starting with 140 into a list named marketers 

marketers = market.calling_number.to_list() # O(n)

# creating a function to print unique a list of possible telemarketers 

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
    

unique(marketers) # O(n)





# Big O = O(18 N)

# There are 18 steps to solve this problem

#dropping costants 

#==> O(N)




















