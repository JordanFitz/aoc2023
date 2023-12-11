#!/bin/python3

def add_space(mat):
    empty_rows = set()
    empty_cols = set()

    for x in range(len(mat[0])):
        col_empty = True
        for y in range(len(mat)):
            if len(set(mat[y])) == 1:
                empty_rows.add(y)

            if mat[y][x] != '.':
                col_empty = False
                break

        if col_empty:
            empty_cols.add(x)

    for i,y in enumerate(sorted(list(empty_rows))):
        mat = mat[:y+i] + [mat[y+i]] + mat[y+i:]

    for i,x in enumerate(sorted(list(empty_cols))):
        for y in range(len(mat)):
            row = mat[y]
            row = row[:x+i] + '.' + row[x+i:]
            mat[y] = row

    return mat

def get_nodes(mat):
    results = []
    for y,row in enumerate(mat):
        for x,col in enumerate(row):
            if col == '#': 
                results.append((x,y))
    return results

def main():
    with open("input.txt") as input:
        mat = list(map(lambda l: l.strip(), input.readlines()))
        mat = add_space(mat)

        nodes = get_nodes(mat)

        for i,n in enumerate(nodes):
            row = list(mat[n[1]])
            row[n[0]] = str(i+1)
            mat[n[1]] = "".join(row)

        node_pairs = set()
        for a in nodes:
            for b in nodes:
                if a == b: continue
                node_pairs.add(frozenset((a,b)))

        total = 0
        for pair in node_pairs:
            # pair = list(pair)
            a,b=pair
            total += abs(a[0]-b[0])+abs(a[1]-b[1])

        print(total)

if __name__ == '__main__':
    main()
