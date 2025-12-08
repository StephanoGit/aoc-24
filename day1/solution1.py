def find_distance(input):
    left, right = [], []
    distance = 0
    len = 0
    for line in input.readlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
        len += 1

    left.sort() 
    right.sort()

    for i in range(len):
        distance += abs(left[i] - right[i])

    return distance

if __name__ == '__main__':
    input = open("input.txt")
    print(f"Result: {find_distance(input)}")
    
