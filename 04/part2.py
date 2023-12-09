#!/bin/python3

import threading

def do(instances, card, wins):
    for i in range(card+1, card+wins+1):
        instances[i] += 1

def main():
    with open("input.txt") as input:
        total = 0
        winners = []

        instances = {}

        for card_num,line in enumerate(input):
            line = line.strip()
            if len(line) == 0: continue
            instances[card_num] = 1
            _, values = line.split(":")
            values = values.strip()
            winning, have = values.split("|")
            winning = list(filter(lambda w: len(w)>0, winning.strip().split(" ")))
            have = list(filter(lambda h: len(h)>0, have.strip().split(" ")))
            num_winning = 0
            for num in have:
                if num in winning:
                    num_winning+=1
            winners.append(num_winning)

        for card,wins in enumerate(winners):
            for i in range(card+1, card+wins+1):
                instances[i] += instances[card]

        total = 0
        for k in instances:
            total += instances[k]

        print(total)

if __name__ == '__main__':
    main()
