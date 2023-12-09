#!/bin/python3

def is_valid(num, color):
    maxes = {
        "red":12,
        "green":13,
        "blue":14
    }
    return num <= maxes[color]

def main():
    with open("input.txt") as input:
        total = 0
        for line in input:
            line = line.strip()
            game, values = line.split(": ")
            _, game = game.split(" ")
            game = int(game)

            valid = True
            sets = values.split("; ")
            for s in sets:
                draws = s.split(", ")
                for d in draws:
                    num, color = d.split(" ")
                    num = int(num)
                    if not is_valid(num, color):
                        valid = False
            if valid: total += game
        print(total)

if __name__ == '__main__':
    main()
