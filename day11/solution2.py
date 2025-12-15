from collections import Counter

def plutonian_pebbles(input):
    stones = Counter(map(int, input.readline().split()))

    for _ in range(75):
        new_stones = Counter()

        for s, count in stones.items():
            if s == 0:
                new_stones[1] += count
                continue

            digits = len(str(s))

            if digits % 2 == 0:
                mid = digits // 2
                l = int(str(s)[:mid])
                r = int(str(s)[mid:])
                new_stones[l] += count 
                new_stones[r] += count 
            else:
                new_stones[s * 2024] += count

        stones = new_stones

    return sum(stones.values())

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {plutonian_pebbles(input)}")
            
