#!/usr/bin/env python3

import re
from functools import reduce
from operator import mul, add


def num_beatable_ways(race):
    time = race[0]
    distance = race[1]
    out = [(time-speed) * speed for speed in range(1, time)]
    return len(list(filter(lambda x: x > distance, out)))


def part1(lines):
    return reduce(mul, map(num_beatable_ways, lines))


def part2(line):
    return num_beatable_ways(line)


def join_line_num(line):
    nums = re.findall(r'\d+', line)
    return int(reduce(add, nums))


def main():
    with open('main.input', encoding='utf-8') as f:
        lines = f.readlines()

        # Lines for part 1
        lines1 = [list(map(int, re.findall(r'\d+', line)))
                  for line in lines]
        # First index in tuple is time, second is distance
        lines1 = list(zip(lines1[0], lines1[1]))

        lines2 = (join_line_num(lines[0]), join_line_num(lines[1]))

    print(part1(lines1))
    print(part2(lines2))


if __name__ == "__main__":
    main()
