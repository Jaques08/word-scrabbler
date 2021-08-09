import pandas as pd
import random
import sys
import argparse

parser = argparse.ArgumentParser(description='Word scrabbling app.')
parser.add_argument("--words", help="The words to scrabble.")


args = parser.parse_args()


test_sentence = args.words

if not test_sentence:
    # Handle unadded arguments
    print("Please add words to program using --words e.g\n"
          "python scrabble.py --words \"some sentence to scrabble\"")
    exit(1)

words_to_scrabble = test_sentence.split(" ")

result = []

data = pd.read_csv(
    "words.txt",
    header=None,
    usecols=[0],
    names=['words']
)

data = data['words'].str.lower()

# Loop through words that needs to be scrabbled find the words starting with
# correct letter and then the same length.
# Out of the results a random words is chosen and appended to results to create
# a sentence to return.
for word in words_to_scrabble:
    bool_words_starting_with = data.str.startswith(word[0].lower(), na=False)
    words_starting_with = data[bool_words_starting_with]
    bool_words_len = words_starting_with.str.len() == len(word)
    words_len = words_starting_with[bool_words_len].to_list()
    result.append(random.choice(words_len)) \
        if len(words_len) else result.append(word)

print(" ".join(result))
