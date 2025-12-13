

def guard_gallivant(input):
    map = [list(line.strip()) for line in input.readlines()]

    nr = len(map)
    nc = len(map[0])

    visited = set()
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}
    guard_pos = [-1, -1, ""]

    for r in range(nr):
        for c in range(nc):
            if map[r][c] in directions.keys():
                guard_pos = [r, c, map[r][c]]
                visited.add((r, c))

    x, y, direction = guard_pos[0], guard_pos[1], guard_pos[2]

    while True:
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
    
        if nx < 0 or nx >= nr or ny < 0 or ny >= nc:
            break
    
        if map[nx][ny] == "#":
            direction = turn_right[direction]
        else:
            x, y = nx, ny
            visited.add((x, y))

    return len(visited)



if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {guard_gallivant(input)}")


    
    
