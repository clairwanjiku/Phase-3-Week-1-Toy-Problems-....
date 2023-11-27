def zodiac(word):
    # Define the vowels
    vowels = "aeiou"
    
    # Initialize variables for maximum and current value of consonant substrings
    max_value = current_value = 0

    # Iterate through each letter in the word
    for letter in word:
        # Check if the letter is a consonant
        if letter not in vowels:
            # Calculate the value of the consonant letter and add it to the current value
            current_value += ord(letter) - ord('a') + 1
        else:
            # If a vowel is encountered, update the maximum value and reset the current value
            max_value = max(max_value, current_value)
            current_value = 0

    # Return the maximum value found among consonant substrings
    return max(max_value, current_value)

# example
print(zodiac("zodiacs"))   # Output: 26
print(zodiac("strength"))  # Output: 57
