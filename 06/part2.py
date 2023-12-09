#!/bin/python3

def main():
    with open("input.txt") as input:
        times, distances = map(lambda l: l.strip(), input.readlines())
        time = int("".join(list(filter(lambda s: len(s)>0, times.split(" ")[1:]))))
        distance = int("".join(list(filter(lambda s: len(s)>0, distances.split(" ")[1:]))))

        options = [x for x in range(time+1) if x**2 - time*x + distance <= 0]
        print(len(options))

if __name__ == '__main__':
    main()
