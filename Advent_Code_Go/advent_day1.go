// Main Package - Used to group functions
package main

// Prints to console
import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func singleDiff(f []int64) {
	var tot_sum = 0
	c := f[0]
	for _, value := range f {
		if value-c > 0 {
			tot_sum += 1
		}
		c = value
	}
	fmt.Println(tot_sum)
}

func t_sum(v []int64) int64 {
	var sum int64 = 0
	for _, val := range v {
		sum += val
	}
	return sum
}

func tripleDiff(f []int64) {
	c := t_sum(f[0:3])
	var tot_sum = 0
	for i := 1; i < len(f)-2; i++ {
		a := t_sum(f[i : i+3])
		if a-c > 0 {
			tot_sum += 1
		}
		c = a
	}
	fmt.Println((tot_sum))
}

// Main function runs when running the main package
func main() {
	var f_int []int64

	f, err := ioutil.ReadFile("input1.txt")
	f_str := strings.Fields(string(f))
	check(err)

	//Convert to STR array
	for _, fs := range f_str {
		intVar, _ := strconv.ParseInt(fs, 0, 64)
		f_int = append(f_int, intVar)
	}

	singleDiff(f_int)
	tripleDiff(f_int)

}
