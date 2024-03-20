#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store multiplied values
    new_dictionary = {}

    # Iterate through the original dictionary and multiply each value by 2
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2

    return (new_dictionary)

# Test the function
if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print("Original Dictionary:")
    print_sorted_dictionary(a_dictionary)
    print("--")
    print("Modified Dictionary:")
    print_sorted_dictionary(new_dict)

