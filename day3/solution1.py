import re 
def corrupt_mul(input):
    mul = 0 
    for line in input.readlines():
        mul += sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", line))

    return mul


if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {corrupt_mul(input)}")


