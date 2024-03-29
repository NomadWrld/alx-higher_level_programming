#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(*("{:d}".format(col) for col in row), sep=" ")

if __name__ == "__main__":
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
