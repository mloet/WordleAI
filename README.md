# WordleAI

## Downloading and setup

Please clone the repository to get the source code for the game and the algorithm and AI. To install all dependencies, run ``pip install requirements.txt`` in order to be able to run the alorithms and the game.

## Set Up UI for User

To play wordle with a simple graphic UI, run ``python3 runwordle.py`` in the terminal. It will play the game on the terminal.

## Working with Algorithms

To play wordle with a specific algorithm, run ``python3 runwordle.py {'algo', 'Algo', 'algorithm', 'Algorithm', 'run_algo'} {'Trie', 'All'}`` where the first additional argument specifies an algorithm should be used and the second argument are the algorithms to run. If a second argument is not specified, ``'All'`` will be used as default.
