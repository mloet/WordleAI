import random
from pathlib import Path


class WordSet:

    def __init__(self):
        self._solutions = set()
        self._guesses = set()

        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'possiblesolutions.txt'
        with open(file_location, 'r') as file:
            lines = file.readlines()

        file.close()

        for word in lines:
            self._solutions.add(word[0:5])

        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'possibleguesses.txt'
        with open(file_location, 'r') as file:
            lines = file.readlines()

        file.close()

        for word in lines:
            self._guesses.add(word[0:5])

    def __len__(self):
        return len(self._solutions)

    def get_solutions(self):
        return self._solutions

    def get_guesses(self):
        return self._guesses

    def get_random_word(self):
        return random.choice(tuple(self._solutions))
