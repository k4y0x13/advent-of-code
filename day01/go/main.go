package main

import (
	"fmt"
	"os"
	"strings"
)

func SolvePart1(input string) int {
	lines := strings.Split(input, "")
	sum := 0

	// process each line
	for _, line := range lines {
		// fmt.Println("line:", line)
		if line == "(" {
			// fmt.Println("opening found")
			sum += 1
		} else if line == ")" {
			// fmt.Println("closing found")
			sum -= 1
		}
	}
	return sum
}

func SolvePart2(input string) int {
	lines := strings.Split(input, "")
	sum_p2 := 0
	counter := 0

	for _, line := range lines {

		if line == "(" {
			// fmt.Println("opening found")
			sum_p2 += 1
		} else if line == ")" {
			// fmt.Println("closing found")
			sum_p2 -= 1
		}

		counter += 1

		if sum_p2 < 0 {
			return counter
		}
	}
	return sum_p2
}

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)

	// solve parts
	part1 := SolvePart1(input)
	part2 := SolvePart2(input)

	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}
