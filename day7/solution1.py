def bridge_repair(input):
    ops = [] 
    for line in input.readlines():
        parts = line.replace(':', ' ').split()
        target = int(parts[0])
        numbers = [int(x) for x in parts[1:]]
        ops.append((target, numbers))


    def check_op(target, numbers, index, current):
        if index == len(numbers):
            return current == target

        next_num = numbers[index]

        if check_op(target, numbers, index + 1, current * next_num):
            return True

        if check_op(target, numbers, index + 1, current + next_num):
            return True

        return False

    total = 0
    for target, numbers in ops:
        if check_op(target, numbers, 1, numbers[0]):
            total += target
    
    return total

if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {bridge_repair(input)}")


    
    
