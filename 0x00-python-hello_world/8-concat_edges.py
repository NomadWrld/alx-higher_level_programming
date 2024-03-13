#!/usr/bin/python3

# Define the string
str = "Python is an interpreted, interactive, object-oriented programming \
        language that combines remarkable power with very clear syntax"

# Extract the required parts and concatenate them
str = str[39:66] + str[106:112] + str[:6]

# Print the result
print(str)
