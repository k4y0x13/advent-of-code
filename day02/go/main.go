package main

import (
	"fmt"
	// "math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func find_min_of_three(l, w, h int) (int, int) {
	nums := []int{l, w, h}
	sort.Ints(nums)
	return nums[0], nums[1]
}

func SolvePart1(input string) int {
	lines := strings.Split(input, "\n")
	total := 0
	for _, line := range lines {
		// error checks
		if len(line) < 3 {
			continue
		}
		fmt.Println("Line:", line)
		// split the line with x as delimiter
		numbers := strings.Split(line, "x")
		// fmt.Printf("Numbers: ", numbers)
		l, err := strconv.Atoi(numbers[0])
		if err != nil {
			panic(err)
		}
		w, err := strconv.Atoi(numbers[1])
		if err != nil {
			panic(err)
		}
		h, err := strconv.Atoi(numbers[2])
		if err != nil {
			panic(err)
		}
		// fmt.Printf("Numbers l:%d w:%d h:%d\n", l, w, h)

		// solve for the problem
		surface_area := 2*l*w + 2*w*h + 2*h*l
		// fmt.Println("Surface Area:", surface_area)
		min1, min2 := find_min_of_three(l, w, h)
		slack := min1 * min2
		// fmt.Println("Slack: ", slack)
		total_surface_area := surface_area + slack
		// fmt.Println("total surface area: ", total_surface_area)
		total += total_surface_area
	}
	return total
}

func SolvePart2(input string) int {
	lines := strings.Split(input, "\n")
	total := 0
	for _, line := range lines {
		// error checks
		if len(line) < 3 {
			continue
		}
		fmt.Println("Line:", line)
		// split the line with x as delimiter
		numbers := strings.Split(line, "x")
		// fmt.Printf("Numbers: ", numbers)
		l, err := strconv.Atoi(numbers[0])
		if err != nil {
			panic(err)
		}
		w, err := strconv.Atoi(numbers[1])
		if err != nil {
			panic(err)
		}
		h, err := strconv.Atoi(numbers[2])
		if err != nil {
			panic(err)
		}
		// fmt.Printf("Numbers l:%d w:%d h:%d\n", l, w, h)

		// solve for the problem
		min1, min2 := find_min_of_three(l, w, h)
		perimeter := min1 + min1 + min2 + min2
		fmt.Println("perimeter", perimeter)
		cubit_feet := l * w * h
		fmt.Println("cubic feet", cubit_feet)
		total_ribbon := perimeter + cubit_feet
		fmt.Println("total ribbon", total_ribbon)
		total += total_ribbon

	}
	return total
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
