with open('4_input.txt') as file:
    data = file.readlines()
data = [l.rstrip().split(' ') for l in data]

num_valid = len(data)
for passphrase in data:
    if len(passphrase) > len(set(passphrase)):
        num_valid -= 1

print(num_valid)  # solution 1

num_valid = len(data)
for passphrase in data:
    sorted_pp = [''.join(sorted(word)) for word in passphrase]
    if len(sorted_pp) > len(set(sorted_pp)):
        num_valid -= 1

print(num_valid)  # solution 2