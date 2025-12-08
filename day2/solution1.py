def function(input):
    t = 0
    for raw in input.readlines():
        line = list(map(int, raw.split()))
        p, pp = 0, 1
        increasing = True
        while pp < len(line):
            past = increasing
            diff = line[p] - line[pp]
            if abs(diff) > 3 or abs(diff) == 0:
                break 
            if diff < 0:
                increasing = True
            else:
                increasing = False
            
            if past != increasing and p != 0:
                break
            p += 1
            pp += 1
        else:
            t += 1 
    return t

if __name__ == '__main__':
    input = open("input.txt")
    print(f"Result: {function(input)}")
