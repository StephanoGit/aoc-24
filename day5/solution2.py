
def print_queue(input):
    rules = []
    updates = []
    for line in input.readlines():
        if "|" in line:
            a, b = line.split("|")
            rules.append((int(a), int(b)))
        if "," in line:
            updates.append([int(a) for a in line.split(",")])
    

    def check_update(update):
        modified = False
        i = 0
        while i < len(rules):
            f, s = rules[i]
            if f in update and s in update:
                f_index_in_u = update.index(f)
                s_index_in_u = update.index(s)
                if f_index_in_u > s_index_in_u:
                    update[f_index_in_u] = s
                    update[s_index_in_u] = f
                    modified = True 
                    i = 0 
            i += 1
        return modified

    valid_updates = []

    for u in updates:
        if check_update(u):
            valid_updates.append(u) 
  
    return sum(u[len(u)//2] for u in valid_updates)

     
if __name__ == '__main__':
    input = open("input1.txt")
    print(f"Result: {print_queue(input)}")


