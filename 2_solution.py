with open('2_input.txt') as file:
    data = file.readlines()
data = [l.rstrip().split('\t') for l in data]
data = [[int(cell) for cell in row] for row in data]
max_rows = [max(row) for row in data]
min_rows = [min(row) for row in data]
chk_rows = [max_rows[i] - min_rows[i] for i in range(len(data))]
chksum = sum(chk_rows)
print(chksum)
