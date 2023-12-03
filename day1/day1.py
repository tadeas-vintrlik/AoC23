#!/usr/bin/env/python3

import re

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine']


def part1(in_file: str):
    with open(in_file, encoding='utf-8') as file:
        print(sum(map(first_last_digit_num, file.readlines())))


def part2(in_file: str):
    with open(in_file, encoding='utf-8') as file:
        print(sum(map(first_last_digit_word_num, file.readlines())))


def first_last_digit_num(line: str) -> int:
    s = re.findall(r'([0-9])', line)
    return int(s[0] + s[-1])


def word_num_to_num(n: str):
    if n in list(map(str, range(0, 10))):
        return n
    return str(digits.index(n) + 1)


def first_last_digit_word_num(line: str):
    re_string = r'(?=([0-9]|' + '|'.join(digits) + r'))'
    s = re.findall(re_string, line)
    s = list(map(word_num_to_num, s))
    r = int(s[0] + s[-1])
    return r


def main():
    in_file = 'main.input'
    part1(in_file)
    part2(in_file)


if __name__ == "__main__":
    main()
