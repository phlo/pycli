"""Some module."""

import argparse
import sys

def main ():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pos0", help="Some positional argument.")
    parser.add_argument("-opt0", metavar="opt", help="Some optional argument.")
    args = parser.parse_args()
    print(f"{__name__}.main({sys.argv})")
    return { "argv" : sys.argv, "args" : args }

if __name__ == "__main__":
    main()
