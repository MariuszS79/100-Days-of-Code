import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv(r'nato_phonetic_alphabet.csv')
letters = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word: ").upper()
by_nato = [letters[letter] for letter in word]
print(by_nato)
