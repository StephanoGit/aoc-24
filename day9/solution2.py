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

    for curr_id in range(file_id - 1, -1, -1):
        curr_file_start = disk.index(curr_id)

        curr_file_len = 0
        for i in range(curr_file_start, len(disk)):
            if disk[i] == curr_id:
                curr_file_len += 1 
            else:
                break

        window_size = 0
        new_spot = -1

        for i in range(curr_file_start):
            if disk[i] == ".":
                window_size += 1 
                if window_size == curr_file_len:
                    new_spot = i - curr_file_len + 1 
                    break 
            else:
                window_size = 0

        if new_spot != -1:
            disk[curr_file_start : curr_file_start + curr_file_len] = ["."] * curr_file_len
            disk[new_spot : new_spot + curr_file_len] = [curr_id] * curr_file_len
    
    sum = 0
    for i, n in enumerate(disk):
        if n == ".":
            continue
        sum += i * int(n)

    print(disk)

    return sum 

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {disk_fragmenter(input)}")
            
