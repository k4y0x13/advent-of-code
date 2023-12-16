# ===================
# ====== TASK 1 =====
# ===================

# read the input
with open('./input.txt', 'r') as f:
    input = f.readline()
    input = [char for counter, char in enumerate(input)]

for charIndex in range(0, len(input)):
    next_four_chars = input[charIndex:charIndex+4]
    # print(next_four_chars)
    next_four_chars_set = set(next_four_chars)
    # print(next_four_chars_set, "len: ", len(next_four_chars_set))
    if len(next_four_chars_set) == 4:
        print('Task 1 Solution')
        print('Value: ', charIndex+4)
        print('letters: ', next_four_chars)
        break

# ===================
# ====== TASK 2 =====
# ===================

for charIndex in range(0, len(input)):
    next_fourteen_characters = input[charIndex:charIndex+14]
    # print(next_four_chars)
    next_four_chars_set = set(next_fourteen_characters)
    # print(next_four_chars_set, "len: ", len(next_four_chars_set))
    if len(next_four_chars_set) == 14:
        print('Task 2 Solution')
        print('Value: ', charIndex+14)
        print('letters: ', next_fourteen_characters)
        break
