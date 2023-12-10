#!/bin/python3

VERTICAL = "|"
HORIZONTAL = "-"
NORTH_EAST = "L"
NORTH_WEST = "J"
SOUTH_WEST = "7"
SOUTH_EAST = "F"

START = "S"

TOP = "top"
BOTTOM = "bottom"
LEFT = "left"
RIGHT = "right"

SIDE_ORDER = [TOP,RIGHT,BOTTOM,LEFT]

def find_start(mat):
    for y,line in enumerate(mat):
        x = line.find('S')
        if x != -1: return (x,y)
    assert False, "couldn't find start"

def get_sides(pipe):
    if pipe == START:
        return [TOP, RIGHT, BOTTOM, LEFT]
    if pipe == HORIZONTAL:
        return [LEFT, RIGHT]
    if pipe == VERTICAL:
        return [TOP, BOTTOM]
    if pipe == NORTH_EAST:
        return [TOP, RIGHT]
    if pipe == NORTH_WEST:
        return [TOP, LEFT]
    if pipe == SOUTH_WEST:
        return [BOTTOM, LEFT]
    if pipe == SOUTH_EAST:
        return [BOTTOM, RIGHT]
    assert False, "couldn't get sides"

def is_connected(a, b, side):
    if side == TOP:
        return (TOP in a and BOTTOM in b)
    if side == RIGHT:
        return (RIGHT in a and LEFT in b)
    if side == LEFT:
        return (LEFT in a and RIGHT in b)
    if side == BOTTOM:
        return (BOTTOM in a and TOP in b)
    assert False, "couldn't determine if connected"

# return list of top, right, bottom, left
def get_connections(mat, pos):
    x,y=pos

    if y == 0:
        top = None
    else:
        top = mat[y-1][x] if mat[y-1][x] != '.' else None
    if x == 0:
        left = None
    else:
        left = mat[y][x-1] if mat[y][x-1] != '.' else None
    if y == len(mat)-1:
        bottom = None
    else:
        bottom = mat[y+1][x] if mat[y+1][x] != '.' else None
    if x == len(mat[0])-1:
        right = None
    else:
        right = mat[y][x+1] if mat[y][x+1] != '.' else None

    top = (top,(x,y-1))
    left = (left,(x-1,y))
    bottom = (bottom,(x,y+1))
    right = (right,(x+1,y))

    sub = mat[y][x]
    sub_sides = get_sides(sub)

    result = [top, right, bottom, left]
    for i,side in enumerate(result):
        if side[0] is None: continue
        if not is_connected(sub_sides, get_sides(side[0]), SIDE_ORDER[i]):
            result[i] = (None,side[1])

    return result

def walk(mat, start):
    curr_pos = start
    path = []
    steps = 0

    prev_pos = None

    while True:
        connections = get_connections(mat, curr_pos)

        for conn in connections:
            t,pos=conn
            if t is None: continue

            if pos != prev_pos:
                steps += 1

                prev_pos = curr_pos
                curr_pos = pos
                path.append(pos)

                if t == START:
                    return path

                break

def main():
    with open("input.txt") as input:
        mat = list(map(lambda l: l.strip(), input.readlines()))

        start = find_start(mat)
        path = walk(mat, start)

        assert len(path) % 2 == 0, "loop not even"

        print("halfway:", len(path)//2)

if __name__ == '__main__':
    main()
