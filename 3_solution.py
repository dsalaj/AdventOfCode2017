input = 265149
tmp = 265149 - 1

circle_idx = 1
while tmp > circle_idx * 8:
    tmp -= circle_idx * 8
    circle_idx += 1

print("circle index ", circle_idx)
print("circle size  ", circle_idx * 8)
print("idx in circle", tmp)
print("side length  ", circle_idx * 8 / 4)
print("side in circ ", (tmp // (circle_idx * 2)) + 1)
print("idx in side  ", tmp % (circle_idx * 2))
print("side center  ", (circle_idx * 2) / 2)
print("dist from side center", abs((tmp % (circle_idx * 2)) - ((circle_idx * 2) / 2)))
print("manhattan distance", abs((tmp % (circle_idx * 2)) - ((circle_idx * 2) / 2)) + circle_idx)
print("manhattan distance", tmp % (circle_idx * 2))  # solutions 1

# OEIS.org
# A141481 Square spiral of sums of selected preceding terms, starting at 1.
# Author: Niclas Rantala Aug 09 2008


def sum_neighbors_(field, pos):
    return field[pos[0]+1, pos[1]] + \
           field[pos[0]-1, pos[1]] + \
           field[pos[0], pos[1]+1] + \
           field[pos[0], pos[1]-1] + \
           field[pos[0]+1, pos[1]+1] + \
           field[pos[0]-1, pos[1]+1] + \
           field[pos[0]+1, pos[1]-1] + \
           field[pos[0]-1, pos[1]-1]


def sum_neighbors(field, pos):
    res = int(sum_neighbors_(field, pos))
    if res > input:
        print(res)  # solution 2
        exit(0)
    else:
        return res

side = int(circle_idx * 8 / 4 + 1)
side += 2  # expand so sum_neighbors does not fail on edges
import numpy as np
field = np.zeros((side, side))
pos = [side//2, side//2]
field[pos[0], pos[1]] = 1
# right
pos[0] += 1
field[pos[0], pos[1]] = sum_neighbors(field, pos)

while True:
    # up
    while field[pos[0]-1, pos[1]] != 0:
        pos[1] += 1
        field[pos[0], pos[1]] = sum_neighbors(field, pos)
    # left
    while field[pos[0], pos[1]-1] != 0:
        pos[0] -= 1
        field[pos[0], pos[1]] = sum_neighbors(field, pos)
    # down
    while field[pos[0]+1, pos[1]] != 0:
        pos[1] -= 1
        field[pos[0], pos[1]] = sum_neighbors(field, pos)
    # right
    while field[pos[0], pos[1]+1] != 0:
        pos[0] += 1
        field[pos[0], pos[1]] = sum_neighbors(field, pos)

