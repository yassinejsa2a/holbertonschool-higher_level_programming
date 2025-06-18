#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.
    """
    return json.loads(my_str)
