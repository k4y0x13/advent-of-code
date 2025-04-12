package main

import (
	"fmt"
	"os"
)

func SolvePart2(input string) int {
	return 0
}

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)

	part2 := SolvePart2(input)
	fmt.Println("Part 2:", part2)
}
