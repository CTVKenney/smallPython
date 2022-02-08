#!/usr/bin/env python3

import re
import os.path
import sys
from math import prod

"""
The first time we run this program, we'll
need to make the list of words for wordle from scratch.
After that we can just save it as a text file and import it from there.
re.fullmatch returns a match object if the whole string matches the pattern
"""
def makelist():
    if os.path.exists('./wordleWords.txt'):
        wordFile = open('wordleWords.txt')
        theWordFileContents = wordFile.read()
        wordle_list = theWordFileContents.splitlines()
        wordFile.close()
    else:
        from nltk.corpus import words
        word_list = words.words()
        wordle_list = [word for word in word_list if re.fullmatch(r'[a-z]{5}',word)]
        with open('wordleWords.txt', 'w+') as wordFile:
            wordFile.write('\n'.join(wordle_list))
    return sorted(wordle_list)


"""
gameToPos inputs a game (as a list of strings representing the game so far)
The list of tuples of strings so far should look like this: 
[('amaze','Y****'),('sails','*G***'),('vapor','*G***'),('watch','*GY**'),('taffy','GG**G')]
G in the location of a lowercase letter means that letter is in its correct spot
Y in the location of a lowercase letter means that letter is in the word, but not in the correct spot
and outputs a position (see newWordList below)
"""
def gameToPos(game):

"""
wordPossible inputs a position (see newWordList below) and a word (5 letter string) and outputs
1 if the word might be possible in the position, 0 otherwise
"""
def wordPossible(position,word):
    return prod([position[i][word[i]] for i in range(len(word))]) #for standard Wordle, of course, len(word) will be 5

"""
newWordList inputs a position (known information in the game) and an existing wordlist
and winnows the dictionary based on the known information.

A position is a list of length 5:
[dict0, dict1, dict2, dict3, dict4],
where dictn is a dictionary:
{'a': 1, 'b':0, 'c':1, ..., 'z':0},
and dictn[let] is 1 if let could go in position n, 0 otherwise.
"""
def newWordList(position, wordlist):
    return [word for word in wordList if wordPossible(position, word)]
   

def main():
    print(sys.argv[1:])
    return 1

if __name__ == '__main__':
    main()
