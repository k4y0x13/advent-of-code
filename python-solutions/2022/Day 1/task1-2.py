
# Read the input from file input.txt
with open('input.txt') as f:
    input = f.readlines()

# print first 20 lines of input
# print(input[:20])

# First 20 lines
test = input[:20]
# print(len(test))

# Clean the input
cleaned_input = []
for line in input:
    line = line.strip()
    cleaned_input.append(line)

# Worked !!! ====================
# for line in cleaned_input[:20]:
#     print(line)


# TASKS ================================ 
# Find the Elf carrying the most Calories. 
# How many total Calories is that Elf carrying?
# ======================================

# Group calories to elves using dictionary
# Example:
# {1: [500, 300, 200], 2: [400, 200, 100], 3: [300, 100, 100]}

evles_calorie_map = {}
evles_id = 1

elves_calories = []
for line in cleaned_input:
    if line == "":
        elves_calories = []
        evles_id += 1
        continue
    elves_calories.append(int(line))
    evles_calorie_map[evles_id] = elves_calories

# print(evles_calorie_map)

# Find max calorie and which elve has it
elve_max = 0
max_calorie = 0

for elve in evles_calorie_map:
    total_elve_calorie = 0
    calories = evles_calorie_map[elve]
    # Calculate sum of all calorie of each elve
    for calorie in calories:
        total_elve_calorie += calorie
    
    # check if it is the maximum. 
    # If no, leave it, else reassign
    if (total_elve_calorie < max_calorie):
        continue
    else:
        max_calorie = total_elve_calorie
        elve_max = elve

# Print the result
print(f'Elve that has max calorie: {elve_max}')
print(f'Max Calorie amoutn: {max_calorie}\n')

# Correct answer:
# Elve: 26th
# Calorie amount: 70764


# =================================
# TASK 2 ==========================
# =================================

#Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total? 

# Solution
# Calculate the sum for each elve
for elve in evles_calorie_map:
    # calculate the sum total
    total_calorie = 0
    calories = evles_calorie_map[elve]
    for calorie in calories:
        total_calorie += calorie
    # Reassign the total calorie to the map
    evles_calorie_map[elve] = total_calorie

# This is a better one:
# print(evles_calorie_map)

# Sort the dictionary using the sort method of python
# But the dict needs to be sorted by values and not keys
# Ref: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/

# Sorted() takes in three parameters:
    # iterable
    # key
    # reverse
# the items() fn on dict will return key and value pari
# We want reverse=True as we want in desending and not ascending

sorted_evles_calorie_map = sorted(evles_calorie_map.items(), key=lambda x:x[1], reverse=True)
# Print the top three evles
print('Top three evles and calories: ')
print(f'{sorted_evles_calorie_map[:3]}\n')

# Calculate the total calorie of the top three:
total_top_three = 0
for elve in sorted_evles_calorie_map[:3]:
    total_top_three += elve[1]

print(f'Total top three calorie: {total_top_three}')

