with open('1_input.txt') as file:
    data = file.read()
    data = list(data)
    data = [int(c) for c in data[:-1]]

full = len(data)
target_nums = [data[i] if data[(i+1) % full] == data[i] else 0
               for i in range(full)]
print(sum(target_nums))  # solution 1

half = full // 2
target_nums = [data[i] if data[(i+half) % full] == data[i] else 0
               for i in range(full)]
print(sum(target_nums))  # solution 2
