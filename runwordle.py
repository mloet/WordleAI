import wordlegame
import runalgo
import sys

from colorama import init, Fore, Back, Style

if __name__ == '__main__':
    run_algo = ['algo', 'Algo', 'algorithm', 'Algorithm', 'run_algo']
    if any(special in run_algo for special in sys.argv):
        runalgo.run_all(1000)
    else:
        game = wordlegame.WordleGame()
        end_state, _ = game.play_game()

        init(autoreset=True)
        if end_state:
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'You Won!')
        else:
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'You Lost!')
