import wordset.wordset as ws
from pathlib import Path
import json


class Entropy:

    def __init__(self):
        self.wordset = list(ws.WordSet().get_solutions())

        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'ent_data.json'
        with open(file_location, 'r') as json_file:
            json_load = json.load(json_file)

        self.frequency = list({k: v for k, v in sorted(
            json_load.items(), key=lambda item: item[1], reverse=True)}.items())
        self.yellow_letter = set()
        self.green_letter = set()
        self.black_letter = set()

    def get_entropy(freq):
        return freq

    def next_word(self):
        if len(self.wordset) == 0:
            self.wordset = list(ws.WordSet().get_solutions())
            script_location = Path(__file__).absolute().parent
            file_location = script_location / 'frequency.json'
            with open(file_location, 'r') as json_file:
                json_load = json.load(json_file)
            self.frequency = list({k: v for k, v in sorted(
                json_load.items(), key=lambda item: item[1], reverse=True)}.items())

        for letter in self.black_letter:
            self.wordset = [
                word for word in self.wordset if not letter in word]

        for letter, position in self.green_letter:
            self.wordset = [
                word for word in self.wordset if word[position] == letter]

        for letter, position in self.yellow_letter:
            self.wordset = [
                word for word in self.wordset if letter in word and word[position] != letter]

        self.frequency = [
            pair for pair in self.frequency if self.wordset.count(pair[0]) == 1]

        guess = self.wordset[0]

        self.wordset.remove(guess)
        return guess

    def add_info(self, exact, close, impossible):
        for position, letter in exact:
            self.green_letter.add((letter, position))

        for position, letter in close:
            self.yellow_letter.add((letter, position))

        for letter in impossible:
            self.black_letter.add(letter)
