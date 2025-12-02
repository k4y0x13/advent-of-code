package main

import "testing"

func TestPart1(t *testing.T) {
	sample := `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
`
	got := part1(sample)
	want := 3

	if got != want {
		t.Errorf("part1() = %v, want %v", got, want)
	}
}

func TestPart2(t *testing.T) {
	sample := `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
`
	got := part2(sample)
	want := 6

	if got != want {
		t.Errorf("part1() = %v, want %v", got, want)
	}
}
