package main

import (
	"fmt"
	"os"
	"io/ioutil"
	"strings"
)

func nFlips(s string) int {
	if len(s) == 1 {
		if s[0] == '-' {
			return 1
		} else {
			return 0
		}
	}

	count := 0
	for i := 0; i < len(s) - 1; i++ {
		if s[i] != s[i+1] {
			count++
		}
	}

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
	
	for i, test := range tests {
		if (test != "") {
			fmt.Printf("Case #%d: %d\n", i+1, nFlips(test))
		}
	}
	
}
