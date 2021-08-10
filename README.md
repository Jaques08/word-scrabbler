
# Word-Scrabbler

## Description

 - The main purpose is to scrabble words returning words starting with the same letter and same length word. 
 - It accepts sentences and handles each word individually

## Requirements
- pandas==1.3.1
- python==3.8

## Getting started
Make sure python is installed. 
Copy the following and paste it into terminal (first time setup only)
```
git clone https://github.com/Jaques08/word-scrabbler.git
cd word-scrabbler/
pip install -r requirements.txt
```
## Using the program
To run the program after running the setup use the following command.
```
python scrabble.py --words "some sentence to scrabble"
```
Which should return something like:
```
sane soldered to shuffler
```
## Updating words
Should there be new words to train against the text file can be copied into folder and renamed to `words.txt`

## Developement

To run tests run:
```
pytest tests.py 
```
