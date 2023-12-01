#!/usr/bin/env python3

import functools


def extrapolate_next_number(diffs):
    return sum([diff[-1] for diff in diffs])


def extrapolate_previous_number(diffs):
    return functools.reduce(lambda x, y: y - x, reversed([diff[0] for diff in diffs]))


def generate_diffs(line):
    diffs = [line]
    while not all(x == 0 for x in diffs[-1]):
        diffs.append([ diffs[-1][i+1] - diffs[-1][i] for i in range(len(diffs[-1])-1)])
    return diffs


def part1(lines):
    return sum(map(lambda x: extrapolate_next_number(generate_diffs(x)), lines))


def part2(lines):
    return sum(list(map(lambda x: extrapolate_previous_number(generate_diffs(x)), lines)))


def main():
    with open('main.input', encoding='utf-8') as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
