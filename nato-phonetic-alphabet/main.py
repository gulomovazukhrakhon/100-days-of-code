import pandas as pd

with open("nato_phonetic_alphabet.csv") as df:
    data = pd.read_csv(df)

user_word = input("Enter a word: ").upper()


def convert(word):

    phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
    try:
        list_user_word = [f"{letter} for {phonetic_alphabet[letter]}" for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(list_user_word)


converted_word = convert(word=user_word)
print(converted_word)
