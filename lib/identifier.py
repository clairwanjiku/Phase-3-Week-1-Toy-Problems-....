def exactly_two_positive(a, b, c):
    # Count the number of positive integers
    positives = sum(x > 0 for x in [a, b, c])

    # Return True if exactly two integers are positive, False otherwise
    return positives == 2

# example

print(exactly_two_positive(2, 4, -3))    # Output: True
print(exactly_two_positive(-4, 6, 8))    # Output: True
print(exactly_two_positive(4, -6, 9))    # Output: True
print(exactly_two_positive(-4, 6, 0))    # Output: False
