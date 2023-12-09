#!/bin/python3

import threading

order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

def lookup(ranges, input):
    for r in ranges:
        if input >= r[1] and input < r[1] + r[2]:
            return r[0] + (input - r[1])
    return input

lowest_loc = -1

def do(maps, seed_start, seed_end, id, lock):
    global lowest_loc
    # print(i, ":", seed_start,"->",seed_end)
    for seed in range(seed_start, seed_end):
        if seed % 100000 == 0:
            print("working on", id, ":", seed_start,"->",seed_end, "...", 100*((seed_end-seed_start)/seed), "%")
        val = seed
        for i,o in enumerate(order[1:]):
            map_name = order[i]+":"+o
            l = lookup(maps[map_name], val)
            val = l
            if o == "location":
                with lock:
                    if lowest_loc == -1 or val < lowest_loc:
                        print("new lowest:", val)
                        lowest_loc = val
    print(id,"done")

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

        lowest_location = -1

        min_seed = -1
        max_seed = -1

        for i in range(0, len(seeds), 2):
            seed, num = seeds[i], seeds[i+1]

            if min_seed == -1 or seed < min_seed:
                min_seed = seed
            if seed + num > max_seed:
                max_seed = seed + num

        lookup_table = {}

        threads = []

        
        lock = threading.Lock()
        # for i in range(parts):
        for i in range(0, len(seeds), 2):
            seed_start, num = seeds[i], seeds[i+1]
            seed_end = seed_start + num

            print("sugg", i//2, "proccessing", seed_end-seed_start)

            parts = (seed_end-seed_start)//10
            # assert (seed_end - seed_start) > parts
            for start in range(seed_start, seed_end, parts):
                t = threading.Thread(
                    target=do,
                    args=(maps,
                        start,
                        min(start+parts, seed_end),
                        str(i//2)+":"+str(start),
                        lock,
                    )
                )
                threads.append(t)
                t.start()

            # t = threading.Thread(
            #     target=do,
            #     args=(lookup_table, maps, seed_start, seed_end, i, lock)
            # )
            # t = threading.Thread(
            #     target=do,
            #     args=(lookup_table, maps, min_seed+i*part_size, min_seed+(i+1)*part_size, i, lock)
            # )
            # threads.append(t)
            # t.start()

        for t in threads:
            t.join()

        # for i in range(0, len(seeds), 2):
        #     start, num = seeds[i], seeds[i+1]
        #     print(start, num)
        #     for seed in range(start, start+num):
        #         val = seed
        #         for i,o in enumerate(order[1:]):
        #             map_name = order[i]+":"+o
        #             l = lookup(maps[map_name], val)
        #             val = l
        #             if o == "location":
        #                 if lowest_location == -1 or val < lowest_location:
        #                     lowest_location = val

        print(lowest_loc)


if __name__ == '__main__':
    main()
