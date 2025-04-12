package main

import (
	"testing"
)

func TestSolvePart1(t *testing.T) {
	// struct of array test cases
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "sample 1",
			input:    "2x3x4",
			expected: 58,
		},
		{
			name:     "sample 2",
			input:    "1x1x10",
			expected: 43,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			restult := SolvePart1(tc.input)
			if restult != tc.expected {
				t.Errorf("expected %d, got %d", tc.expected, restult)
			}
		})
	}
}

func TestSolvePart2(t *testing.T) {
	// struct of array test cases
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "sample 1",
			input:    "2x3x4",
			expected: 34,
		},
		{
			name:     "sample 2",
			input:    "1x1x10",
			expected: 14,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			restult := SolvePart2(tc.input)
			if restult != tc.expected {
				t.Errorf("expected %d, got %d", tc.expected, restult)
			}
		})
	}
}
