def is_palindrome(word: str) -> bool:
    # Convert the word to lowercase
    word = word.lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Example usage
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("Python"))   # Output: False
