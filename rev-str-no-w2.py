def reverse_except_w(input_string):
    words = input_string.split()
    result = ''
    
    for word in words:
        if word.startswith('w'):
            result += word + ' '
        else:
            result += word[::-1] + ' '
    
    return result.strip()

# Test the function
input_string = "hello world welcome to python programming"
output_string = reverse_except_w(input_string)
print(output_string)
