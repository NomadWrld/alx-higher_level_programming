#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set()

    # Iterate through each integer in the list
    for integer in my_list:
        # Add the integer to the set (sets only store unique elements)
        unique_integers.add(integer)

    # Sum up all the unique integers in the set
    result = sum(unique_integers)

    return (result)

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result:", result)

