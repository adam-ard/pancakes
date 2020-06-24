package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func base(s string) int {
	if s[0] == '-' {
		return 1
	} else {
		return 0
	}
}

// While simpler recursion is between 3-4 time slower, so I use the
//   iterative solution below. But I keep this here for reference.
func nFlipsRecursive(s string) int {
	// handle base case, single letter strings
	if len(s) == 1 {
		return base(s)
	}

	if s[0] != s[1] {
		return nFlipsRecursive(s[1:]) + 1
	}
	return nFlipsRecursive(s[1:])
}

func nFlips(s string) int {
	// count the flips
	count := 0
	for i := 0; i < len(s)-1; i++ {
		if s[i] != s[i+1] {
			count++
		}
	}

	// check if last one is a flip
	if s[len(s)-1] == '-' {
		count++
	}

	return count
}

func main() {
	// get filename from commandline
	testFile := os.Args[1]

	// read the data from file
	data, _ := ioutil.ReadFile(testFile)

	// split into lines
	lines := strings.Split(string(data), "\n")

	// exclude the first line
	tests := lines[1:]

	// iterate through all test cases
	for i, test := range tests {
		if test != "" {
			fmt.Printf("Case #%d: %d\n", i+1, nFlips(test))
		}
	}

}
