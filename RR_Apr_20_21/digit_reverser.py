# Exercise 2(b)
# -------------

# Write a function which reverses digits in an integer number (for example 7245 -> 5427).
# The function should be documented, with type hints, and appropriate comments.

def digits_reverser(number: int) -> int:
    """
    This function returns the digits of a number starting from the last digit to the first.
    """
    num_to_string = str(number)  # Converts the number to a string
    
    num_to_string = num_to_string[::-1] # Reverses the character in the string
    
    reversed_number = int(num_to_string) # Converts number back to integer
    
    print(reversed_number)

# Example
digits_reverser(12345)
    
    