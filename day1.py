from runner import data


def part1():
    vals = [int(line) for line in data.split("\n")]
    prev = vals[0]
    increase_count = 0
    for val in vals[1:]:
        increase_count += 1 if val > prev else 0
        prev = val
    print("part 1 =", increase_count)


def part2():
    vals = [int(line) for line in data.split("\n")]
    prev = sum(vals[:3])
    increase_count = 0
    for i in range(1, len(vals) - 2):
        increase_count += 1 if sum(vals[i : i + 3]) > prev else 0
        prev = sum(vals[i : i + 3])
    print("part 2 =", increase_count)


part1()
part2()
