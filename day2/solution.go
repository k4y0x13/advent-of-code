package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func part1(input string) int {
	// solution
	total_sum := 0

	// Input: one line of string
	// 1. Delimete string with commas for range
	ranges := strings.Split(input, ",")
	// 2. Separate each range with - for start and end
	for _, range_value := range ranges {
		start_end := strings.Split(range_value, "-")
		start_str := start_end[0]
		end_str := start_end[1]
		fmt.Println("\nrange:", range_value, "\nstart:", start_str, "\nend:", end_str)
		// 3. loop through start and end, inclusive (int)
		start_int, err := strconv.Atoi(start_str)
		if err != nil {
			log.Fatal("Cannot convert str to int, start_int: ", start_int)
		}
		end_int, err := strconv.Atoi(end_str)
		if err != nil {
			log.Fatal("Cannot convert str to int, end_int: ", end_int)
		}
		for i := start_int; i <= end_int; i++ {
			i_str := strconv.Itoa(i)
			// fmt.Println("i is: ", i, "and: ", i_str)
			if len(i_str)%2 != 0 {
				// if division isn't even then there ain't any repeats
				// fmt.Println("Skipping:", i)
				// fmt.Println("Skipping:", i_str)
				continue
			}
			// Else, check for repeats
			mid_index := len(i_str) / 2
			// fmt.Println("mid index: ", mid_index)
			fmt.Println("Comparing:", i_str[:mid_index], "with: ", i_str[mid_index:])
			if i_str[:mid_index] == i_str[mid_index:] {
				// fmt.Println("Invalid id found:", i)
				total_sum += i
				// fmt.Println("Value added:", i)
				// fmt.Println("Total sum:", total_sum)
			}
		}
	}
	// 4. Check if number repeats twice
	// 4.1 Convert back to string
	// 4.2 Check if len is even
	// 4.3 if even, divide into two and check if it's repeating
	// 4.4 If it's repeating, add to the sum value

	fmt.Println("Total sum:", total_sum)
	return total_sum
}

func part2(input string) int {
	return 2
}

func readInput(filename string) (string, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return "", err
	}

	return string(data), nil
}
