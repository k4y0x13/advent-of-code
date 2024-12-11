
from re import split


cleaned = []
with open('./input.txt', 'r') as f:
    data = f.readlines()

for line in data:
    line = line.strip()
    cleaned.append(line)

# print(cleaned[:10])
first_line = cleaned[0]
print(first_line[1:4])

def clean_string(num_str):
    # Extract out the numbers from the string_to_multiply
    string_to_multiply_cleaned = num_str.replace("(", "")
    string_to_multiply_cleaned = string_to_multiply_cleaned.replace(")", "")
    splitted = string_to_multiply_cleaned.split(',')
    if len(splitted) != 2:
        return (0,0)
    try:
        num1 = int(splitted[0])
        num2 = int(splitted[1])
        return (num1, num2)
    except:
        return(0,0)

sum = 0
def return_nums(chars):
    # loop through and search for the keyword "mul"
    string_to_multiply = ''
    for i in range(len(chars)):
        end_of_mul_index = i + 3 # exclusive
        if chars[i:end_of_mul_index] == 'mul':
            key_word = chars[i:end_of_mul_index]
            # print('Chars found:', key_word)
            start_of_parenthesis_index = end_of_mul_index # not inclusive
            # print('start of parenthesis:', start_of_parenthesis_index)

            # find end of parenthesis index if start is (
            if chars[end_of_mul_index] == "(":
                # print('openining parenthesis found at index:', end_of_mul_index)
                j = end_of_mul_index
                while chars[j] != ')':
                    if chars[j] == ']' or chars[j] == "}":
                        break
                    j += 1
                end_of_parenthesis = j+1

                if chars[end_of_parenthesis-1] == ')':
                    mul_nums = chars[start_of_parenthesis_index:end_of_parenthesis]
                    print('mul nums:', mul_nums)
                    num1, num2 = clean_string(mul_nums)
                    print('num 1:', num1)
                    print('num 2:', num2)

                    global sum 
                    sum += num1 * num2

for line in cleaned:
    return_nums(line)

print('Total Sum:', sum)
