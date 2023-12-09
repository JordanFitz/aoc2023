#!/bin/python3

def main():
    with open("input.txt") as input:
        total = 0
        for card_num,line in enumerate(input):
            line = line.strip()
            if len(line) == 0: continue
            card_num += 1
            _, values = line.split(":")
            values = values.strip()
            winning, have = values.split("|")
            winning = list(filter(lambda w: len(w)>0, winning.strip().split(" ")))
            have = list(filter(lambda h: len(h)>0, have.strip().split(" ")))
            num_winning = 0
            for num in have:
                if num in winning:
                    num_winning+=1
            if num_winning > 0:
                total += 2**(num_winning-1)
        print(total)

if __name__ == '__main__':
    main()
