package main

import (
	"fmt"
	"os"
	// "strings"
)

func SolvePart1(input string) int {
	// lines := strings.Split(input, "\n")
	sum := 0

	// process each line
	// for _, line := range lines {
	// }
	return sum
}

func SolvePart2(input string) int {
	// lines := strings.Split(input, "\n")
	sum := 0

	// process each line
	// for _, line := range lines {
	// }
	return sum
}

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)

	// solve parts
	part1 := SolvePart1(input)
	part2 := SolvePart1(input)

	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}
