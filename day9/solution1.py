def disk_fragmenter(input):
    disk_map = input.readline().strip()
    
    disk = [] 
    file_id = 0
    
    for i, char in enumerate(disk_map):
        length = int(char)
        if i % 2 == 0:
            disk.extend([file_id] * length)
            file_id += 1
        else:
            disk.extend(["."] * length)

    l, r = 0, len(disk) - 1
    while l < r:
        while l < r and disk[l] != ".":
            l += 1

        while l < r and disk[r] == ".":
            r -= 1

        if l < r:
            disk[l] = disk[r]
            disk[r] = "."
            r -= 1
            l += 1
    
    sum = 0
    for i, n in enumerate(disk):
        if n == ".":
            break
        sum += i * int(n)

    return sum 

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {disk_fragmenter(input)}")
            
