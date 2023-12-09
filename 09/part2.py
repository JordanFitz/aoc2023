#!/bin/python3

def get_diffs(values):
    diffs = []
    for i,v in enumerate(values[1:]):
        diffs.append(v-values[i])
    return diffs

def get_next(sequence):
    sequence.reverse()
    results = [sequence[0]]
    for i,diffs in enumerate(sequence[1:]):
        results.append([diffs[0] - results[i][0]] + diffs)
    return list(reversed(results))

def main():
    with open("input.txt") as input:
        total = 0
        for line in input:
            line = line.strip()
            values = list(map(lambda v: int(v), line.split(" ")))
            
            sequence = [values]

            diffs = values
            while set(diffs) != set([0]):
                diffs = get_diffs(diffs)
                sequence.append(diffs)

            n = get_next(sequence)
            print(n)
            total += n[0][0]
        print(total)

if __name__ == '__main__':
    main()
