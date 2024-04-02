#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists element-wise.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The length of the resulting list.

    Returns:
        list: A new list with all divisions.
    """
    result = []
    for i in range(list_length):
        try:
            # Try to divide the elements if they are valid numbers
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    if my_list_2[i] != 0:
                        quotient = my_list_1[i] / my_list_2[i]
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            else:
                print("out of range")
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        finally:
            result.append(quotient)
    return (result)

# Test cases
if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

