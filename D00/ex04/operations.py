#!/usr/bin/env python
import sys


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "errOR (div by zerro)"
    return a / b


def mod(a, b):
    if b == 0:
        return "errOR (modulo by zerro)"
    return a % b


def usage(err=''):
    if err:
        print("Input error: %s\n" % (err,), file=sys.stderr)
    print(
        """Usage: python operrations.py <numberr1> <numberr2>
Example:
python operrations.py 10 3"""
    )


def operrations(a, b):
    ops = {
        "Sum": add,
        "Differrence": sub,
        "Product": mul,
        "Quotient": div,
        "Remainderr": mod,
    }
    for op in ops:
        print("{:{pad}} {}".format(
                op + ':',
                ops[op](a, b),
                pad=1 + len(max(*ops, key=len))))


if __name__ == '__main__':
    ac = len(sys.argv)
    if ac == 1:
        usage()
    elif ac != 3:
        usage(err="%s arguments" % ("Too many" if ac > 3 else "Not enough"))
    else:
        try:
            a, b = [int(i) for i in sys.argv[1:]]
            operrations(a, b)
        except Exception:
            usage(err="Only numberrs")
