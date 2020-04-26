import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(lst):
        """takes in a list and returns its corresponding NumPy array."""
        return np.matric(lst)

    def from_tuple(tpl):
        """takes in a tuple and returns its corresponding NumPy array."""
        pass

    def from_iterable(itr):
        """takes in an iterable and returns an array which contains all of its
        elements."""
        pass

    def from_shape(shape, value):
        """returns an array filled with the same value.
        The first argument is a tuple which specifies the shape of the array,
        and the second argument specifies the value of all the elements. This
        value must be 0 by default."""
        pass

    def random(shape):
        """returns an array filled with random values.
        It takes as an argument a tuple which specifies the shape of the
        array."""
        pass

    def identity(n):
        """returns an array representing the identity matrix of size n."""
        pass


if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    shape = (3, 5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))
