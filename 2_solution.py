with open('2_input.txt') as file:
    data = file.readlines()
data = [l.rstrip().split('\t') for l in data]
data = [[int(cell) for cell in row] for row in data]

max_rows = [max(row) for row in data]
min_rows = [min(row) for row in data]
chk_rows = [max_rows[i] - min_rows[i] for i in range(len(data))]
chksum = sum(chk_rows)
print(chksum)  # solution 1

divs = []
for row in data:
    row_div = None
    for i in row:
        for j in row:
            if i != j:
                if i % j == 0:
                    row_div = i / j
                    break
        if row_div is not None:
            break
    divs.append(row_div)
print(int(sum(divs)))  # solution 2
