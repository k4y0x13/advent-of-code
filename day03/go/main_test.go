package main

import "testing"

func TestSolvePart1(t *testing.T) {

	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "2 chars",
			input:    "^v",
			expected: 3,
		},
		{
			name:     "4 chars square",
			input:    "^>v<",
			expected: 3,
		},
		{
			name:     "up down ",
			input:    "^v^v^v^v^v",
			expected: 11,
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
