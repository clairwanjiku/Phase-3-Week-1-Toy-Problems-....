def two_positive(a, b, c):
    # Count the number of positive integers
    positives = sum(x > 0 for x in [a, b, c])

    # Return True if exactly two integers are positive, False otherwise
    return positives == 2

# example

print(two_positive(2, 4, -3))    
print(two_positive(-4, 6, 8))    
print(two_positive(4, -6, 9))    
print(two_positive(-4, 6, 0))   
