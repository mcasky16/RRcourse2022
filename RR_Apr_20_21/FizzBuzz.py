# Exercise 1
# ----------

# Consider a FizzBuzz problem. The program should write numbers from 1 to 100,
# separated by a newline, but multiples of 3 and of 5 should be replaced with “Fizz” and “Buzz”
# respectively. For numbers which are multiples of both 3 and 5 print “FizzBuzz”

for i in range(1,101):  # Defines the numbers in range between 1 to 100 in a loop
    
    # Checks if 3 and is 5 are multiples of the number and Prints 'FizzBuzz'
    if (i % 3 == 0) and (i % 5) == 0:  
        print('FizzBuzz') 
    
    # If not check if 3 is a multiple of the number and Prints 'Fizz'
    elif i % 3 == 0:
        print('Fizz')
    
    # If not check if 5 is a multiple of the number and Prints 'Buzz'
    elif i % 5 == 0:
        print('Buzz')
        
    # If all above statements are false the print the number.
    else:
        print(i)
  
    
    
