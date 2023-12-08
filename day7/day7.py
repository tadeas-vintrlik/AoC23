#!/usr/bin/env python3

from functools import total_ordering
from enum import Enum


CARDS = "AKQJT98765432"
CARDS2 = "AKQT98765432J"


@total_ordering
class HandType(Enum):
    FIVE_OF_KIND = 7
    FOUR_OF_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH = 1

    def __gt__(self, other):
        return self.value > other.value


@total_ordering
class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.counts = {
            symbol: self.hand.count(symbol)
            for symbol in set(self.hand)
        }

    def __repr__(self):
        return f'"{self.hand} {self.bid}"'

    def get_type(self):
        values = list(self.counts.values())
        of_kind = max(values)
        if of_kind == 5:
            return HandType.FIVE_OF_KIND
        if of_kind == 4:
            return HandType.FOUR_OF_KIND
        if 2 in values and 3 in values:
            return HandType.FULL_HOUSE
        if of_kind == 3:
            return HandType.THREE_OF_KIND
        if values.count(2) == 2:
            return HandType.TWO_PAIR
        if 2 in values:
            return HandType.PAIR
        return HandType.HIGH

    def __gt__(self, other):
        if self.get_type() != other.get_type():
            return self.get_type() > other.get_type()
        for i, _ in enumerate(self.hand):
            if self.hand[i] == other.hand[i]:
                continue
            return CARDS.index(self.hand[i]) < CARDS.index(other.hand[i])


class HandJoker(Hand):

    def __init__(self, hand, bid):
        Hand.__init__(self, hand, bid)
        self.jokerize()

    def jokerize(self):
        if "J" in self.counts:
            jokers = self.counts["J"]
            del self.counts["J"]
            try:
                max_key = max(self.counts, key=self.counts.get)
            except ValueError:
                max_key = "J"
                self.counts[max_key] = 0
            self.counts[max_key] = self.counts[max_key] + jokers

    def __gt__(self, other):
        if self.get_type() != other.get_type():
            return self.get_type() > other.get_type()
        for i, _ in enumerate(self.hand):
            if self.hand[i] == other.hand[i]:
                continue
            return CARDS2.index(self.hand[i]) < CARDS2.index(other.hand[i])


def get_value(game):
    return sum(rank * hand.bid for rank, hand in enumerate(game, start=1))


def part1(game):
    return (get_value(sorted(list(map(lambda x: Hand(*x), game)))))


def part2(game):
    return (get_value(sorted(list(map(lambda x: HandJoker(*x), game)))))


def main():
    with open('main.input', encoding='utf-8') as f:
        # Parse a list of tuples of hand and bid
        game = [tuple(line.split()) for line in f.readlines()]
        game = list(map(lambda x: (x[0], int(x[1])), game))
    print(part1(game))
    print(part2(game))


if __name__ == "__main__":
    main()
