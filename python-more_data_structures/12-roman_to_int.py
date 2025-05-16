#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if roman_string[i] in dict:
            if i > 0 and dict[roman_string[i]] > dict[roman_string[i - 1]]:
                result += dict[roman_string[i]] - 2 * dict[roman_string[i - 1]]
            else:
                result += dict[roman_string[i]]
    return (result)
