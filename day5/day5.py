#!/usr/bin/env python3

import re
import itertools


def num_in_range(num, rg):
    dst, src, l = rg
    return num in range(src, src + l)


def translate_numbers(nums, map_part):
    for i, num in enumerate(nums):
        for rg in map_part:
            if num_in_range(num, rg):
                dst, src, l = rg
                nums[i] = dst + (nums[i] - src)

    return nums


def part1(seeds, maps):
    next = seeds
    for mp in maps:
        next = translate_numbers(next, mp)

    return(min(next))


def main():
    with open('main.input', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    seeds = [int(seed) for seed in re.findall(r'\d+', lines[0])]

    maps = [ list(group)[1:] for k, group in itertools.groupby(lines[2:], lambda x: x == '') if not k]
    maps = [ [ tuple(map(int, line.split())) for line in mp ] for mp in maps ]

    print(part1(seeds, maps))


if __name__ == "__main__":
    main()
