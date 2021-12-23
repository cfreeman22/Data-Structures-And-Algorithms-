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


# grouping the sorted calls list to extract the total sum of call duration per number
grouped_list = []
for key, items in itertools.groupby(sorted_calls, operator.itemgetter('calling_num')):
    
    grouped_list.append(list(items))


    
#Find all of the area codes and mobile prefixes initiated by "(080)" area code
new_filt = [x for x in sorted_calls if x['calling_num'].startswith('(080)')]


# lets filter for fixed lines that begings with 0 called by "(080)" area code

fix_num = [x for x in new_filt if x['receiving_num'].startswith("(0")]

# lets filter calling numbers starting with (080) from the calls into a list

all_fix = [key['receiving_num'] for key in fix_num]

#lets split the list at the closing parentheses containing the area code
all_fix_area_Code = [x.split(')') for x in all_fix]

# extracting the area code and joining the parentheses to have area code in brackets 
all_fix_codes = [x[0] + x[0].join(')') for x in all_fix_area_Code]

# repeating the same proccess for calls initiated by area code (080) to mobile numbers starting with 7, 8, 9

mobile = [x for x in new_filt if " " in x['receiving_num']]

# Filtering all mobile numbers and storing it to a list
all_mobile_phones = [key['receiving_num'] for key in mobile]

# Filtering all mobile number starting with 7, 8, 9 and storing it to a list and extacting the first 4 digits 

mobile_code_list =[x[:4] for x in all_mobile_phones if x.startswith('7') or x.startswith('8') or x.startswith('9')]

# creating a list of all calls initiated by (080) to all area codes 
all_area_codes = all_fix_codes + mobile_code_list


# creating a function to print unique a list of unique area codes called by (080)

def unique(x):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for num in x:
        # check if exists in unique_list or not
        if num not in unique_list:
            unique_list.append(num)
    # print list
    print("The numbers called by people in Bangalore have codes:",'\n'.join(map(str, sorted(unique_list)))) 
    

unique(all_area_codes)


# PART B

#Lets find the percentage of calls made from a number starting with "(080)" to a number also starting with "(080)"
# The  list new_filt contains all records of calls initiated by (080)
#lets filter further to extract the receiving number starting with (080) and stor it in fix2 list
fix2 = [x for x in new_filt if x['receiving_num'].startswith("(080")]

#the percentage of calls is expressed as the len of fix2 / the len of the entire calls dataframe

print(round(len(fix2) / len(sorted_calls) * 100, 2),'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')



# Big O = O(26 N)

# There are 26 steps to solve this problem

#dropping costants 

#==> O(N)

















