package main

import (
	"fmt"
	"log"
)

func main() {
	input, err := readInput("input.txt")
	if err != nil {
		log.Fatal("Cannot read file", err)
	}

	fmt.Println("Part 1: ", part1(input))
	fmt.Println("Part 2: ", part2(input))
}
