import re 
def print_queue(input):
    rules = []
    updates = []
    for line in input.readlines():
        if "|" in line:
            a, b = line.split("|")
            rules.append((int(a), int(b)))
        if "," in line:
            updates.append([int(a) for a in line.split(",")])
    

    for u in updates:
        p1 = 0 
        p2 = 1
        while p2 < len(u):
            for f, s in rules:
                u[p1] r[0]  
                u[p2] r[1]

    print(rules)
    print(updates)
     
if __name__ == '__main__':
    input = open("input0.txt")
    print(f"Result: {print_queue(input)}")


