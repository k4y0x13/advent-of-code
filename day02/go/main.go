package main

import (
	"fmt"
	"os"
	// "strings"
)

func SolvePart1(input string) int {
	return 0
}

func SolvePart2(input string) int {
	return 0
}

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)

	part1 := SolvePart1(input)
	part2 := SolvePart2(input)

	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}
