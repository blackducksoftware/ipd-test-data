def greeting(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

print(greeting("Alice"))
print(add_numbers(5, 3))
print(multiply_numbers(4, 6))
print(check_even(8))
print(count_vowels("hello"))
print(calculate_factorial(5))
