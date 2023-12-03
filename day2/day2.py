#!/usr/bin/env python3

import re


def parse_game(line):
    return {**{color: max(map(int, re.findall(r'(\d+) ' + color, line)))
               for color in ['red', 'green', 'blue']},
            **{'id': parse_id(line)}}


def parse_id(line):
    return int(re.search(r'Game (\d+): (.*)', line).group(1))


def is_possible(game):
    max_red = 12
    max_green = 13
    max_blue = 14
    return (game['red'] <= max_red and
            game['green'] <= max_green and
            game['blue'] <= max_blue)


def part1(games):
    return sum(map(lambda x: x['id'], filter(is_possible, games)))


def part2(games):
    return sum(map(lambda x: x['red'] * x['blue'] * x['green'], games))


def main():
    with open('main.input', encoding='utf-8') as file:
        lines = file.readlines()
        games = [parse_game(line) for line in lines]
    print(part1(games))
    print(part2(games))


if __name__ == "__main__":
    main()
