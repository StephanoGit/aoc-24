patterns = [
        [["M", ".", "S"], 
         [".", "A", "."], 
         ["M", ".", "S"]],
       
        [["S", ".", "M"], 
         [".", "A", "."], 
         ["S", ".", "M"]], 

        [["M", ".", "M"], 
         [".", "A", "."], 
         ["S", ".", "S"]],

        [["S", ".", "S"], 
         [".", "A", "."], 
         ["M", ".", "M"]],  
        ]

def xmas_search(input):
    res = 0
    mat = [[l for l in line[:-1]] for line in input.readlines()]

    nr = len(mat)
    nc = len(mat[0])

    for r in range(nr-2):
        for c in range(nc-2):
            for p in patterns:
                if check_pattern(p, mat, r, c):
                    res += 1
                    break
    return res

def check_pattern(p, mat, r, c):
    for dr in range(3):
        for dc in range(3):
            if p[dr][dc] != mat[r+dr][c+dc] and p[dr][dc] != ".":
                return False
    return True 

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {xmas_search(input)}")

