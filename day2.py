from runner import data
from parse import parse


def part1():
    horizontal, depth = 0, 0
    for line in data.split("\n"):
        (direction, amount) = parse("{} {:d}", line)
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
    print("part 1 =", horizontal * depth)


def part2():
    horizontal, depth, aim = 0, 0, 0
    for line in data.split("\n"):
        (direction, amount) = parse("{} {:d}", line)
        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    print("part 2 =", horizontal * depth)


part1()
part2()
