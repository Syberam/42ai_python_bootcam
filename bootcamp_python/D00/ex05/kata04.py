#! /usr/bin/env python


if __name__ == '__main__':
    num = (0, 4, 132.42222, 10000, 12345.67)
    print("day_{:02} ex_{:02} {:.2f} {:.2e} {:.2e}".format(*num))
