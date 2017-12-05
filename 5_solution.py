with open('5_input.txt') as file:
    raw = file.readlines()

data = [int(l) for l in raw]
steps = 0
idx = 0

while 0 <= idx < len(data):
    instr = data[idx]
    data[idx] += 1
    idx += instr
    steps += 1

print(steps)  # solution 1

data = [int(l) for l in raw]
steps = 0
idx = 0
instr = 0

while 0 <= idx < len(data):
    instr = data[idx]
    if instr >= 3:
        data[idx] -= 1
    else:
        data[idx] += 1
    idx += instr
    steps += 1

print(steps)  # solution 2
