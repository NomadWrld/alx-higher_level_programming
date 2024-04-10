#!/usr/bin/python3
"""
Module: 5-text_indentation

This module defines a function `text_indentation` that prints text with specified indentation rules.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    text (str): The input text.

    Raises:
    TypeError: If `text` is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = {'.', '?', ':'}
    result = ""
    line = ""

    for char in text:
        line += char
        if char in punctuations:
            result += line.strip() + "\n\n"
            line = ""

    if line:
        result += line.strip()

    print(result)
