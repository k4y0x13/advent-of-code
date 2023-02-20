# Each rucksack: 2 compartment
# a means one type and A means another type
# Item of a given type: in one rucksack
# Another type: in another rucksack
# Error rate: One item per rucksack

# first-half of chars = one component
# second half = another component in the rucksack

# Example: 'vJrwpWtwJgWrhcsFMMfFFhFp'
# First half: vJrwpWtwJgWr
# Second half: hcsFMMfFFhFp
# Error: 'p' as it appears in both of the compartments

# a- z: priority level 1-26
# A - Z: priority level 27 - 52

# Sum of priorities: ?

# =======================
# ===== SOLUTION ========
# =======================

# Read input from file to an array
with open('/home/yeshey-dorji/cs/advent-of-code/2022/Day 3/input.txt', 'r') as f:
    input = f.readlines()

# Remove new line characters
input = [x.strip() for x in input]

# Variables needed:
first_compartment = []
second_compartment = []
error_item = []

# Initialize the variables
for item in input:
    # Get the items for the first compartment 
    # half the string lenth
    divide_at = int(len(item)/2)
    f_items = item[:divide_at]
    s_items = item[divide_at:]
    first_compartment.append(f_items)
    second_compartment.append(s_items)

# Checking if my code is right:
# for i in range(5):
#     print(input[i] + '\n')
#     print(first_compartment[i] + '\n')
#     print(second_compartment[i] + '\n')
#     print()

# Calculate the error as there is only one per rucksack
# print(len(first_compartment))
# print(len(second_compartment))

# Function to return the common item in both the components:
def get_item_error(firstC, secondC):
    for char in firstC:
        if char in secondC:
            return char

# ASCII of 
#   'a' = 97, 'z' = 122
#   'A' = 65, 'Z' = 90

def calc_priority(char_item):
    if char_item.islower():
        return ord(char_item) - 96
    else: # It is upper case
        return ord(char_item) - 38

# print(calc_priority('a'))
# print(calc_priority('z'))
# print(calc_priority('A'))
# print(calc_priority('Z'))

# Calculate the sum of priority
sum = 0
for i in range(len(first_compartment)): # Len of first C = second C
    error = get_item_error(first_compartment[i], second_compartment[i])
    priority = calc_priority(error)
    sum += priority

print('Total priority (task 1): ', sum)

# ==========================
# TASK 2 ===================
# ==========================

# Check the Badge that is common in all of the three groups

# From the input:
# Three lines = One group
# One item that is common among those three

# Solution:
# For each of three line, get the itemlists.
# Check for item that is common among them
# Calculate priority and print the output

sum_priority = 0
print(len(input))
# print(input[-1])
# print(input[297:300])

for i in range(0, len(input), 3):
    # print(first_compartment[i:i+3])
    group_rucksacks = input[i:i+3]
    # print(f"i: {i}, i+3: {i+3}")
    # print(group_rucksacks)
    for char in group_rucksacks[0]:
        if char in group_rucksacks[1] and char in group_rucksacks[2]:
            # print(char) # Got the most common item in all three rucksacks
            prioril = calc_priority(char)
            # print(char, f' {calc_priority(char)} {i}')
            sum_priority += prioril
            break
    
print('Priority level (task 2): ', sum_priority)

