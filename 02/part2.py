#!/bin/python3

def power(game):
    maxes = {
        "red":0,
        "green":0,
        "blue":0
    }

    for s in game.split("; "):
        draws = s.split(", ")
        for d in s.split(", "):
            num, color = d.split(" ")
            num = int(num)
            if num > maxes[color]:
                maxes[color] = num

    print(maxes)
    return maxes["red"]*maxes["green"]*maxes["blue"]

def main():
    with open("input.txt") as input:
        total = 0
        for line in input:
            line = line.strip()
            game, values = line.split(": ")
            _, game = game.split(" ")
            game = int(game)

            p = power(values)
            print(p)
            total += p

        print(total)

if __name__ == '__main__':
    main()
