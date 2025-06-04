#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file."""
import json


def class_to_json(obj):
    """Return the dictionary"""
    return obj.__dict__ if hasattr(obj, "__dict__") else obj
