package main

import (
	"testing"
)

func TestSolvePart1(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "sample 1",
			input:    `(())`,
			expected: 0,
		},
		{
			name:     "sample 2",
			input:    `(((`,
			expected: 3,
		},
		{
			name:     "sample 3",
			input:    `())`,
			expected: -1,
		},
		// add more test cases as needed.
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := SolvePart1(tc.input)

			if result != tc.expected {
				t.Errorf("expected %d, got %d", tc.expected, result)
			}
		})
	}
}

func TestSolvePart2(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "sample 1",
			input:    `)`,
			expected: 1,
		},
		{
			name:     "sample 2",
			input:    `()())`,
			expected: 5,
		},
		// add more test cases as needed.
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := SolvePart2(tc.input)

			if result != tc.expected {
				t.Errorf("expected %d, got %d", tc.expected, result)
			}
		})
	}
}
