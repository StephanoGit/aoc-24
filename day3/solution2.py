import re


def corrupt_mul(input):
    mul = 0 
    enable = True
    
    text = input.read()
    instructions = []
   
    # goes through string only once:
    # Single regex that captures all three patterns
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"


    for m in re.finditer(r"mul\((\d+),(\d+)\)", text):
        instructions.append(('mul', m.start(), int(m.group(1)), int(m.group(2))))
    
    for m in re.finditer(r"do\(\)", text):
        instructions.append(('do', m.start(), None, None))
    
    for m in re.finditer(r"don't\(\)", text):
        instructions.append(('dont', m.start(), None, None))
    
    instructions.sort(key=lambda x: x[1])
    
    for instr, _, a, b in instructions:
        if instr == 'do':
            enable = True
        elif instr == 'dont':
            enable = False
        elif instr == 'mul' and enable:
            mul += a * b
    
    return mul


if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {corrupt_mul(input)}")


