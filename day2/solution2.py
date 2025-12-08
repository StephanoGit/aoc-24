
def safe(line):
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
        return True 
    return False

def function(input):
    t = 0
    for raw in input.readlines():
        line = list(map(int, raw.split()))
        if safe(line):
            t += 1
        else:
           for p in range(len(line)):
                if safe(line[:p] + line[p+1:]):
                    t += 1
                    break
    return t

if __name__ == '__main__':
    input = open("input.txt")
    print(f"Result: {function(input)}")
