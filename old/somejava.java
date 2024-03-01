1. public class Main {
2.    public static void main(String[] args) {
3.        System.out.println("Hello, World!");
4.        
5.        // Declare variables
6.        int x = 5;
7.        int y = 10;
8.        int sum = x + y;
9.        
10.        // Print the sum
11.        System.out.println("The sum of x and y is: " + sum);
12.        
13.        // Create a loop to print numbers from 1 to 10
14.        for (int i = 1; i <= 10; i++) {
15.            System.out.println(i);
16.        }
17.        
18.        // Use if-else statement to check if x is greater than y
19.        if (x > y) {
20.            System.out.println("x is greater than y");
21.        } else {
22.            System.out.println("y is greater than x");
23.        }
24.        
25.        // Define a method to calculate the square of a number
26.        int square(int num) {
27.            return num * num;
28.        }
29.        
30.        // Call the square method and print the result
31.        System.out.println("The square of 5 is: " + square(5)); 
32.    }
33.}
