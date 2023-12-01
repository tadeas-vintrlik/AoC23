#!/usr/bin/env python3

from functools import reduce
from operator import add, mul
import re


def is_adjacent(rows, symbol_index, num_span):
    adjacent = {
        symbol_index-1, symbol_index+1,
        symbol_index+1+rows, symbol_index+rows, symbol_index-1+rows,
        symbol_index-1-rows, symbol_index-rows, symbol_index+1-rows}
    return bool(adjacent & set(num_span))


def part1(rows, symbols, nums):
    labels = {span for index in symbols.keys()
              for span in nums.keys()
              if is_adjacent(rows, index, span)}
    return sum(map(lambda x: nums[x], labels))


def part2(rows, symbols, nums):
    # Filter out stars
    stars = [index for (index, symbol) in symbols.items() if symbol == "*"]
    # Filter out numbers adjecent to them
    coeficients = [
        [num for (span, num) in nums.items()
         if is_adjacent(rows, index, span)]
        for index in stars]
    # Filter out only those with two adjacent
    coeficients = filter(lambda x: len(x) == 2, coeficients)
    # Sum their multiples
    return sum(map(lambda x: reduce(mul, x), coeficients))


def main():
    with open('main.input', encoding='utf-8') as f:
        lines = f.readlines()
        rows = len(lines)
        chars = reduce(add, list(map(lambda x: x.strip(), lines)))

    # Dict of number index range to number value
    nums = {range(m.start(), m.end()): int(m.group(0))
            for m in re.finditer(r'(\d+)', chars)}

    # Dict of index to special character
    symbols = {m.start(): chars[m.start()]
               for m in re.finditer(r'[^\.\d]+', chars)}

    print(part1(rows, symbols, nums))
    print(part2(rows, symbols, nums))


if __name__ == "__main__":
    main()
