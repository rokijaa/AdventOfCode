input = open("input.txt", "r").read()

def main():
    pos = [0,0]
    new_pos = [(0,0)]
    for i in input:
        pos[0] += {"^": 0, "v": 0, ">": 1, "<": -1}[i]
        pos[1] += {"^": 1, "v": -1, ">": 0, "<": 0}[i]
        new_pos.append(tuple(pos))
    return len(set(new_pos))
print(main())


