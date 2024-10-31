package main

import ( "fmt" )

func main() { // declare variables var num1, num2 int var result int

// get user input
fmt.Print("Enter first number: ")
fmt.Scanln(&num1)

fmt.Print("Enter second number: ")
fmt.Scanln(&num2)

// perform addition
result = num1 + num2

// display result
fmt.Printf("The sum of %d and %d is %d\n", num1, num2, result)

// check if result is even or odd
if result%2 == 0 {
	fmt.Printf("The sum is even\n")
} else {
	fmt.Printf("The sum is odd\n")
}
}
