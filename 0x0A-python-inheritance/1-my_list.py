#!/usr/bin/python3

class MyList(list):
    """
    A custom list class inheriting from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)  # Sort the list in ascending order
        print(sorted_list)          # Print the sorted list

# Test the implementation
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)         # Output: [1, 4, 2, 3, 5]
    my_list.print_sorted() # Output: [1, 2, 3, 4, 5]
    print(my_list)         # Output: [1, 4, 2, 3, 5]
