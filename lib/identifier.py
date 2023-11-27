def exactly_two_positive(a, b, c):
    count_positive = 0
    if a > 0:
        count_positive += 1
    if b > 0:
        count_positive += 1
    if c > 0:
        count_positive += 1

    result = count_positive == 2
    print(f"For inputs {a}, {b}, {c}: {result}")
    return result


print(exactly_two_positive(2, 4, -3))  
print(exactly_two_positive(-4, 6, 8))  
print(exactly_two_positive(4, -6, 9))  
print(exactly_two_positive(-4, 6, 0))  
