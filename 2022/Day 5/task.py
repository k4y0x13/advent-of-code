import re

# ===================
# ====== TASK 1 =====
# ===================

# Tasks:
# 1. Setup the initial stack. aka, the given input stack.
#   a. array 1 to 9 for each of the stack.
# 2. Read the input line by line
# 3. Get the numbers from the input:
#   a. first number: amount of stack to move
#   b. second number: stack to be reduced
#   c. third number: stack to be added to
# 4. Make a function that will perform the stack operations
# 5. Read the top element of each stack and output it.

arr1 = ['D', 'L', 'J', 'R', 'V', 'G', 'F']
arr2 = ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S']
arr3 = ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C']
arr4 = ['M', 'D', 'P', 'N', 'G', 'Q']
arr5 = ['J', 'L', 'H', 'N', 'F']
arr6 = ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z']
arr7 = ['F', 'D', 'B', 'L']
arr8 = ['M', 'J', 'B', 'S', 'V', 'D', 'N']
arr9 = ['G', 'L', 'D']

number_to_stack_map = {
    1: arr1,
    2: arr2,
    3: arr3,
    4: arr4,
    5: arr5,
    6: arr6,
    7: arr7,
    8: arr8,
    9: arr9,
}

# Read input:
with open('/home/yeshey-dorji/cs/advent-of-code/2022/Day 5/input.txt', 'r') as f:
    input = f.readlines()
    input = [x.strip() for x in input]

print('Len of input: ', len(input))

# inputExample = 'move 3 from 4 to 6'

def get_all_numbers_from_input(inputLine):
   return(re.findall(r'\d+', inputLine))

# def move_element_CrateMover9000(no_of_stacks, from_stack_index, to_stack_index):
#     for i in range(0, no_of_stacks):
#         to_move_element_CrateMover9000 = number_to_stack_map[from_stack_index].pop()
#         number_to_stack_map[to_stack_index].append(to_move_element_CrateMover9000)

# for line in input:
#     numbers = get_all_numbers_from_input(line)

#     no_of_stacks = int(numbers[0])
#     from_stack_index = int(numbers[1])
#     to_stack_index = int(numbers[2])

#     move_element_CrateMover9000(no_of_stacks, from_stack_index, to_stack_index)

# # Task 1 Solution
# print('Task 1: solution: ')
# for key in number_to_stack_map:
#     arr = number_to_stack_map[key]
#     print(arr[-1])
# print()

# ===================
# ====== TASK 2 =====
# ===================

def move_element_CrateMover9001(no_of_stacks, from_stack_index, to_stack_index):
    array_to_be_deducted = number_to_stack_map[from_stack_index]
    array_to_be_added = number_to_stack_map[to_stack_index]
    elements_to_be_moved_array = array_to_be_deducted[-no_of_stacks:]
    array_to_be_added.extend(elements_to_be_moved_array)
    
    # Delete the elements from the to_be_deducted and reassign to the map
    for i in range(0, no_of_stacks):
        number_to_stack_map[from_stack_index].pop()



for line in input:
    numbers = get_all_numbers_from_input(line)

    no_of_stacks = int(numbers[0])
    from_stack_index = int(numbers[1])
    to_stack_index = int(numbers[2])

    move_element_CrateMover9001(no_of_stacks, from_stack_index, to_stack_index)

# Task 2 Solution
print('Task 2: solution: ')
for key in number_to_stack_map:
    arr = number_to_stack_map[key]
    print(arr[-1])
print()