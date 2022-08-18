import wordset.wordset as ws
from colorama import init, Fore, Back, Style, deinit, reinit


class WordleGame:

    def __init__(self):
        self._ws = ws.WordSet()
        self._all_words = self._ws.get_solutions().union(self._ws.get_guesses())
        self._possible_goal = self._ws.get_solutions()
        self._possible_support = self._ws.get_guesses()
        self._goal = self._ws.get_random_word()

    def play_game(self, engine=None):
        self.new_random_word()
        guessed_words = list()

        if not engine:
            init(autoreset=True)
            print(Back.BLACK + Fore.LIGHTWHITE_EX +
                  Style.BRIGHT + 'Welcome to Wordle!')
            deinit()

            while len(guessed_words) < 6 and self._goal not in guessed_words:
                self._wordle_format_ui(guessed_words)
                guessed_words = self._wordle_guessing_ui(guessed_words)

            reinit()
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                  'Game End! Word was ' + self._goal + '.')
            deinit()
            self._wordle_format_ui(guessed_words, True)

        else:
            guessed_words = self.run_algo(engine)

        return self._goal in guessed_words, len(guessed_words)

    def run_algo(self, algo):
        guesses = list()
        while self._goal not in guesses and len(guesses) < 6:  ## need length of guesses to be less than six
            new_guess = algo.next_word(self._goal)
            guesses.append(new_guess)
            exact, close, impossible = self.get_matches([new_guess])
            exact = exact[0]
            close = close[0]
            algo.add_info(exact, close, impossible)

        return guesses

    def new_random_word(self):
        self._goal = self._ws.get_random_word()

    def get_matches(self, guessed):
        exact = dict()
        close = dict()
        impossible = set()
        for i, word in enumerate(guessed):
            exact[i] = list()
            close[i] = list()
            for j, letter in enumerate(word):
                if letter == self._goal[j]:
                    exact[i].append((j, letter))
                elif letter in self._goal:
                    close[i].append((j, letter))
                else:
                    impossible.add(letter)

        return exact, close, impossible

    def _wordle_format_ui(self, guessed, end=False):
        reinit()

        for word in guessed:
            for j, letter in enumerate(word):
                if letter == self._goal[j]:
                    print(Back.GREEN + Fore.LIGHTWHITE_EX +
                          Style.BRIGHT + ' ' + letter + ' ', end=' ')
                elif letter in self._goal:
                    print(Back.YELLOW + Fore.LIGHTWHITE_EX +
                          Style.BRIGHT + ' ' + letter + ' ', end=' ')
                else:
                    print(Back.WHITE + Fore.LIGHTWHITE_EX +
                          Style.BRIGHT + ' ' + letter + ' ', end=' ')
            print()

        for guess in range(6 - len(guessed)):
            for letter in range(5):
                print(Back.WHITE + Fore.LIGHTWHITE_EX +
                      Style.BRIGHT + '   ', end=' ')
            print()

        if not end:
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                  'You currently have ' + str(6 - len(guessed)) + ' guesses.')
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                  'Input your next guess: ', end='')
            deinit()

    def _wordle_guessing_ui(self, guessed):
        new_guess = input().lower()

        while (len(new_guess) != 5 or
               not new_guess.isalpha() or
               new_guess in guessed or
               new_guess not in self._all_words):
            reinit()
            if len(new_guess) != 5:
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'Word must be of length five!')
            if not new_guess.isalpha():
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'Word must be made of alphabetical letters!')
            if new_guess in guessed:
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'Word cannot have been guessed already!')
            if new_guess not in self._all_words:
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'Word must be a valid word!')

            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                  'Invalid input. Please input a valid guess:', end='')

            deinit()
            new_guess = input().lower()

        guessed.append(new_guess)

        return guessed

    def get_word(self):
        return self._goal

    def get_possible_words(self):
        return self._all_words
