package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Test")

	// Read from input.txt
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
	}
	defer file.Close()

	// Go through file line by line
	reader := bufio.NewReader(file)

	global_total_area := 0
	for {

		string_slice_with_new_line, err := reader.ReadString('\n') // Delim String in parameters
		string_slice := strings.TrimSuffix(string_slice_with_new_line, "\n")

		if err != nil {
			// When you reach EOF break
			if err == io.EOF {
				break // End of File
			}
			fmt.Println("Error reading character", err)
		}

		fmt.Println("string slice:", string_slice)
		// Start of Solution
		// NOTE: STEP 2: Split string into l, w, h and calculate Surface Area
		length_width_height := strings.Split(string_slice, "x")
		length, err := strconv.Atoi(length_width_height[0])
		width, err := strconv.Atoi(length_width_height[1])
		height, err := strconv.Atoi(length_width_height[2])
		if err != nil {
			fmt.Println("Error converting str to int", err)
		}

		// TEST: Just Debugging
		// first := 2 * length * width
		// second := 2 * width * height
		// third := 2 * height * length
		//
		// fmt.Println("first, second, thrid", first, second, third)

		surface_area := (2 * length * width) + (2 * width * height) + (2 * height * length)
		fmt.Println("Surface Area:", surface_area)

		// NOTE: Step 3: Calculate slack
		// It can only be three possibilities (only one can be max)
		slack := 0
		if length > height && length > width {
			slack = height * width
		} else if width > height && width > length {
			slack = length * height
		} else if height > length && height > width {
			slack = length * width
		}
		fmt.Println("slack:", slack)

		total_surface_area := slack + surface_area
		fmt.Println("total surface area:", total_surface_area)

		// NOTE: Step 4: Sum up the total area
		global_total_area = global_total_area + total_surface_area
	}

	fmt.Println("Total Area overall:", global_total_area)

}
