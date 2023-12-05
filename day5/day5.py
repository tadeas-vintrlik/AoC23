#!/usr/bin/env python3

import re
import itertools


def range_almanac_map(nums):
    nums = list(map(int, re.findall(r'\d+', nums)))
    return (
        range(nums[0], nums[0] + nums[2]),
        range(nums[1], nums[1] + nums[2]),
    )


def part1(seeds, maps):
    pass


def main():
    with open('test.input', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    seeds = {int(seed) for seed in re.findall(r'\d+', lines[0])}

    maps = [ list(group)[1:] for k, group in itertools.groupby(lines[2:], lambda x: x == '') if not k]
    maps = [ [ range_almanac_map(line) for line in mp ] for mp in maps]
    print(maps)


if __name__ == "__main__":
    main()
