import pandas as pd
import random
import argparse


def scrabble_sentence(sentence):
    """
    Read the data from text file.
    Loop through words that needs to be scrabbled find the words starting
    with correct letter and then the same length.
    Out of the results a random words is chosen and appended to results
    to create a sentence to return.

    :param sentence: The sentence to scrabble.
    :return: List of found words.
    """
    words_to_scrabble = sentence.split(" ")

    result = []

    data = pd.read_csv(
        "words.txt",
        header=None,
        usecols=[0],
        names=['words']
    )

    data = data['words'].str.lower()

    for word in words_to_scrabble:
        if word == "":
            raise Exception(f"Incorrect word not valid: {word}")
        bool_words_starting_with = data.str.startswith(
            word[0].lower(),
            na=False
        )
        words_starting_with = data[bool_words_starting_with]
        bool_words_len = words_starting_with.str.len() == len(word)
        words_len = words_starting_with[bool_words_len].to_list()
        result.append(random.choice(words_len)) \
            if len(words_len) else result.append(word)

    return " ".join(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word scrabbling app.')
    parser.add_argument("--words", help="The words to scrabble.")

    args = parser.parse_args()

    sentence = args.words

    if not sentence:
        raise Exception("Please add words to program using --words e.g\n"
                         "python scrabble.py --words \"some sentence "
                         "to scrabble\"")
    else:
        result = scrabble_sentence(sentence=sentence)
        print(result)
