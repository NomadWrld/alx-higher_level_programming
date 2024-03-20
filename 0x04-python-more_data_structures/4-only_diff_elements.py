#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Find elements present in only one set using symmetric difference
    diff_elements = set_1 ^ set_2
    return (diff_elements)

# Test the function
if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
