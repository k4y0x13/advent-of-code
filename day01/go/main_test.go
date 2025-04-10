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
			name: "example 1",
			input: `sample,
		input
		here`,
			expected: 42,
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
			name: "example 1",
			input: `sample,
		input
		here`,
			expected: 42,
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
