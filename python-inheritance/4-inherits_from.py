#!/usr/bin/python3



def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.
    """
    return inssubclass (type(obj , a_class))
