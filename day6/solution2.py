from collections import defaultdict
import copy

def guard_gallivant(input):
    map = [list(line.strip()) for line in input.readlines()]

    nr = len(map)
    nc = len(map[0])

    visited = defaultdict(int)
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}
    guard_pos = [-1, -1, ""]

    for r in range(nr):
        for c in range(nc):
            if map[r][c] in directions.keys():
                guard_pos = [r, c, map[r][c]]
                visited[(r, c)] += 1


    def check_loop(test_map):
        x, y, direction = guard_pos[0], guard_pos[1], guard_pos[2] 
        visited_states = set()
        visited_states.add((x, y, direction))
        
        while True:
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
    
            if nx < 0 or nx >= nr or ny < 0 or ny >= nc:
                return False
    
            if test_map[nx][ny] == "#":
                direction = turn_right[direction]
            else:
                x, y = nx, ny
                
                state = (x, y, direction)
                if state in visited_states:
                    return True 
                visited_states.add(state)
  
    loops = 0
    for r in range(nr):
        for c in range(nc):
            if map[r][c] == ".":
                new_map = copy.deepcopy(map) 
                new_map[r][c] = "#"
                
                if check_loop(new_map):
                    loops += 1


    return loops



if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {guard_gallivant(input)}")


    
    
