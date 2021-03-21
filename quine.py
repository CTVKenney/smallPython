#!/usr/bin/env python3

def main():
    f = open("quine.py")
    print(f.read())
    f.close()
    return

if __name__ == '__main__':
    main()
