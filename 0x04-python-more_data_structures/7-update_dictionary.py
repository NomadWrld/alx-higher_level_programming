#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the dictionary with the new key-value pair
    a_dictionary[key] = value
    return (a_dictionary)

# Test the function
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

    # Test case 1
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print("Updated Dictionary:")
    print_sorted_dictionary(new_dict)
    print("--")
    print("Original Dictionary:")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    # Test case 2
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print("Updated Dictionary:")
    print_sorted_dictionary(new_dict)
    print("--")
    print("Original Dictionary:")
    print_sorted_dictionary(a_dictionary)

