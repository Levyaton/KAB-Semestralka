from ear.WordPower import WordPowerObject
# I followed the tutorial at this link: https://www.geeksforgeeks.org/program-to-perform-a-letter-frequency-attack-on-a-monoalphabetic-substitution-cipher/, then made my own modifications
import random

from ear.githubLibraries.substitution import Substitution


def getDict(shift, alphabet):
    dict = {}
    for x in range(0,len(alphabet),1):
        dict[alphabet[(x + shift)%len(alphabet)]]=alphabet[x]
    return dict

def decrypt(encrypted, shift, alphabet, words):
    decrypted = ""
    dict= getDict(shift=shift,alphabet=alphabet)
    for char in encrypted:
        decrypted += dict[char]
    return WordPowerObject(sentence=decrypted,shift=shift,password=None,words=words)

def decipher(encrypted, words, filename, alphabet):
    results = []
    for x in range(len(alphabet)):
        results.append(decrypt(encrypted=encrypted,words=words,alphabet=alphabet,shift=x))
    return results
