#!/usr/bin/env python
import functools


def ft_reduce(function_to_apply, list_of_inputs):
    it = iter(list_of_inputs)
    try:
        initializer = next(it)
    except StopIteration:
        raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function_to_apply(accum_value, x)
    return accum_value


if __name__ == '__main__':
    lis = [2, 4, 6, 89]
    print(functools.reduce(lambda a, b: a + b, lis))
    print(ft_reduce(lambda a, b: a + b, lis))
    print(functools.reduce(lambda a, b: a if a < b else b, lis))
    print(ft_reduce(lambda a, b: a if a < b else b, lis))
