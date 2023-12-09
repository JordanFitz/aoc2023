#!/bin/python3

# reduce/simplify ranges
def simplify(ranges):
    ranges = list(ranges)

    if len(ranges) < 2: return ranges
    
    ranges.sort(key=lambda r: r[0])
    result = [ranges[0]]
    for i,curr in enumerate(ranges[1:]):
        last = result[-1]
        # fully overlap, skip
        if curr[0] >= last[0] and curr[1] <= last[1]: continue
        # partially overlap, extend
        elif curr[0] >= last[0] and curr[0] <= last[1] and curr[1] > last[1]:
            result[-1] = (last[0],curr[1])
        # adjacent, combine
        elif curr[0] == last[1]+1:
            result[-1] = (last[0],curr[1])
        # no overlap, add
        elif curr[0] > last[1]:
            result.append(curr)

    return result

def get_overlap(range1, range2):
    overlap = (max(range1[0], range2[0]), min(range1[1], range2[1]))
    if overlap[0] > overlap[1]:
        return None
    return overlap

# subtract the overlap from the range r
def sub(r, overlap):
    if r[0] < overlap[0]:
        if r[1] > overlap[1]:
            return [(r[0],overlap[0]-1),(overlap[1]+1,r[1])]
        if r[1] == overlap[1]:
            return [(r[0],overlap[0]-1)]
    if r[0] == overlap[0]:
        if r[1] == overlap[1]:
            return [None]
        if r[1] > overlap[1]:
            return [(overlap[1]+1,r[1])]

    # the overlap should never be outside the bounds of r
    assert False

def pull_out(ranges, range):
    results = []
    for i,r in enumerate(ranges):
        overlap = get_overlap(r, range)
        if overlap is None: 
            results.append(r)
            continue
        new_ranges = list(filter(lambda r: r is not None, sub(r, overlap)))
        print(r,"-",overlap,"=",new_ranges)
        results.extend(new_ranges)
    return simplify(results)

def process(in_ranges, out_ranges):
    overlapped = []
    translations = []

    for i,out_range in enumerate(map(lambda r: (r[1],r[1]+r[2]-1), out_ranges)):
        translation = out_ranges[i][0]-out_ranges[i][1]
        for in_range in in_ranges:
            overlap = get_overlap(in_range, out_range)
            if overlap is None: continue
            overlapped.append(overlap)
            translations.append(translation)

    overlapped = list(overlapped)

    others = in_ranges
    for d in overlapped:
        others = pull_out(others, d)

    for i,d in enumerate(overlapped):
        overlapped[i] = (
            d[0] + translations[i],
            d[1] + translations[i],
        )

    overlapped.extend(others)

    return simplify(overlapped)

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

        for i in range(0, len(seeds), 2):
            seed_start, num_seeds = seeds[i], seeds[i+1]
            in_ranges = [(seed_start,seed_start+num_seeds-1)]

            print("range of seeds:",in_ranges[0])

            for i,o in enumerate(order[1:]):
                map_name = order[i]+":"+o
                print(map_name, "map")

                in_ranges = process(in_ranges, maps[map_name])
                print("new ranges:", in_ranges)

                if o == "location":
                    lowest = in_ranges[0][0]
                    if lowest_location == -1 or lowest < lowest_location:
                        lowest_location = lowest
                        print("new lowest:", lowest)

            print("lowest:", lowest_location)


if __name__ == '__main__':
    main()
