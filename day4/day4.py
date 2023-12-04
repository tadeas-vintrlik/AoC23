#!/usr/bin/env python

import re


def parse_scratch_cards(file_name):
    with open(file_name, encoding='utf-8') as f:
        return [
            # One is the count of cards for part2
            (winning, our, 1) for (winning, our)
            in map(
                lambda x: (re.findall(r'\d+', x[0]), re.findall(r'\d+', x[1])),
                map(lambda x: x.strip().split(':')[1].split('|'),
                    f.readlines()))]


def matching(card):
    return len(set(card[0]) & set(card[1]))


def card_value(card):
    return 2 ** (matching(card)) // 2


def part1(cards):
    return sum(map(card_value, cards))


def part2(cards):
    for i, card in enumerate(cards):
        for j in range(i+1, min(len(cards), i+matching(card)+1)):
            orig_card = cards[j]
            cards[j] = (orig_card[0], orig_card[1], orig_card[2] + card[2])
    return sum(map(lambda x: x[2], cards))


def main():
    file_name = 'main.input'
    cards = parse_scratch_cards(file_name)
    print(part1(cards))
    print(part2(cards))


if __name__ == "__main__":
    main()
