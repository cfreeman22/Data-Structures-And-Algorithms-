"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from datetime import datetime
import operator
import itertools
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# lets creaate variables to dissect to dissect the two tables


    
#Find all of the area codes and mobile prefixes initiated by "(080)" area code
calls_by_080 = [call for call in calls if call[0].startswith('(080)')]

# lets filter for fixed lines that begings with 0 called by "(080)" area code

fix_lines = [call for call in calls_by_080 if call[1].startswith("(0")]

# lets filter calling numbers starting with (080) from the calls into a list split the list at the closing parentheses

all_fix_lines = [x[1].split(')') for x in fix_lines]

 
# extracting the area code and joining the parentheses to have area code in brackets 
all_fix_lines_codes = [x[0] + x[0].join(')') for x in all_fix_lines]

# repeating the same proccess for calls initiated by area code (080) to mobile numbers starting with 7, 8, 9

mobile_num_codes = [x[1][:4] for x in calls_by_080 if " " in x[1]]

 
# creating a list of all calls initiated by (080) to all area codes 
all_codes = all_fix_lines_codes + mobile_num_codes

# creating a set to get unique a list of unique area codes called by (080)

unique_codes = set()
for x in all_codes:
    unique_codes.add(x)


     
print("The numbers called by people in Bangalore have codes:",'\n'.join(map(str, sorted(unique_codes)))) 
    


# PART B

#Lets find the percentage of calls made from a number starting with "(080)" to a number also starting with "(080)"
# The  list new_filt contains all records of calls initiated by (080)
#lets filter further to extract the receiving number starting with (080) and stor it in fix2 list
fix2 = [x for x in calls_by_080 if x[1].startswith("(080")]

#the percentage of calls is expressed as the len of fix2 / the len of the entire calls dataframe

print(round(len(fix2) / len(calls_by_080) * 100, 2),'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')



 
















