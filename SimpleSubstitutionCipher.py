import WordPower

import random
import os


def decipher(encrypted, words):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    temp = alphabet[:]
    random.shuffle(list(temp))

    bestGuess = WordPower.WordPowerObject(sentence=decrypt(buildDictionary(alphabet,temp),temp),words=words,password=temp,shift=None)
    currentKey = alphabet
    attempt = 0
    while True:
        attempt+=1
        count = 0
        bestGuessCpy = list(bestGuess.password)
        random.shuffle(bestGuessCpy)
        while count < 1000:
            x = random.randint(0, 25)
            y = random.randint(0, 25)
            child = bestGuessCpy.copy()
            # swap two characters in the child
            temp1 = child[x]
            child[x] = child[y]
            child[y] = temp1
            length = len(child)
            if length != 26:
                print(''.join(child))
            dictionary = buildDictionary(alphabet,''.join(child))
            deciphered = WordPower.WordPowerObject(sentence=decrypt(dictionary=buildDictionary(alphabet,''.join(child)),encrypted=encrypted),words=words,password=child,shift=None)
            # if the child was better, replace the parent with it
            if deciphered.counter > bestGuess.counter:
                bestGuess = deciphered
                count = 0
            count = count + 1
            clear = lambda: os.system('cls')
            clear()
            print("Current Guess: " + deciphered.sentence + " Key: " + str(deciphered.password) + " Strength: " + str(deciphered.counter))
            print("Best Guess:" + bestGuess.sentence + " Key: " + str(bestGuess.password) + " Strength: " + str(bestGuess.counter))

def buildDictionary(alphabet, key):
    dict = {}

    for x in range(0,len(alphabet),1):
        dict[key[x]] = alphabet[x]
    return dict

def decrypt(dictionary, encrypted):
    result = ""
    for char in encrypted:
        if char in dictionary:
            result+=dictionary[char]
        else:
            print(dictionary)
    return result
