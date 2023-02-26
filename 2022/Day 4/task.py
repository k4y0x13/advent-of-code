
# Check in one range is in another range:

# Read inputs into an array
with open('input.txt', 'r') as f:
    input = f.readlines()

# print(input[:10])

# Clean New lines
input = [x.strip() for x in input]

# print(input[:10])

# Clean comma and -:
input = [x.replace('-',' ') for x in input]
input = [x.replace(',',' ') for x in input]

# Calculate the overlapping ranges
print('len of input: ', len(input))

def is_rangeA_in_rangeB(start_a, end_a, start_b, end_b):
    return start_b <= start_a and end_a <= end_b

def is_rangeA_beside_rangeB(end_a, start_b):
    return start_b >end_a 

overlapping_range = 0
task2_answer = 0
for pairs in input:
    numbers = (pairs.split(' '))

    start_a = int(numbers[0])
    end_a = int(numbers[1])
    start_b = int(numbers[2])
    end_b = int(numbers[3])

    if is_rangeA_in_rangeB(start_a, end_a, start_b, end_b) or is_rangeA_in_rangeB(start_b, end_b, start_a, end_a):
        overlapping_range += 1
    
    if start_a in range(start_b, end_b+1) or end_a in range(start_b, end_b+1) or  start_b in range(start_a, end_a+1) or end_b in range(start_a, end_a+1):
        task2_answer += 1

    # if start_b >= start_a and end_b <= end_a:
    #     overlapping_range += 1
    #     continue
    #     # print(numbers)
    # elif start_a >= start_b and end_a <= end_b:
    #     overlapping_range += 1 
    #     continue
    #     # print(numbers)

print('Overlaping total: ', overlapping_range)
print('Overlaping task 2: ', task2_answer)

# =======================
# ===== TASK 2 ==========
# =======================

# Find pairs that "overlap at all." Example:
# In the above example, 
#   the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, 

#     5-7,7-9 overlaps in a single section, 7.
#     2-8,3-7 overlaps all of the sections 3 through 7.
#     6-6,4-6 overlaps in a single section, 6.
#     2-6,4-8 overlaps in sections 4, 5, and 6.



