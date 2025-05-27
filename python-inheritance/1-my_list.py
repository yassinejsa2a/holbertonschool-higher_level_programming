#!/usr/bin/python3



class Mylist(list):
    """A class that inherits from list and adds a method to print the sorted list."""
    
    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
