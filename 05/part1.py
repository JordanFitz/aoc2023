#!/bin/python3

def lookup(ranges, input):
    for r in ranges:
        if input >= r[1] and input < r[1] + r[2]:
            return r[0] + (input - r[1])
    return input

def main():
    with open("input.txt") as input:
        lines = list(filter(lambda l: len(l) > 0, map(lambda l: l.strip(), input.readlines())))

        _, seeds = lines[0].split(": ")
        seeds = list(map(lambda s: int(s), seeds.split(" ")))
        
        maps = {}

        map_name = ""
        current = []
        for line in lines[1:]:
            if line[0].isnumeric():
                current.append(list(map(lambda s: int(s), line.split(" "))))
            else:
                if len(current) > 0:
                    maps[map_name] = current

                map_name, _ = line.split(" ")
                map_name = ":".join(map_name.split("-to-"))

                current = []

        if len(current) > 0:
            maps[map_name] = current

        order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

        lowest_location = -1

        for seed in seeds:
            val = seed
            for i,o in enumerate(order[1:]):
                map_name = order[i]+":"+o
                l = lookup(maps[map_name], val)
                val = l
                if o == "location":
                    if lowest_location == -1 or val < lowest_location:
                        lowest_location = val

        print(lowest_location)


if __name__ == '__main__':
    main()
