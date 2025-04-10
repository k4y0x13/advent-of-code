def solve_part1(input_data):
    lines = input_data.strip('\n')
    total = 0
    for line in lines:
        # process each line
        pass
    return total

def solve_part2(input_data):
    return 0

if __name__ == "__main__":
    # Read input file
    with open("input.txt", "r") as f:
        input_data  = f.read()
        
    # solve parts
    part1 = solve_part1(input_data)
    part2 = solve_part2(input_data)

    print(f"Part 1:", {part1})
    print(f"Part 2:", {part2})
