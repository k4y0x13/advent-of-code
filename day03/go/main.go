package main

import (
	"fmt"
	"os"
	"strings"
)

type Point struct {
	X, Y int
}

func SolvePart2(input string) int {
	// process the input
	directions := strings.Split(input, "")
	var santa_directions []string
	var robot_directions []string

	for index, direction := range directions {
		if index%2 == 0 {
			santa_directions = append(santa_directions, direction)
		} else {
			robot_directions = append(robot_directions, direction)
		}
	}

	fmt.Println("santa directions:", santa_directions)
	fmt.Println("robot directions:", robot_directions)
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
