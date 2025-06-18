#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
