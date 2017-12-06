with open('6_input.txt') as file:
    raw = file.readlines()[0].split('\t')

data = [int(r) for r in raw]
memory = [''.join(str(i) for i in data)]
cycles = 0

while True:
    max_bank = max(data)
    max_bank_idx = data.index(max_bank)

    # distribute
    data[max_bank_idx] = 0
    idx = max_bank_idx + 1
    while max_bank > 0:
        data[idx % len(data)] += 1
        idx += 1
        max_bank -= 1
    cycles += 1

    state = ''.join(str(i) for i in data)
    if state in memory:
        reappear_cycles = len(memory) - memory.index(state)
        break

    memory.append(state)

print(cycles)  # solution 1
print(reappear_cycles)  # solution 2
