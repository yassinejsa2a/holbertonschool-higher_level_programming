#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
