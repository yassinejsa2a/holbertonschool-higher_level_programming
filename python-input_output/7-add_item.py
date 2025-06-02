#!/usr/bin/python3


import json
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


filename = "add_item.json"
def add_item(item):
    """Add an item to a JSON file."""
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.append(item)
    save_to_json_file(items, filename)
