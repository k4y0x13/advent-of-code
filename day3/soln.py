
cleaned = []
with open('./test_input.txt', 'r') as f:
    data = f.readlines()

for line in data:
    line = line.strip()
    cleaned.append(line)

print(cleaned[:10])

def return_nums(chars):

    # loop through and search for the keyword "mul"
    for i in range(len(chars) - 2):
        if chars[i:i+2] == 'mul':


    return (2,3)

sum = 0
for line in cleaned:

    num1, num2 = return_nums(line)
    sum += (num1 * num2)
    

print('Total Sum:', sum)
