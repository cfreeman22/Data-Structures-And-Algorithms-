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

# creating  a dictionary phone_dict to capture the the phone numbers and time spent
# we note that calling numbers might also be at receiving end 
# capturing calling numbers and time spent

phone_dict={}
for call in calls:
    phone_dict[call[0]] = phone_dict.get(call[0],0) + int(call[3])
    
    
    
# capturing receiving numbers and time spent and updating the phone_dict

for call in calls:
    phone_dict[call[1]] = phone_dict.get(call[1],1) + int(call[3])
    phone_dict.update()
    

# extrating the longest time spent using the max() built in function and itemgetter from the opreator module  

longest_time = max(phone_dict.items(), key=operator.itemgetter(1))

# print the message with the longest time spent

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(*longest_time))

























