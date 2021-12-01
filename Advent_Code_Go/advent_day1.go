// Main Package - Used to group functions
package main

// Prints to console
import (
	//"bufio"
	"fmt"
	//"io"
	"os"
	"rsc.io/quote"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// Main function runs when running the main package
func main() {
	fmt.Println("Hello,World!")
	fmt.Println(quote.Go())

	f, err := os.ReadFile("input1.txt")
	check(err)

	for index, val := range f {
		fmt.Println(index)
		fmt.Println(val)
	}

}
