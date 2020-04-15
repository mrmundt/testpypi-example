"""
Utils:
    Utilities to be use with nose2
"""

import sys

def category(*args, **kwargs):
    """
    Decorator that adds attributes to classes or functions
    for use with the nose2 Attribute (-A) plugin.
    """
    def wrap_ob(ob):
        for name in args:
            setattr(ob, name, True)
        if sys.version_info < (3, 4):
            for name, value in kwargs.iteritems():
                setattr(ob, name, value)
        else:
            for name, value in kwargs.items():
                setattr(ob, name, value)
        return ob
    return wrap_ob
