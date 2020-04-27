#!/usr/bin/env python
from Vector import Vector


def math_methods_tests():
    mm_test_add()
    mm_test_sub()


def mm_test_add():
    v1 = Vector([1, 2, 3, 4, 5])
    v2 = Vector([5, 4, 3, 2, 1])
    print(repr(v1))
    print(repr(v2))
    v3 = v1 + v2
    print(repr(v3))
    # test error
    v4 = Vector(8)
    print(repr(v4))

    try:
        v5 = v3 + v4
        print(repr(v5))
    except ValueError as e:
        print(e)

    try:
        v5 = v3 + 10
        print(repr(v5))
    except ValueError as e:
        print(e)

    try:
        v5 = 10 + v3
        print(repr(v5))
    except ValueError as e:
        print(e)

    v6 = v1 + v2 + v3
    print(repr(v6))

def mm_test_sub():
    v1 = Vector([1, 2, 3, 4, 5])
    v2 = Vector([5, 4, 3, 2, 1])
    print(repr(v1))
    print(repr(v2))
    v3 = v1 - v2
    print(repr(v3))
    # test error
    v4 = Vector(8)
    print(repr(v4))

    try:
        v5 = v3 - v4
        print(repr(v5))
    except ValueError as e:
        print(e)

    try:
        v5 = v3 - 10
        print(repr(v5))
    except ValueError as e:
        print(e)

    try:
        v5 = 10 - v3
        print(repr(v5))
    except ValueError as e:
        print(e)

    v6 = v1 - v2 - v3
    print(repr(v6))



def init_tests():
    i_test_list()
    i_test_range()
    i_test_size()
    i_test_empty()


def i_test_list():
    vector = Vector([1, 2, 3, 4, 5])
    print(vector)
    print(repr(vector))
    # trunc to size
    vector = Vector([1, 2, 3, 4, 5], 2)
    print(vector)
    print(repr(vector))
    # trunc to size from end
    vector = Vector([1, 2, 3, 4, 5], -2)
    print(vector)
    print(repr(vector))
    # scalar
    vector = Vector([1])
    print(vector)
    print(repr(vector))


def i_test_range():
    vector = Vector((10, 15))
    print(vector)
    print(repr(vector))


def i_test_size():
    vector = Vector(3)
    print(vector)
    print(repr(vector))


def i_test_empty():
    vector = Vector()
    print(vector)
    print(repr(vector))


if __name__ == '__main__':
    init_tests()
    math_methods_tests()