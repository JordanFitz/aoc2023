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

def get_num(line, x, y):
    res = {}
    r = ""
    s = x
    while x >= 0 and line[x].isnumeric():
        res[str(x)+","+str(y)] = line[x]
        r = line[x] + r
        x -= 1
    x = s+1
    while x < len(line) and line[x].isnumeric():
        res[str(x)+","+str(y)] = line[x]
        r += line[x]
        x += 1
    return res,r

def overlap(a, b):
    for k in a:
        if k in b: return True
    for k in b:
        if k in a: return True
    return False

def get_adj_nums(mat, x, y):
    nums = []

    offsets = [-1,0,1]

    for oy in offsets:
        yy = y + oy
        if yy < 0 or yy >= len(mat): continue
        for ox in offsets:
            xx = x + ox

            if ox == 0 and oy == 0: continue
            if xx < 0 or xx >= len(mat[yy]): continue

            val = mat[yy][xx]
            if val.isnumeric():
                num = get_num(mat[yy], xx, yy)
                overlaps = False
                for existing in nums:
                    if not overlaps:
                        overlaps = overlap(existing[0], num[0])
                    else: break
                if not overlaps:
                    nums.append(num)

    res = list(map(lambda n: int(n[1]), nums))
    return res


def main():
    with open("input.txt") as input:
        lines = []
        for line in input:
            lines.append(line.strip())

        total = 0

        for y,line in enumerate(lines):
            num = ""
            is_adj = False
            for x,c in enumerate(line):
                if c == '*':
                    nums = get_adj_nums(lines, x, y)
                    if len(nums) == 2:
                        total += nums[0]*nums[1]

        print(total)


if __name__ == '__main__':
    main()
