with open('7_input.txt') as file:
    raw = file.readlines()

data = [r.strip().replace(',', '').split(' ') for r in raw]
programs = [l[0] for l in data]

for l in data:
    if '->' in l:
        p_progs = l[3:]
        for p in p_progs:
            programs.remove(p)

print(programs)  # solution 1
