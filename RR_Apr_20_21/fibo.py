# Exercise 2
# ----------

# Write a function which takes n (float or integer) as a parameter and returns the largest
# Fibonacci number smaller than n. The function should be documented, with type hints, and
# appropriate comments.

def fibonacci(n) -> int:
    """
    This function returns the largest fibonacci number smaller than the number you input in
    the function.
    It can either take a float or an integer and changes the class back to interger. 
    """
    # Created a list and place the first two fibonacci sequence in it since they are constant
    n1, n2 = 0, 1
    result_list = [n1,n2]

    # This while loop collects the fibonacci sequence and add to the list
    while result_list[-1] < n:
        nth = n1 + n2  #creates the last term in the sequence
        
        # udating the values
        n1 = n2
        n2 = nth
        result_list += [nth]

    print(f"The largest fibonnacci number smaller than {n} is {result_list[-2]}")  #result_list[-2] shows the last but 1 item in the list.
    
# Example
fibonacci(30)