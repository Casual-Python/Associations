# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import
# pylint: disable=W0614
# pylint: disable=R0913
"""
Create game environment


class Card:
    pass
"""
import random
import sys
import logging as log


class Game:
    def __init__(self, horizontal=5, vertical=5, reds=9, blues=8, blacks=1):
        self.horizontal = horizontal
        self.vertical = vertical
        self.reds = reds
        self.blues = blues
        self.blacks = blacks
        self.field_size = horizontal * vertical
        self.field = self.create_field()
        log.info(self.field)

    def open_file(self):
        log.info(sys.executable)
        with open("data/words_list_eng_v1.txt", "r") as data_file:
            return random.sample(data_file.readlines(), self.field_size)

    def create_field(self):
        words = self.open_file()
        random.shuffle(words)
        orders = list(range(self.field_size))
        random.shuffle(orders)
        return {
            position: (word, self.color(i))
            for word, position, i in zip(words, orders, range(self.field_size))
        }

    def color(self, i):
        if i < self.reds:
            return "RED"
        if i < self.reds + self.blues:
            return "BLUE"
        if i < self.field_size - self.blacks:
            return "WHITE"
        return "BLACK"
