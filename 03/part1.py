#!/bin/python3

def get_adj(mat, x, y):
    offsets = [-1,0,1]
    for oy in offsets:
        yy = y + oy
        if yy < 0 or yy >= len(mat): continue
        for ox in offsets:
            xx = x + ox

            if ox == 0 and oy == 0: continue
            if xx < 0 or xx >= len(mat[yy]): continue

            val = mat[yy][xx]
            if not val.isnumeric() and val != ".":
                return True

    return False

def main():
    with open("input.txt") as input:
        lines = []
        for line in input:
            lines.append(line.strip())

        total = 0

        for y,line in enumerate(lines):
            # if y > 0: print(lines[y-1])
            # if y+1 < len(lines): print(lines[y+1])

            num = ""
            is_adj = False
            for x,c in enumerate(line):
                if c.isnumeric():
                    num += c
                    if not is_adj:
                        is_adj = get_adj(lines, x, y)
                elif num != "":
                    if is_adj: total += int(num)
                    num = ""
                    is_adj = False
            if num != "":
                if is_adj: total += int(num)

        print(total)


if __name__ == '__main__':
    main()
