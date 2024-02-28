package main

import "fmt"

func main() {
    var a int = 5
    var b int = 10

    sum := a + b
    fmt.Println("Sum:", sum)

    if sum > 10 {
        fmt.Println("Sum is greater than 10")
    } else {
        fmt.Println("Sum is less than or equal to 10")
    }

    for i := 0; i < 5; i++ {
        fmt.Println("Index:", i)
    }

    array := [3]int{1, 2, 3}
    for i, value := range array {
        fmt.Printf("Index: %d, Value: %d\n", i, value)
    }

    x := 0
    for x < 5 {
        fmt.Println("x is less than 5")
        x++
    }

    var y int
    for {
        y++
        if y > 10 {
            break
        }
        fmt.Println("Value of y:", y)
    }

    switch sum {
    case 15:
        fmt.Println("Sum is 15")
    case 20:
        fmt.Println("Sum is 20")
    default:
        fmt.Println("Sum is not 15 or 20")
    }

    result := add(a, b)
    fmt.Println("Result of addition function:", result)
}

func add(x, y int) int {
    return x + y
}
