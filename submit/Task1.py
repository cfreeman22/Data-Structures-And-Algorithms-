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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# first i will extract using indexing the calling number and recieving number from both the call and text lists and store them in predefined variables (lists)

# extracting calling number in texts list
calling_num_text = [x[0] for x in texts]

# extracting receiving number in text list
receiving_number_text = [x[1] for x in texts]


# extracting calling number in calls list

calling_number_calls = [x[0] for x in calls]

# extracting receiving number in call list

receiving_number_calls = [x[1] for x in calls]

# next I will combine all the lists to have just one list of all numbers

all_calls_and_text_numbers = calling_num_text + calling_number_calls + receiving_number_calls +receiving_number_text

# Next i will define a function to extract unique values(numbers) from the list 
# function to get unique numbers
def unique(x):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for num in x:
        # check if exists in unique_list or not
        if num not in unique_list:
            unique_list.append(num)
    # print the len of the unique list to get the value of unique numbers
    print(f"There are {len(unique_list)} different telephone numbers in all text and calls records.")
    
#printing the message to show the count of different telephone numbers    
unique(all_calls_and_text_numbers)


# Big O = O(7 N)

# There are 7 steps to solve this problem

#dropping costants 

#==> O(N)

