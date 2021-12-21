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

#Find all of the area codes and mobile prefixes initiated by "(080)" area code

# lets filter calling numbers starting with (080) from the calls dataframe and store it in numb dataframe

numb =df[df.calling_number.str.startswith("(080)")] # the numb dataframe gives us 1080 rows

# lets filter for fixed lines that begings with 0 called by "(080)" area code

fix_num = numb[numb.receiving_number.str.startswith("(0")]

# convert all fix numbers extrated into a list

all_fix_area_Code =fix_num.receiving_number.to_list()

#by applying list comprehension lets do the following steps

#lets split the list at the closing parentheses containing the area code
all_fix = [x.split(')') for x in all_fix_area_Code]

# lets extract the first half of all_fix list  that contains the area code and store it in all_fix2

all_fix2 = [x[0] for x in all_fix]

# joining the closing parentheses to have the area code in parentheses and store it in all_fix3

all_fix3 = [x + x.join(')') for x in all_fix2]


# repeating the same proccess for calls initiated by area code (080) to mobile numbers starting with 7, 8, 9

mob = numb[numb.receiving_number.str.contains(" ")]

# conveting the receiving mobile number into a list
all_mobile = mob.receiving_number.to_list()

# Filtering all mobil number starting with 7, 8, 9 and storing it to a list
list1 =[]
for x in all_mobile:
    if x.startswith('7') or x.startswith('8') or x.startswith('9'):
        list1.append(x[:4])
        
# Checking for calls initiated by area code 080 to telemarketers numbers staring with 140

tele= numb[numb.receiving_number.str.startswith("140")] # No record found for this category 

# creating a list of all calls initiated by (080) to all area codes 

all_area_codes = all_fix3 + list1 



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
# The numb dataframe contains all records of calls initiated by (080)
#lets filter further to extract the receiving number starting with (080) and stor it in fix2 dataframe
fix2 = numb[numb.receiving_number.str.startswith("(080")]

#the percentage of calls is expressed as the len of fix2 / the len of the entire calls dataframe

print(round(len(fix2) / len(df) * 100, 2),'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')



 


# Big O = O(19 N)

# There are 19 steps to solve this problem

#dropping costants 

#==> O(N)













