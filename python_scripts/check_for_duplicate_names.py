'''
This script checks to see if two lists have any of the same name in them. It 
then removes any duplicates found in the list. 
'''

# Import modules
import time

# Define functions
def check_for_duplicates(list1, list2):
    for item in list1:
        if item in list2:
            list2.remove(item)
    return list2

# Define variables
file_for_list1 = r"C:\Users\Jackson Roubidoux\Record Linking Lab\Git_training\Git_training\lists_of_food\list1.txt"
file_for_list2 = r"C:\Users\Jackson Roubidoux\Record Linking Lab\Git_training\Git_training\lists_of_food\list2.txt"

# Define lists
with open(file_for_list1, 'r') as f:
    list1 = f.read().splitlines()
with open(file_for_list2, 'r') as f:
    list2 = f.read().splitlines()

# Store the length of list2
list2_length = len(list2)

# Define start time
start_time = time.time()

# Run function
check_for_duplicates(list1, list2)

# Define end time
end_time = time.time()

# Store the length of list2 after the function has been run
list2_length_after_function = len(list2)

# Print results
print('There was {} duplicate(s) found in the list.'.format(list2_length - list2_length_after_function))
print('The script took {} seconds to run.'.format(end_time - start_time))