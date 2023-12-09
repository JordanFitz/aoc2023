#!/bin/python3

def main():
    with open("input.txt") as input:
        lines = list(filter(lambda l: len(l)>0, map(lambda l: l.strip(), input.readlines())))
        instructions = lines[0]
        lines = lines[1:]
        network = {}
        for line in lines:
            label, to = line.split(" = ")
            network[label] = tuple(to[1:-1].split(", "))
        
        loc = "AAA"
        steps = 0
        searching = True
        while searching:
            for instruction in instructions:

                l,r = network[loc]
                if instruction == 'L': loc = l
                if instruction == 'R': loc = r

                steps += 1

                if loc == "ZZZ":
                    searching = False
                    break

        print(steps)

if __name__ == '__main__':
    main()
