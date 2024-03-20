#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is not empty and has at least one key-value pair
    if a_dictionary:
        # Get the key with the maximum value
        best_key = max(a_dictionary, key=a_dictionary.get)
        return (best_key)
    else:
        return (None)

# Test the function
if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score:", best_key)

    best_key = best_score(None)
    print("Best score:", best_key)

