import copy

cleaned = []
with open('./input.txt') as f:
    data = f.readlines()

for line in data:
    line = line.strip()
    cleaned.append(line)

########################################
# Part 1 - Calcualte Total Safe/Unsafe #
########################################

# Check decreasing 
def check_decreasing(chars):
    range_length = len(chars) - 1
    # WORKING Tey
    # print('Range length:', range_length)
    for i in range(range_length):
        first_num = int(chars[i])
        second_num = int(chars[i+1])
        if first_num > second_num:
            if (first_num - second_num) < 4:
                continue
            else:
                return False
        else:
            return False
    print('yes - decreasing')
    return True

# Check increasing 
def check_increasing(chars):
    range_length = len(chars) - 1
    for i in range(range_length):
        first_num = int(chars[i])
        second_num = int(chars[i+1])
        # 1 3: 
        if first_num < second_num:
            if (second_num - first_num) < 4:
                continue
            else:
                return False
        else:
            return False
    print('yes - increasing')
    return True


safe_counter = 0
for line in cleaned:
    # separate by spaces
    chars = line.split(' ')
    print('Chars:', line.split(' '))
    if check_increasing(chars):
        safe_counter += 1
    elif check_decreasing(chars):
        safe_counter += 1
    else:
        print('unsafe\n')
        # Check removal of a single number and see if it's safe or not
        # 1. Remove character by character
        chars_copy = copy.deepcopy(chars)
        for j in range(len(chars)):
            # NOTE: Python copies by ref; I need copy by val here --> import copy
            chars_copy = copy.deepcopy(chars)
            del chars_copy[j]
            print('new char:', chars_copy, '\n')
            # 2. Then check if it is safe or unsafe
            if check_increasing(chars_copy):
                safe_counter += 1
                break
            elif check_decreasing(chars_copy):
                safe_counter += 1
                break

print('Total Safes:', safe_counter)

# Part 2 Ans: 339 - 363
