#!/usr/bin/env python3

import sys

def main():
    filename = 'quasiquine.py'
    with open(filename, 'r') as opened:
        readfile = opened.read()
        print(readfile)

if __name__ == '__main__':
    main()
