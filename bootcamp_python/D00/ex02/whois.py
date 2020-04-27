#!/usr/bin/env python
import sys

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("ERROR", file=sys.stderr)
    elif len(sys.argv) == 2:
        try:
            x = int(sys.argv[1])
            r = "Zero" if x == 0 else "Odd" if x % 2 == 1 else "Even"
            print("I'm %s" % (r,))
        except Exception:
            print("ERROR", file=sys.stderr)
