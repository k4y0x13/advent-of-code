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
		if len(start_end) < 2 {
			continue
		}
		start_str := start_end[0]
		end_str := start_end[1]
		// fmt.Println("\nrange:", range_value, "\nstart:", start_str, "\nend:", end_str)
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
			// fmt.Println("Comparing:", i_str[:mid_index], "with: ", i_str[mid_index:])
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

	// fmt.Println("Total sum:", total_sum)
	return total_sum
}

// the problem changes to n-repeated subsequence
func part2(input string) int {
	total_sum := 0

	ranges := strings.Split(input, ",")
	for _, value := range ranges {
		each_range := strings.Split(value, "-")
		if len(each_range) < 2 {
			continue
		}

		start_str := each_range[0]
		end_str := each_range[1]
		fmt.Printf("converting start str %v and end str %v", start_str, end_str)
		start_int, err := strconv.Atoi(start_str)
		if err != nil {
			log.Fatal("cannot convert start str to int")
		}
		end_int, err := strconv.Atoi(end_str)
		if err != nil {
			log.Fatal("cannot convert end str to int")
		}

		// for each number in the range
	each_number_loop:
		for each_number := start_int; each_number <= end_int; each_number++ {
			each_number_str := strconv.Itoa(each_number)
			// 1. check if it's a multiple
			// 0 till length of str half

			for win_size := 1; win_size <= (len(each_number_str) / 2); win_size++ {
				// fmt.Printf("\nlength of number str: %v\n", len(each_number_str))
				if len(each_number_str)%win_size != 0 { // if it's not a multiple
					// not, so continue
					continue
				}
				// then it's divisible
				// add every subdivisions into set
				// create an empty set and add each substring the divisions into the set
				set := make(map[string]struct{}) // map of string to struct?
				var void struct{}

				// adding items: set["apple"] = void
				// checking for existence: _, exists = set["grape"])
				// the exist variable would be either true or false
				// delete: delete(set, "banana")
				// print: for element:= range set{fmt.print(element)}

				// divide string into substrings with the given win_size and add to them
				sub_div_start_index := 0
				fmt.Println("\nwin size: ", win_size)
				fmt.Println("each number in consideration: ", each_number_str)
				for sub_div_index := win_size; sub_div_index < len(each_number_str)+1; sub_div_index += win_size {
					fmt.Printf("sub_div  start: %v, sub_div end: %v\n", sub_div_start_index, sub_div_index)
					set[each_number_str[sub_div_start_index:sub_div_index]] = void
					sub_div_str := each_number_str[sub_div_start_index:sub_div_index]
					fmt.Println("subdivision: ", sub_div_str)
					sub_div_start_index += win_size - 1
					fmt.Printf("length of set: %v\n", len(set))
					fmt.Println("set: ", set)
					if len(set) == 1 {
						fmt.Printf("\n=====\nadding %v to total sum %v\n=====\n", each_number, total_sum)
						total_sum += each_number
						break each_number_loop
					}
				}

			}

		}
		//
	}

	// fmt.Println("Total sum:", total_sum)
	fmt.Println("")
	return total_sum
}

func readInput(filename string) (string, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return "", err
	}

	return string(data), nil
}
