
import re
# * 1. Read the input file
input_file_path = '../0-instructions/day1/input.txt'

# ? read
with open(input_file_path, 'r') as file:
    data = file.readlines()

# ? Clean
data_cleaned = []
for line in data:
    data_cleaned.append(line.strip())

# ? Day 1 Solution
# ! Using 2 pointer approach 

sum = 0
alpha_numeric_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

number_array = alpha_numeric_map.keys()
# print(alpha_numeric_map.keys(), 'type:', type(alpha_numeric_map.keys()))

number_1 = ''
number_2 = ''
for line in data_cleaned:
    test_line = line
    p1 = 0
    p2 = len(test_line) - 1

    is_p1_numberic = False
    is_p2_numeric = True

    print('line:', line)
    while p1 < len(test_line):

        offset_index_3 = p1 + 3
        offset_index_4 = p1 + 4
        offset_index_5 = p1 + 5
        word_3 = test_line[p1:offset_index_3]
        word_4 = test_line[p1:offset_index_4]
        word_5 = test_line[p1:offset_index_5]

        if test_line[p1].isnumeric():
            # print('p1 found:', p1)
            number_1 = test_line[p1]
            break
        elif word_3 in number_array:
            # print('found: ', word_3)
            number_1 = str(alpha_numeric_map[word_3])
            break
        elif word_4 in number_array:
            # print('found: ', word_4)
            number_1 = str(alpha_numeric_map[word_4])
            break
        elif word_5 in number_array:
            # print('found: ', word_5)
            number_1 = str(alpha_numeric_map[word_5])
            break

        p1 += 1

    while p2 > 0:

        offset_index_3 = p2 - 2
        offset_index_4 = p2 - 3
        offset_index_5 = p2 - 4
        p_index = p2 + 1
        word_3 = test_line[offset_index_3:p_index]
        word_4 = test_line[offset_index_4:p_index]
        word_5 = test_line[offset_index_5:p_index]

        if test_line[p2].isnumeric():
            # print('p2 found:', p2)
            number_2 = test_line[p2]
            break
        elif word_3 in number_array:
            # print('found p2: ', word_3)
            number_2 = alpha_numeric_map[word_3]
            break
        elif word_4 in number_array:
            # print('found p2: ', word_4)
            number_2 = alpha_numeric_map[word_4]
            break
        elif word_5 in number_array:
            # print('found p2: ', word_5)
            number_2 = alpha_numeric_map[word_5]
            break


        p2 -= 1

    print('Number 1:' ,number_1)
    print('Number 2:' ,number_2)
    # print()
    number = str(number_1) + str(number_2)
    print('number:', number)
    number_int = int(number)
    sum += number_int
    print('sum:', sum)
    print('=================')
    # print('number int:', number_int, 'type:', type(number_int))

print('sum:', sum)