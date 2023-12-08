#!/usr/bin/env python3

import re
import math


def next_step(maps, direction, current):
    return maps[current][direction]


def solve(maps, directions, currents):
    steps = 0
    end_steps = {}
    while len(end_steps) != len(currents):
        direction = directions[steps % len(directions)]
        steps = steps + 1
        currents = list(map(lambda x: next_step(maps, direction, x), currents))
        for current in currents:
            if "Z" in current and current not in end_steps:
                end_steps[current] = steps
    return math.lcm(*end_steps.values())


def part1(maps, directions):
    return solve(maps, directions, ["AAA"])


def part2(maps, directions):
    return solve(maps, directions,
                 list(filter(lambda x: "A" in x, maps.keys())))


def main():
    with open('main.input', encoding='utf-8') as f:
        lines = f.readlines()
    directions = [{'L': 0, 'R': 1}[char] for char in lines[0].strip()]
    maps = [re.findall(r'\w{3}', line) for line in lines[2:]]
    maps = {x[0]: (x[1], x[2]) for x in maps}
    print(part1(maps, directions))
    print(part2(maps, directions))


if __name__ == '__main__':
    main()
