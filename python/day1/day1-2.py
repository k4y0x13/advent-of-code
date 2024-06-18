import os
import sys
# Need abs path
abs_path = os.path.abspath('../utils')
# Put it into Path Directory
sys.path.append(abs_path)
# then only you can import the module/file
import read_input
# from ..utils import read_input

# input_file = '../../0-instructions/day1/input.txt'
input_file = '../../0-instructions/day1/example_input.txt'
data = read_input.read_input_from_file(input_file)
cleaned = read_input.remove_newlines(data)

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

def digit_in_line(line):
    is_digit = False
    index_of_digit = 0
    for char in line:
        if char.isdigit():
            is_digit = True
            index_of_digit = index(char)
    return is_digit, index


max_window_size = 4
chars = alpha_numeric_map.keys()
sum = 0
line_no = 1

for line in cleaned:
    start_window = 0
    end_window = 4 
    len_line = len(line)
    nums_in_line = []
    print('line:', line_no)
    line_no += 1

    if len_line <= 2:
        print('2 running')
        end_window = 2
        while end_window <= len(line):
            window_chars = line[start_window:end_window+1]
            # print('window char:', window_chars)
            for char in window_chars:
                if char.isdigit():
                    # print('char found in 2', char)
                    nums_in_line.append(int(char))
                for key in chars:
                    if key in window_chars:
                        # print('key found in key', key)
                        nums_in_line.append(alpha_numeric_map[key])
            start_window += 1
            end_window += 1

        # print('nums in line:', nums_in_line, )
        print('number: ', str(nums_in_line[0]) + str(nums_in_line[-1]))
        print()


    if len_line == 3:
        print('3 running')
        end_window = 3
        while end_window <= len(line):
            window_chars = line[start_window:end_window+1]
            for char in window_chars:
                if char.isdigit():
                    # print('char found', char)
                    nums_in_line.append(int(char))
                for key in chars:
                    if key in window_chars:
                        nums_in_line.append(alpha_numeric_map[key])
            start_window += 1
            end_window += 1

        # print('nums in line:', nums_in_line, )
        print('number: ', str(nums_in_line[0]) + str(nums_in_line[-1]))
        print()


    if len_line >= 4:
        print('4 running')
        while end_window <= len(line):
            window_chars = line[start_window:end_window+1]
            for char in window_chars:
                if char.isdigit():
                    # print('char found', char)
                    nums_in_line.append(int(char))
                for key in chars:
                    if key in window_chars:
                        nums_in_line.append(alpha_numeric_map[key])
            start_window += 1
            end_window += 1

        # print('nums in line:', nums_in_line, )
        print('number: ', str(nums_in_line[0]) + str(nums_in_line[-1]))
        print()

    
    # print('before adding:', nums_in_line)
    sum += int(str(nums_in_line[0]) + str(nums_in_line[-1]))

print('Total sum:', sum)





