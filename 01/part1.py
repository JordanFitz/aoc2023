#!/bin/python3

def main():
    with open("input.txt") as input:
        total = 0
        for line in input:
            first = None
            last = None
            for c in line:
                if c.isnumeric():
                    if first is None:
                        first = c
                    last = c
            total += int(first + last)
        print(total)

if __name__ == '__main__':
    main()
