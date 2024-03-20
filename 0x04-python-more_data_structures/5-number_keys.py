#!/usr/bin/python3
def number_keys(a_dictionary):
    # Count the number of keys in the dictionary
    num_keys = len(a_dictionary)
    return (num_keys)

# Test the function
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys:", nb_keys)

