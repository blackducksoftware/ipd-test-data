package main

import (
    "fmt"
)

func main() {
    // Define a struct type for a Person
    type Person struct {
        Name string
        Age  int
    }

    // Create a new instance of Person
    p := Person{Name: "Alice", Age: 30}

    // Print out the person's name and age
    fmt.Println("Name:", p.Name)
    fmt.Println("Age:", p.Age)

    // Increment the person's age
    p.Age++

    // Print out the person's new age
    fmt.Println("New Age:", p.Age)

    // Define a slice of integers
    numbers := []int{1, 2, 3, 4, 5}

    // Loop through the numbers and print them out
    for i, num := range numbers {
        fmt.Printf("Number %d: %d\n", i, num)
    }

    // Define a map of strings to integers
    names := map[string]int{
        "Alice": 30,
        "Bob":   35,
        "Charlie": 40,
    }

    // Loop through the names and ages and print them out
    for name, age := range names {
        fmt.Printf("%s is %d years old\n", name, age)
    }

    // Declare a new variable and assign it a value
    x := 10

    // Use a switch statement based on the value of x
    switch x {
    case 5:
        fmt.Println("x is 5")
    case 10:
        fmt.Println("x is 10")
    default:
        fmt.Println("x is neither 5 nor 10")
    }

    // Define a function that takes two integers and returns their sum
    add := func(a, b int) int {
        return a + b
    }

    // Call the function and print out the result
    sum := add(3, 4)
    fmt.Println("Sum:", sum)
}
