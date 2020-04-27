#! /usr/bin/env python
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        try:
            bad_string = int(sys.argv[1])
            print("ERROR")
        except Exception:
            string = sys.argv[1]
            try:
                need_len = int(sys.argv[2])
                print(
                    [w for w in
                        ["".join([c if c.isalnum() else '' for c in w])
                            for w in string.split()]
                        if len(w) > need_len])
            except Exception:
                print("ERROR")
