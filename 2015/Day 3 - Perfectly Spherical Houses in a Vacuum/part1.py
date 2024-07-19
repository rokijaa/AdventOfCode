file = open("input.txt").read().split()

position = (0, 0)

for i in file:
    x, y = position
    if i == '>':
        x += 1
    elif i == '<':
        x -= 1
    elif i == 'v':
        y += 1
    elif i == '^':
        y -= 1
    newPos = position.add(x,y)
print(newPos)

