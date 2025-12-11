def xmas_search(input):
    res = 0
    mat = [[l for l in line[:-1]] for line in input.readlines()]   

    nr_cols = len(mat)
    nr_rows = len(mat[0])

    for r in range(nr_rows):
        for c in range(nr_cols):
            if c+4 <= nr_cols and \
                ''.join(mat[r][c:c+4]) == "XMAS":
                    res += 1 
        
            if c-3 >= 0 and \
                mat[r][c] + mat[r][c-1] + mat[r][c-2] + mat[r][c-3] == "XMAS":
                    res += 1
        
            if r+4 <= nr_rows and \
                mat[r][c] + mat[r+1][c] + mat[r+2][c] + mat[r+3][c] == "XMAS": 
                    res += 1
        
            if r-3 >= 0 and \
                mat[r][c] + mat[r-1][c] + mat[r-2][c] + mat[r-3][c] == "XMAS":
                    res += 1
        
            if r+4 <= nr_rows and c+4 <= nr_cols and \
                mat[r][c] + mat[r+1][c+1] + mat[r+2][c+2] + mat[r+3][c+3] == "XMAS":
                    res += 1
        
            if r+4 <= nr_rows and c-3 >= 0 and \
                mat[r][c] + mat[r+1][c-1] + mat[r+2][c-2] + mat[r+3][c-3] == "XMAS":
                    res += 1
        
            if r-3 >= 0 and c+4 <= nr_cols and \
                mat[r][c] + mat[r-1][c+1] + mat[r-2][c+2] + mat[r-3][c+3] == "XMAS":
                    res += 1
        
            if r-3 >= 0 and c-3 >= 0 and \
                mat[r][c] + mat[r-1][c-1] + mat[r-2][c-2] + mat[r-3][c-3] == "XMAS":
                    res += 1
    return res


if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {xmas_search(input)}")


