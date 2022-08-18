import pandas as pd
import pickle

from pathlib import Path


class LetterFrequency:

    def __init__(self):
        script = Path(__file__).absolute().parent
        with open(script / 'letter_to_word.pkl', 'rb') as f:
            self.letter_to_word = pickle.load(f)
        self.word_value = pd.read_csv(script / 'word_power.csv').set_index('Word')

    def next_word(self, goal):
        found_words = self.word_value[self.word_value.Power == self.word_value.Power.max()]
        return found_words.sample().index.values[0]

    def add_info(self, exact, close, impossible):

        for imp in list(impossible):
            self.word_value = self.word_value[~self.word_value.index.isin(self.letter_to_word[imp])]

        for (i, letter) in close:
            self.word_value = self.word_value[self.word_value.index.isin(self.letter_to_word[letter])]
            self.word_value = self.word_value[[s[i] != letter for s in self.word_value.index.values]]

        for (i, letter) in exact:
            self.word_value = self.word_value[[s[i] == letter for s in self.word_value.index.values]]
