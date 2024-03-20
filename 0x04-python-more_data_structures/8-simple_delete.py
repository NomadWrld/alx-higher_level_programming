#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Delete the key-value pair if the key exists
        del a_dictionary[key]
    return (a_dictionary)

# Test the function
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}

    # Test case 1
    new_dict = simple_delete(a_dictionary, 'track')
    print("Original Dictionary:")
    print_sorted_dictionary(a_dictionary)
    print("--")
    print("Modified Dictionary:")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")

    # Test case 2
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print("Original Dictionary:")
    print_sorted_dictionary(a_dictionary)
    print("--")
    print("Modified Dictionary:")
    print_sorted_dictionary(new_dict)
