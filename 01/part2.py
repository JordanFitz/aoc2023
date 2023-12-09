#!/bin/python3

def find(line):
    first_index = 99999
    last_index = -1
    first = None
    last = None   

    for i,val in enumerate(line):
        if val.isnumeric():
            if i < first_index:
                first = val
                first_index = i
            if i > last_index:
                last = val
                last_index = i

    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for ind, num in enumerate(nums):
        val = ind+1
        f = line.find(num)
        l = line.rfind(num)
        if f == -1: continue
        assert l != -1
        if f < first_index:
            first = val
            first_index = f
        if l > last_index:
            last = val
            last_index = l

    assert first is not None and last is not None

    return str(first) + str(last)

def main():
    with open("input.txt") as input:
        total = 0
        for line in input:
            line = line.strip()
            print(line)
            f = find(line)
            print(find(line))
            total += int(find(line))

        print(total)

if __name__ == '__main__':
    main()
