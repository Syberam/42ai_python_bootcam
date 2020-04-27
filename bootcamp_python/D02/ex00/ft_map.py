#!/usr/bin/env python
import sys
import traceback


def ft_map(function_to_apply, list_of_inputs):
    if not list_of_inputs:
        return None
    if function_to_apply:
        return (function_to_apply(inp) for inp in list_of_inputs)
    return list_of_inputs


if __name__ == '__main__':
    def power(n=int()):
        return n * n

    def by_two(n=int()):
        return n * 2

    lst = (1, 2, 3, 6)
    print("_____with function power_____on: {}".format(lst))
    for el in ft_map(power, lst):
        print(el)
    print("_____with function by_two_____")
    for el in ft_map(by_two, lst):
        print(el)
    lst = [1, 2, 'a', 1 == 1, 2 == 2, 3 == 5, ('toto', 'titi'), 'tut' == 'tat']
    print("_____with function_____ on : {}".format(lst))
    for el in ft_map(by_two, lst):
        print(el)
    print("_____without function_____ on : {}".format(lst))
    for el in ft_map(None, lst):
        print(el)
    print("with lambda:")
    numbers = (1, 2, 3, 4)
    print(list(ft_map(lambda x: x*x, numbers)))
    # print("with many iterators")
    # num1 = [4, 5, 6]
    # num2 = [5, 6, 7]
    # print(list(map(lambda n1, n2: n1+n2, num1, num2)))

    print("\n\n_____with function_____but no list")
    try:
        for el in ft_map(power, None):
            print(el)
    except Exception:
        traceback.print_exc(file=sys.stderr)
    print("____vs real map___")
    for el in map(power, None):
        print(el)
