#! /usr/bin/env python


if __name__ == '__main__':
    t = (42, 21, 76)
    print("The {} numbers are: {}".format(len(t), ', '.join(map(str, t))))
