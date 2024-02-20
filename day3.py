from runner import data
import numpy as np


def part1():
    bits = np.array([list(line) for line in data.split("\n")]).astype(int)
    gamma, epsilon = "", ""
    for i in range(0, bits.shape[1]):
        column = bits[:, i]
        gamma_bit, epsilon_bit = np.argmax(np.bincount(column)), np.argmin(np.bincount(column))
        gamma += str(gamma_bit)
        epsilon += str(epsilon_bit)
    power = int(gamma, 2) * int(epsilon, 2)
    print("part 1 =", power)


part1()
# part2()
