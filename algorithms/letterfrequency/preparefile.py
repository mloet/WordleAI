import wordset.wordset as ws
import pandas as pd
import pickle

if __name__ == "__main__":
    words = ws.WordSet().get_solutions()
    word_dictionary = dict()

    for w in words:
        for letter in w:
            if letter not in word_dictionary:
                word_dictionary[letter] = set()
                word_dictionary[letter].add(w)
            else:
                word_dictionary[letter].add(w)

    ordered = [k for k, v in sorted(word_dictionary.items(), key=lambda item: len(item[1]))]
    frequency = dict()

    for i, order in enumerate(ordered):
        frequency[order] = i

    df = pd.DataFrame(columns=['Word', 'Power'])

    for w in words:
        power = 0
        reused = set()
        for letter in w:
            if letter not in reused:
                power += frequency[letter] * 1.5
            else:
                power += frequency[letter] * 0.3
            reused.add(letter)
        df_new = pd.DataFrame([[w, power]], columns=['Word', 'Power'])
        df = pd.concat([df, df_new], axis=0, ignore_index=True)

    with open('letter_to_word.pkl', 'wb') as f:
        pickle.dump(word_dictionary, f)
    df.to_csv('word_power.csv')
