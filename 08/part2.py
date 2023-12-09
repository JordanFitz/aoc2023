#!/bin/python3

import math
from functools import reduce

def lcm(arr):
    return reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)

def main():
    with open("input.txt") as input:
        lines = list(filter(lambda l: len(l)>0, map(lambda l: l.strip(), input.readlines())))
        instructions = lines[0]
        lines = lines[1:]
        network = {}
        for line in lines:
            label, to = line.split(" = ")
            network[label] = tuple(to[1:-1].split(", "))
        
        starting_nodes = []
        for label in network:
            if label[2] == 'A':
                starting_nodes.append(label)

        steps_required = []

        ind = 0
        start_node = starting_nodes[0]
        loc = start_node
        i = steps = 0

        searching = True
        while searching:
            while i < len(instructions):
                l,r = network[loc]

                instruction = instructions[i]
                if instruction == 'L': loc = l
                if instruction == 'R': loc = r

                i += 1
                steps += 1

                if loc[2] == 'Z':
                    print("found an end in for",start_node,"in",steps,"steps")
                    steps_required.append(steps)

                    if ind == len(starting_nodes) - 1:
                        searching = False
                        break

                    ind += 1
                    start_node = starting_nodes[ind]
                    loc = start_node
                    i = steps = 0

            if i == len(instructions): i = 0

        print(lcm(steps_required))

if __name__ == '__main__':
    main()
