#! /usr/bin/env python


if __name__ == '__main__':
    s = "The right format"
    print("{}".format(s.rjust(42, '-')), end='')
