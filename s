def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n-1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Get input from the user
num_terms = int(input("Enter the number of Fibonacci terms you want to generate: "))
fib_sequence = fibonacci(num_terms)

print("Fibonacci Sequence up to", num_terms, "terms:")
for i in fib_sequence:
    print(i, end=" ")


When you run this program, it will prompt the user to enter the number of Fibonacci terms they want to generate and then output the Fibonacci sequence up to that number of terms using recursion. The fibonacci() function recursively computes each term based on the previous two terms until the desired number of terms is reached.
