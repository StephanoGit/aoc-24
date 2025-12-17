from collections import defaultdict

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(r, c, plant_type, map, visited):
    if (r, c) in visited:
        return 0, 0
    if r < 0 or r >= len(map) or c < 0 or c >= len(map[0]):
        return 0, 0
    if map[r][c] != plant_type:
        return 0, 0
    
    visited.add((r, c))
    area = 1
    
    neighbors = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(map) and 0 <= nc < len(map[0]) and map[nr][nc] == plant_type:
            neighbors += 1
    
    perimeter = 4 - neighbors
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        sub_area, sub_perimeter = dfs(nr, nc, plant_type, map, visited)
        area += sub_area
        perimeter += sub_perimeter
    
    return area, perimeter

def garden_groups(input):
    map = [[char for char in line.strip()] for line in input.readlines()]
    visited = set()
    total_score = 0
    
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (r, c) not in visited:
                area, perimeter = dfs(r, c, map[r][c], map, visited)
                total_score += area * perimeter
    
    return total_score

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {garden_groups(input)}")
