1. package main
2. 
3. import (
4. 	"fmt"
5. )
6. 
7. func main() {
8. 	fmt.Println("Hello, World!")
9. }
10. 
11. type Person struct {
12. 	Name string
13. 	Age  int
14. }
15. 
16. func (p *Person) sayHello() {
17. 	fmt.Printf("Hello, my name is %s and I am %d years old\n", p.Name, p.Age)
18. }
19. 
20. func add(a, b int) int {
21. 	return a + b
22. }
23. 
24. func multiply(a, b int) int {
25. 	return a * b
26. }
27. 
28. func fibonacci(n int) int {
29. 	if n <= 1 {
30. 		return n
31. 	}
32. 	return fibonacci(n-1) + fibonacci(n-2)
33. }
34. 
35. func main() {
36. 	p := Person{Name: "Alice", Age: 30}
37. 	p.sayHello()
38. 
39. 	fmt.Println(add(10, 5))
40. 	fmt.Println(multiply(5, 3))
41. 
42. 	fmt.Println("Fibonacci sequence:")
43. 	for i := 0; i < 10; i++ {
44. 		fmt.Println(fibonacci(i))
45. 	}
46. }
47. 
48. type Animal interface {
49. 	Speak() string
50. }
51. 
52. type Dog struct{}
53. 
54. func (d Dog) Speak() string {
55. 	return "Woof!"
56. }
57. 
58. type Cat struct{}
59. 
60. func (c Cat) Speak() string {
61. 	return "Meow!"
62. }
63. 
64. func main() {
65. 	animals := []Animal{Dog{}, Cat{}}
66. 
67. 	for _, animal := range animals {
68. 		fmt.Println(animal.Speak())
69. 	}
70. }
