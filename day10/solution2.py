
dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]

def dfs(r, c, map):
    if not (0 <= r < len(map) and 0 <= c < len(map[0])):
        return 0 

    if map[r][c] == 9:
        return 1
    
    score = 0
    for dir in dirs:
        nr, nc = r + dir[0], c + dir[1]
        if 0 <= nr < len(map) and 0 <= nc < len(map[0]) and\
                map[nr][nc] == map[r][c] + 1:
            score += dfs(nr, nc, map)

    return score

def hoof_it(input):
    map = [[int(ch) for ch in line.strip()] for line in input.readlines()] 

    total_score = 0
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 0:
                total_score += dfs(r, c, map)           
    
    return total_score 

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {hoof_it(input)}")
            
