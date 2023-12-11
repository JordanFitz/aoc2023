#!/bin/python3

def add_space(mat, nodes):
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

    amt = 1000000

    for i,y in enumerate(sorted(list(empty_rows))):
        for ni,n in enumerate(nodes):
            if n[1]>y+(i*(amt-1)):
                nodes[ni] = (n[0],n[1]+(amt-1))

    for i,x in enumerate(sorted(list(empty_cols))):
        for ni,n in enumerate(nodes):
            if n[0]>x+(i*(amt-1)):
                nodes[ni] = (n[0]+(amt-1),n[1])

    return nodes

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

        nodes = get_nodes(mat)
        nodes = add_space(mat, nodes)

        node_pairs = set()
        for a in nodes:
            for b in nodes:
                if a == b: continue
                node_pairs.add(frozenset((a,b)))

        total = 0
        for pair in node_pairs:
            a,b=pair
            total += abs(a[0]-b[0])+abs(a[1]-b[1])

        print(total)

if __name__ == '__main__':
    main()
