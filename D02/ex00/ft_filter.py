#!/usr/bin/env python
import sys
import traceback


def ft_filter(function_to_apply, list_of_inputs):
    if not list_of_inputs:
        return None
    if function_to_apply:
        return (inp for inp in list_of_inputs if function_to_apply(inp))
    return (inp for inp in list_of_inputs if inp)


if __name__ == '__main__':
    def is_even(n=int()):
        return n % 2 == 0

    def is_odd(n=int()):
        return n % 2 == 1

    lst = (1, 2, 3, 6)
    print("_____with function even_____on: {}".format(lst))
    for el in ft_filter(is_even, lst):
        print(el)
    print("_____with function odd_____")
    for el in ft_filter(is_odd, lst):
        print(el)
    lst = [1, 2, 'a', 1 == 1, 2 == 2, 3 == 5, ('toto', 'titi'), 'tut' == 'tat']
    print("_____without function_____ on : {}".format(lst))
    for el in ft_filter(None, lst):
        print(el)
    print("_____with function_____but no list")
    try:
        for el in ft_filter(is_even, None):
            print(el)
    except Exception:
        traceback.print_exc(file=sys.stderr)
    print("____vs real filter___")
    for el in filter(is_even, None):
        print(el)
