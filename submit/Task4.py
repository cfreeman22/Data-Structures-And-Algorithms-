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

# creating a set to store unique telephone numbers from the calls and texts lists outgoing and receiving

# i will get a set with phone numbers making calls and sending texts outgoing()
# also another set with phones receiving calls and receiving texts non_tele()
# then , get the difference to extract possible telemarketers

outgoing = set()
non_tele = set()

for call in calls:
    outgoing.add(call[0])
    non_tele.add(call[1])

for text in texts:
    outgoing.add(text[0])
    non_tele.add(text[1])
    
# the difference are possible telemarketers stored in telemarketers 

telemarketers = outgoing.difference(non_tele)
    
print("These numbers could be telemarketers: ",'\n'.join(map(str, sorted(telemarketers)))) 
    


 



 

























