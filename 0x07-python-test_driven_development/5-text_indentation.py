#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of the characters '.', '?', and ':'.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in the text
    for i, char in enumerate(text):
        # If the current character is a delimiter, add it to the result
        # and add two newlines after it
        if char in ".?:":
            result += char + "\n\n"
        # If the current character is a space, add it to the result if
        # it is not immediately after a delimiter
        elif char == " ":
            if text[i - 1] not in ".?:":
                result += char
        # Otherwise, add the character to the result as-is
        else:
            result += char

    # Print the result, stripping leading and trailing spaces from each line
    for line in result.split("\n"):
        print(line.strip())

