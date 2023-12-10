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

def get_pipe(sides):
    sides = set(sides)
    if sides == set([LEFT, RIGHT]):
        return HORIZONTAL
    if sides == set([TOP, BOTTOM]):
        return VERTICAL
    if sides == set([TOP, RIGHT]):
        return NORTH_EAST
    if sides == set([TOP, LEFT]):
        return NORTH_WEST
    if sides == set([BOTTOM, LEFT]):
        return SOUTH_WEST
    if sides == set([BOTTOM, RIGHT]):
        return SOUTH_EAST
    assert False, "couldn't get pipe for " + ",".join(sides)

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
    assert False, "couldn't get sides for " + pipe

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
    for i,conn in enumerate(result):
        if conn[0] is None: continue
        if not is_connected(sub_sides, get_sides(conn[0]), SIDE_ORDER[i]):
            result[i] = (None,conn[1])

    return result

def get_start_type(connections):
    sides = []
    if connections[0][0] is not None:
        sides.append(TOP)
    if connections[1][0] is not None:
        sides.append(RIGHT)
    if connections[2][0] is not None:
        sides.append(BOTTOM)
    if connections[3][0] is not None:
        sides.append(LEFT)
    return get_pipe(sides)

def walk(mat, start):
    curr_pos = start
    path = {}
    steps = 0

    prev_pos = None
    start_type = None

    horiz_pipes = [
        HORIZONTAL,
        SOUTH_EAST,
        NORTH_EAST,
    ]

    while True:
        connections = get_connections(mat, curr_pos)

        if start_type is None:
            start_type = get_start_type(connections)
            if start_type in horiz_pipes:
                horiz_pipes.append(START)

        for conn in connections:
            t,next_pos=conn
            if t is None: continue

            if next_pos != prev_pos:
                steps += 1

                curr_t = mat[curr_pos[1]][curr_pos[0]]

                path[curr_pos] = curr_t in horiz_pipes

                prev_pos = curr_pos
                curr_pos = next_pos

                if t == START: return path

                break

    assert False, "couldn't walk path"

def is_inside(pos, path_positions):
    x,y=pos

    num_crosses = 0
    for cast_y in range(y-1, -1, -1):
        cast_pos = (x,cast_y)
        if cast_pos in path_positions and path_positions[cast_pos]:
            num_crosses+=1

    return num_crosses % 2 != 0

def get_num_inside(mat, path):
    open_positions = {}
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if not (x,y) in path:
                open_positions[(x,y)]=None

    num_inside = 0
    for pos in open_positions:
        replacement = 'O'

        if is_inside(pos, path):
            num_inside += 1
            replacement = 'I'

        row = list(mat[pos[1]])
        row[pos[0]] = replacement
        mat[pos[1]] = "".join(row)

    print("\n".join(mat)
        .replace("-","━").replace("|","│")
        .replace("7","┑").replace("F","┍")
        .replace("J","┙")
        .replace("L","┕")
    )

    return num_inside

def main():
    with open("input.txt") as input:
        mat = list(map(lambda l: l.strip(), input.readlines()))

        start = find_start(mat)
        path = walk(mat, start)

        print("num inside",get_num_inside(mat, path))

if __name__ == '__main__':
    main()
