1. public class Main {
2.     public static void main(String[] args) {
3.         int num1 = 5;
4.         int num2 = 10;
5.         int sum = num1 + num2;
6.         System.out.println("The sum of " + num1 + " and " + num2 + " is: " + sum);
7.         
8.         String name = "Jane";
9.         System.out.println("Hello, " + name + "!");
10.         
11.         double radius = 5.0;
12.         double area = Math.PI * radius * radius;
13.         System.out.println("The area of a circle with radius " + radius + " is: " + area);
14.         
15.         int[] numbers = {1, 2, 3, 4, 5};
16.         for (int i = 0; i < numbers.length; i++) {
17.             System.out.println(numbers[i]);
18.         }
19.         
20.         String[] fruits = {"apple", "banana", "orange"};
21.         for (String fruit : fruits) {
22.             System.out.println(fruit);
23.         }
24.         
25.         int x = 10;
26.         if (x > 0) {
27.             System.out.println("x is positive");
28.         } else {
29.             System.out.println("x is non-positive");
30.         }
31.     }
32. }
