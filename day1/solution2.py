from collections import defaultdict

def similarity_score(input):
    left = []
    occ = defaultdict(int)
    score = 0

    for line in input.readlines():
        l, r = line.split()
        left.append(int(l))
        occ[int(r)] += 1
    
    for val in left:
        score += val * occ[val]

    return score 

if __name__ == '__main__':
    input = open("input.txt")
    print(f"Result: {similarity_score(input)}")
    
