######################################
# Part 1 - Calcualte Total Distances #
######################################

cleaned = []
first_column = []
second_column = []

with open('./input.txt', 'r') as f:
        data = f.readlines()

for line in data:
    # line.replace("", '\n')
    line = line.strip()
    cleaned.append(line)


# separate each line based on spaces
# first column is from 0 till 4th index
# second column is from 
for line in cleaned:
    line = line.split("   ")
    first_column.append(line[0])
    second_column.append(line[1])

print('first:', first_column[:10])
print('second:', second_column[:10])

first_column.sort()
second_column.sort()

# print('first sorted:', first_column[:10])
# print('first length:', len(first_column))
# print('second sorted:', second_column[:10])
# print('second length:', len(second_column))

total_distance = 0

for i in range(len(first_column)):
    first_number = int(first_column[i])
    second_number = int(second_column[i])
    distance = second_number - first_number
    total_distance += abs(distance)

print('Total Distance:', total_distance)

######################################
# Part 2 - Calcualte Similarity Score#
######################################
from collections import Counter

second_column_counters = Counter(second_column)
# print('Second Counters:', second_column_counters)

similarity_score = 0
for i in range(len(first_column)):
    first_number = first_column[i]
    if first_number in second_column_counters:
        similarity_score += int(first_number) * int(second_column_counters[first_number])

print('Similarity score:', similarity_score)



