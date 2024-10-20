package main

import (
	"bufio" // Buffered I/O operations
	"fmt"   // Formatting to output
	"io"
	"os" // OS functionalities
)

func main() {
	fmt.Println("test")

	// Read from input.txt:
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
	}
	defer file.Close() // Runs after main has finished executing.

	reader := bufio.NewReader(file)

	floor_counter := 0
	character_position := 1
	for { // Infinite loop

		char, _, err := reader.ReadRune() // Correctly handles multi-byte chars in UTF-8 texts
		// Prefered over ReadByte

		if err != nil {
			if err == io.EOF {
				break // End of file reached
			}
			fmt.Println("Error reading character:", err)
			return
		}

		// fmt.Printf("%c\n", char)
		if char == '(' {
			floor_counter += 1
		} else if char == ')' {
			floor_counter -= 1
		}

		if floor_counter == -1 {
			break
		} else {
			character_position += 1
		}
		// fmt.Println("Current floor counter:", floor_counter)
	}

	fmt.Println("Final Floor:", floor_counter)
	fmt.Println("Position for -1", character_position)
}
