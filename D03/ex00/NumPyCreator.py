#!/usr/bin/env python
import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(self, lst):
        """takes in a list and returns its corresponding NumPy array."""
        return np.array(lst)

    def from_tuple(self, tpl):
        """takes in a tuple and returns its corresponding NumPy array."""
        return np.array(tpl)

    def from_iterable(self, itr, dtype=None):
        """takes in an iterable and returns an array which contains all of its
        elements."""
        return np.fromiter(itr, dtype)

    def from_shape(self, shape, value=0, dtype=None):
        """returns an array filled with the same value.
        The first argument is a tuple which specifies the shape of the array,
        and the second argument specifies the value of all the elements. This
        value must be 0 by default."""
        return np.full(shape, value, dtype)

    def random(self, shape):
        """returns an array filled with random values.
        It takes as an argument a tuple which specifies the shape of the
        array."""
        return np.random.rand(*shape)

    def identity(self, n, dtype=None):
        """returns an array representing the identity matrix of size n."""
        return np.identity(n, dtype)


if __name__ == "__main__":
    npc = NumPyCreator()
    mat = npc.from_list([[1, 2, 3], [6, 3, 4]])
    print("{}({})".format(type(mat), mat))
    mat = npc.from_tuple(("a", "b", "c"))
    print("{}({})".format(type(mat), mat))
    mat = npc.from_iterable(range(5))
    print("{}({})".format(type(mat), mat))
    shape = (3, 5)
    mat = npc.from_shape(shape)
    print("{}({})".format(type(mat), mat))
    mat = npc.random(shape)
    print("{}({})".format(type(mat), mat))
    mat = npc.identity(4)
    print("{}({})".format(type(mat), mat))
    mat = npc.identity(4, int)
    print("{}({})".format(type(mat), mat))
