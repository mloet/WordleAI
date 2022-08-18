import wordset.wordset as ws
import random


class Randomized:

    def __init__(self):
        self.wordset = list(ws.WordSet().get_solutions())
        self.yellow_letter = set()
        self.green_letter = set()
        self.black_letter = set()
        self.guesses = 0

    def next_word(self, goal):

        for letter in self.black_letter:
            self.wordset = [word for word in self.wordset if not letter in word]

        for letter, position in self.green_letter:
            self.wordset = [word for word in self.wordset if word[position] == letter]

        for letter, position in self.yellow_letter:
            self.wordset = [word for word in self.wordset if letter in word and word[position] != letter]

        guess = random.choice(self.wordset)
        self.guesses += 1
        self.wordset.remove(guess)

        return guess

    def add_info(self, exact, close, impossible):
        for position, letter in exact:
            self.green_letter.add((letter, position))

        for position, letter in close:
            self.yellow_letter.add((letter, position))

        for letter in impossible:
            self.black_letter.add(letter)
