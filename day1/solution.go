package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
	// "golang.org/x/text/runes"
)

func part1(input string) int {
	// solution
	// fmt.Println("input:", input)
	current_number := 50
	zero_counter := 0

	// 1. split input into new lines so that we can access each line
	lines := strings.Split(input, "\n")
	//fmt.Println("first line:", lines[0])
	//fmt.Println("10th line:", lines[10])

	for _, line := range lines {
		if len(line) == 0 {
			break
		}
		// 2. take out L/R from number
		l_r := line[0]
		number_string := line[1:] // starting is inclusive, end is exclusive
		number_change, err := strconv.Atoi(number_string)
		if err != nil {
			log.Fatal("failed to convert string to integer, part1", err)
		}

		// convert l_r to rune
		lr_char := string(l_r)
		// fmt.Println("line:", line)
		// fmt.Println("l or r: ", lr_char)
		// fmt.Println("number:", number_change)

		// 3. map L to sub and R to add and convert rest to int
		// 4. sub and add to the final answer modulus 100 (absolute sum)
		// fmt.Printf("current number: %v\n", current_number)
		// fmt.Printf("zero counter: %v\n", zero_counter)
		if lr_char == "R" {
			// add
			// fmt.Printf("adding %v\n", number_change)
			current_number += number_change
			current_number = current_number % 100

			if current_number == 0 {
				zero_counter += 1
				// fmt.Printf("zero added")
			}

		} else if lr_char == "L" {
			// sub
			// fmt.Printf("subbing %v\n", number_change)
			current_number -= int(math.Abs(float64(number_change)))
			current_number = current_number % 100

			if current_number == 0 {
				zero_counter += 1
				// fmt.Printf("zero added")
			}
		}
		// fmt.Println("")
	}

	// fmt.Println("")
	fmt.Println("final zero value part1: ", zero_counter)
	return zero_counter
}

func part2(input string) int {
	// solution
	current_number := 50
	zero_counter := 0

	lines := strings.Split(input, "\n")

	for _, line := range lines {
		if len(line) == 0 {
			break
		}
		// 2. take out L/R from number
		l_r := line[0]
		number_string := line[1:] // starting is inclusive, end is exclusive
		number_change, err := strconv.Atoi(number_string)
		if err != nil {
			log.Fatal("failed to convert string to integer, part1", err)
		}

		// convert l_r to rune
		lr_char := string(l_r)
		// fmt.Println("line:", line)
		// fmt.Println("l or r: ", lr_char)
		// fmt.Println("number:", number_change)

		// 3. map L to sub and R to add and convert rest to int
		// 4. sub and add to the final answer modulus 100 (absolute sum)
		// fmt.Printf("current number: %v\n", current_number)
		// fmt.Printf("zero counter: %v\n", zero_counter)
		for i := 0; i < number_change; i++ {
			if lr_char == "R" {
				// add
				//fmt.Printf("adding %v\n", number_change)
				current_number += 1
				current_number = current_number % 100

				if current_number == 0 {
					zero_counter += 1
					// fmt.Printf("zero added")
				}

			} else if lr_char == "L" {
				// sub
				//fmt.Printf("subbing %v\n", number_change)
				current_number -= 1
				//current_number = int(math.Abs(float64(current_number)))
				current_number = current_number % 100

				if current_number == 0 {
					zero_counter += 1
					// fmt.Printf("zero added")
				}
			}
		}
		// fmt.Println("")
	}

	// fmt.Println("")
	fmt.Println("final zero value part2: ", zero_counter)
	return zero_counter
}

func readInput(filename string) (string, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return "", err
	}
	return string(data), nil
}
