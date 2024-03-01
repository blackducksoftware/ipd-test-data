1. package main

2. import (
3. 	"fmt"
4. )

5. func main() {
6. 	fmt.Println("Hello, World!")
7. }

8. type Person struct {
9. 	Name string
10.	Age int
11.}

12. func (p *Person) greet() {
13.	fmt.Println("Hello,", p.Name)
14.}

15. func add(a, b int) int {
16. 	return a + b
17.}

18. func multiply(a, b int) int {
19.	return a * b
20.}
