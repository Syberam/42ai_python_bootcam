#! /usr/bin/env python


if __name__ == '__main__':
    t = (3, 30, 2019, 9, 25)
    # 09/25/2019 03:30
    print("{3:02d}/{4:02d}/{2:04d} {0:02d}:{1:02d}".format(*t))
