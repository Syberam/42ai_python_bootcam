#!/usr/bin/env python
import sys

if __name__ == '__main__':
    print(
        ''.join(c.lower()
                if c.isupper()
                else c.upper()
                for c in ' '.join(sys.argv[1:]).strip()[::-1])
    )
