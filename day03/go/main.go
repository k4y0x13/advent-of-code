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

	// the solutions
	pointSet := make(map[Point]bool)
	pointSet[Point{0, 0}] = true
	// santa goes and delivers
	x_santa := 0
	y_santa := 0
	for _, direction := range santa_directions {
		if direction == "^" {
			y_santa += 1
			if !pointSet[Point{x_santa, y_santa}] {
				// doesn't exist
				pointSet[Point{x_santa, y_santa}] = true
			}
		} else if direction == "v" {
			y_santa -= 1
			if !pointSet[Point{x_santa, y_santa}] {
				// doesn't exist
				pointSet[Point{x_santa, y_santa}] = true
			}
		} else if direction == ">" {
			x_santa += 1
			if !pointSet[Point{x_santa, y_santa}] {
				// doesn't exist
				pointSet[Point{x_santa, y_santa}] = true
			}
		} else if direction == "<" {
			x_santa -= 1
			if !pointSet[Point{x_santa, y_santa}] {
				// doesn't exist
				pointSet[Point{x_santa, y_santa}] = true
			}
		}
	}

	// robot goes to deliver
	x_robot := 0
	y_robot := 0
	for _, direction := range robot_directions {
		if direction == "^" {
			y_robot += 1
			if !pointSet[Point{x_robot, y_robot}] {
				// doesn't exist
				pointSet[Point{x_robot, y_robot}] = true
			}
		} else if direction == "v" {
			y_robot -= 1
			if !pointSet[Point{x_robot, y_robot}] {
				// doesn't exist
				pointSet[Point{x_robot, y_robot}] = true
			}
		} else if direction == ">" {
			x_robot += 1
			if !pointSet[Point{x_robot, y_robot}] {
				// doesn't exist
				pointSet[Point{x_robot, y_robot}] = true
			}
		} else if direction == "<" {
			x_robot -= 1
			if !pointSet[Point{x_robot, y_robot}] {
				// doesn't exist
				pointSet[Point{x_robot, y_robot}] = true
			}
		}
	}

	total_visited := len(pointSet)
	return total_visited
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
