def solve_part1(input_data):
    lines = input_data.strip('')
    total = 0
    for line in lines:
        # process each line
        if line=="(":
            total += 1
        elif line==")":
            total -= 1
    return total

def solve_part2(input_data):
    lines = input_data.strip('')
    total = 0
    counter = 0
    for line in lines:
        # process each line
        if line=="(":
            total += 1
        elif line==")":
            total -= 1
        counter += 1
        if total < 0:
            return counter
    return total



if __name__ == "__main__":
    # Read input file
    with open("input.txt", "r") as f:
        input_data  = f.read()
        
    # solve parts
    part1 = solve_part1(input_data)
    part2 = solve_part2(input_data)

    print(f"Part 1:", part1)
    print(f"Part 2:", part2)
