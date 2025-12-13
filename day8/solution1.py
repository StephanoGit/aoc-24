from collections import defaultdict

def antinodes(input):
    map = [list(line.strip()) for line in input.readlines()]

    nr, nc = len(map), len(map[0])
    antennas = defaultdict(list)

    for r in range(nr):
        for c in range(nc):
            if map[r][c] != ".":
                antennas[map[r][c]].append((r,c))

    count = set()
    for _, pos in antennas.items():
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                r, c = pos[i]
                rr, cc = pos[j]
                dr = r - rr
                dc = c - cc

                if 0 <= rr - dr < nr and \
                        0 <= cc - dc < nc:
                    count.add((rr-dr, cc-dc))

                if 0 <= r + dr < nr and \
                        0 <= c + dc < nc:
                    count.add((r+dr, c+dc))

    return len(count)
            


if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {antinodes(input)}")
            
