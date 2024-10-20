
data = []
with open("./input.txt") as f:
    data = f.readlines()


counter = 0
for char in data[0]:
    print(char)
    if char == "(":
        counter += 1
    elif char == ")":
        counter -= 1


print("final counter:", counter)
