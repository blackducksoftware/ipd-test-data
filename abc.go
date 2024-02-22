package main

import (
	"fmt"
)

func main() {
	// Declare variables
	var name string
	var age int

	// Assign values to variables
	name = "Alice"
	age = 30

	// Print out the values
	fmt.Println("Name:", name)
	fmt.Println("Age:", age)

	// Increment age
	age++

	// Print incremented age
	fmt.Println("After incrementing age:", age)

	// Declare and initialize a new variable
	var country string = "USA"

	// Print out the country
	fmt.Println("Country:", country)

	// Declare multiple variables at once
	var (
		city    string = "New York"
		address string = "123 Main Street"
	)

	// Print out city and address
	fmt.Println("City:", city)
	fmt.Println("Address:", address)

	// Check if age is greater than 18
	if age > 18 {
		fmt.Println("Adult")
	} else {
		fmt.Println("Minor")
	}

	// Create a simple loop
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Declare a function
	func greet() {
		fmt.Println("Hello, World!")
	}

	// Call the function
	greet()
}