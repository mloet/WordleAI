import algorithms.trie.trie as tr
import wordset.wordset as ws


class TrieEngine:

    def __init__(self):
        words = ws.WordSet()
        self.struct = tr.Trie(words.get_solutions())
        self.must_have = set()

    def next_word(self):
        i = 0
        new_word = ""

        while all(must in new_word for must in self.must_have) and i < 1000 and len(new_word) != 5:
            self.struct.clean_trie(new_word)
            new_word = self.struct.get_word()
            i += 1

        if not all(must in new_word for must in self.must_have) and len(new_word) != 5:
            raise Exception('Time Out on searching for Word')

        return new_word

    def add_info(self, exact, close, impossible):
        for position, letter in exact:
            self.struct.only_letter(letter, position)

        for position, letter in close:
            self.struct.remove_letter_single(letter, position)
            self.must_have.add(letter)

        for letter in impossible:
            self.struct.remove_letter_all(letter)