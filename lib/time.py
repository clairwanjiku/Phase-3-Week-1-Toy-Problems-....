def converter_to_24_hour(hour, minute, period):
    # Check if the period is "am"
    if period == "am":
        # If it's 12 am, convert hour to 0
        if hour == 12:
            hour = 0
    else:
        # If it's "pm" and not 12 pm, add 12 to the hour
        if hour != 12:
            hour += 12

    # Formatting the time into a four-digit string
    result = f"{hour:02d}{minute:02d}"
    
    # Display the 24-hour format
    print(f"The 24-hour format is: {result}")

    return result


# example
print(converter_to_24_hour(8, 30, "am"))  # Output: 0830
print(converter_to_24_hour(8, 30, "pm"))  # Output: 2030