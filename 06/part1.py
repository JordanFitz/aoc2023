#!/bin/python3

def main():
    with open("input.txt") as input:
        times, distances = map(lambda l: l.strip(), input.readlines())
        times = list(map(lambda t: int(t), list(filter(lambda s: len(s)>0, times.split(" ")))[1:]))
        distances = list(map(lambda t: int(t), list(filter(lambda s: len(s)>0, distances.split(" ")))[1:]))

        result = 1
        for i in range(len(times)):
            minimum = distances[i]+1
            time = times[i]
            options = [x for x in range(time+1) if x**2 - time*x + minimum <= 0]
            result *= len(options)

        print(result)


if __name__ == '__main__':
    main()
