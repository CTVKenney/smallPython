#!/usr/bin/env python3

import re
import os.path
import sys

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
    position = ['*****',{},'abcdefghijklmnopqrstuvwxyz']
    for wordTup in game:
        wordGuessed = wordTup[0]
        guessResults = wordTup[1]
        for i in range(5):
            if guessResults[i] == '*': #The letter indexed by i is impossible
                position[2] = position[2].replace(wordGuessed[i],'') #Remove that letter from our list of possible letters
            elif guessResults[i] == 'Y': #The letter indexed by i is used in another spot, but not position i!
                if wordGuessed[i] in position[1]:
                    position[1][wordGuessed[i]][i] = 0 #The letter now can't be used in position i either
                else:
                    position[1][wordGuessed[i]] = [1 - (j == i) for j in range(5)] #Add the letter to the dict & forbid it at position i
            elif guessResults[i] == 'G': #The letter indexed by i is correct already!
                newListVersion = list(position[0])
                newListVersion[i] = wordGuessed[i]
                position[0] = ''.join(newListVersion)
            else:
                raise Exception('The second tuple in a game position should only include asterisks, Gs, and Ys')

"""
wordPossible inputs a position (see newWordList below) and a word (5 letter string) and outputs
True if the word might be possible in the position, False otherwise
Impossible words may (very rarely) return True, but possible words will always return True.
"""
def wordPossible(position,word):
    knownSpots = position[0]
    needLetters = position[1]
    allowLetters = position[2]
    firstMatchString = knownSpots.replace('*','['+allowLetters+']')
    if re.match(firstMatchString, word):
        hasNeededLetters = True
        for letter in needLetters:
            spots = needLetters[letter]
            numLetterInGoodSpot = 0
            for i in range(5):
                if spots[i] == 1 and letter == word[i]:
                    numLetterInGoodSpot = numLetterInGoodSpot + 1
            if numLetterInGoodSpot == 0:
                hasNeededLetters = False
        return hasNeededLetters
    else:
        return False


"""
newWordList inputs a position (known information in the game) and an existing wordlist
and winnows the dictionary based on the known information.

A position is a list with: [knownSpots, needLetters, allowLetters].
knownSpots is a string like '*a**y' (has known letters in their spots and stars elsewhere).
needLetters is a dictionary { 't': [1,0,0,1,0], 'g': [1,1,1,0,1] } containing the possible spots for letters known to be in our word
allowLetters is a string 'abcdfghijklnopqrstuvwxy' of letters that could be used in the remainder of the word.
"""
def newWordList(position, wordlist):
    return [word for word in wordList if wordPossible(position, word)]
   

def main():
    print(sys.argv[1:])
    return 1

if __name__ == '__main__':
    main()
