
def plutonian_pebbles(input):
    stones = list(map(int, input.readline().split()))

    for _ in range(25):
        new_stones = []

        for s in stones:
            if s == 0:
                new_stones.append(1)
                continue

            digits = len(str(s))

            if digits % 2 == 0:
                mid = digits // 2
                l = int(str(s)[:mid])
                r = int(str(s)[mid:])
                new_stones.extend([l, r])
            else:
                new_stones.append(s * 2024)

        stones = new_stones

    return len(stones)

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {plutonian_pebbles(input)}")
            
