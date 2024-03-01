package main

import ( "fmt" )

func main() { fmt.Println("Hello, World!")

// Variables
var num1 int = 10
var num2 int = 20
var sum int

sum = num1 + num2
fmt.Printf("Sum of %d and %d is %d\n", num1, num2, sum)

// Strings
name := "John"
fmt.Printf("Hello, %s\n", name)

// Arrays
var arr [5]int
arr[0] = 1
arr[1] = 2
arr[2] = 3
arr[3] = 4
arr[4] = 5

fmt.Println("Array:", arr)

// Slices
slice := []int{1, 2, 3, 4, 5}
fmt.Println("Slice:", slice)

// Loops
for i := 0; i < 5; i++ {
	fmt.Println(i)
}

// Functions
result := add(5, 3)
fmt.Println("Result of add function:", result)
}

func add(a, b int) int { return a + b }

func mul(a, b int) int { return a * b }

func sub(a, b int) int { return a - b }

func div(a, b int) int { return a / b }
