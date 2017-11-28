with open('1_input.txt') as file:
    data = file.read()
    data = list(data)
    data = [int(c) for c in data[:-1]]

target_nums = [data[-i-1] if data[-i-1] == data[-i] else 0
               for i in range(len(data))]
print(sum(target_nums))
