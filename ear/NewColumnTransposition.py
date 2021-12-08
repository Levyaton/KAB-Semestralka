import math
from collections import OrderedDict

import re
import string
from pycipher import Caesar, ColTrans
from collections import OrderedDict
from itertools import permutations
from future.utils import iteritems
from future.utils import listitems
from ear import WordPower
from pycipher import ColTrans
from functools import reduce


def getKey(col_length):
    key = ""
    for x in range(int(col_length)):
        if x < 10 :
            key += "0"
        if x <100:
            key += "0"
        key += str(x)

    return [key[i:i+3] for i in range(0, len(key), 3)]


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def decrypt(key, encrypted, col_length):
    decriphered = ""
    for x in range(len(encrypted[0])):
        for index in key:
            decriphered += encrypted[int(index) + int(x * col_length)]
    print("Guessing: " + decriphered)
    return decriphered


def decipher(encrypted, words, filename, alphabet):
    length = len(encrypted)
    f = factors(length)
    results = []
    counter = 0
    for factor in f:
        counter += 1
        print(str(counter) + " / " + str(len(f)))
        column_length = length / factor
        temp = breakCipher(column_count=factor, column_length=column_length, encrypted=encrypted, words=words)
        if temp is not None:
            results.extend(temp)
            # results.sort(key=lambda x: x.counter, reverse=True)
            # results = results[:25]
    return results


def breakCipher(column_count, column_length, encrypted, words):
    results = []
    max = 15
    min = 2
    # Skip checking absurdly long tables, as they would make the program crash, due to memory consumption
    if max > column_count:
        perms = permutations([''.join(p) for p in permutations(getKey(column_count))])
        for p in perms:
            for key in p:
                results.append(
                    WordPower.WordPowerObject(sentence=decrypt(key=key, encrypted=encrypted, col_length=column_length),
                                              shift=None, password=p, words=words))
                results.append(
                    WordPower.WordPowerObject(sentence=decryptRow(key=key, encrypted=encrypted, col_length=column_length, col_count=column_count),
                                          shift=None, password=p, words=words))
        return results


def decipherTable(encrypted, words, filename, alphabet):
    length = len(encrypted)
    f = factors(length)
    results = []
    for factor in f:
        column_length = length / factor
        print(str(factor) +  " / " + str(column_length))
        results.append(WordPower.WordPowerObject(
            sentence=decrypt(key=getKey(column_length), encrypted=encrypted, col_length=int(column_length)), shift=None,
            password=str(factor) + " x " + str(column_length), words=words))
        results.append(WordPower.WordPowerObject(
            sentence=decryptRow(key=getKey(column_length), encrypted=encrypted, col_length=int(column_length),col_count=int(factor)), shift=None,
            password=str(factor) + " x " + str(column_length), words=words))
    return results

def decryptRow(key, encrypted, col_length, col_count):
    decriphered = ""
    for x in range(int(col_count)):
            for index in key:
                decriphered += encrypted[int(x) + (int(index) * int(col_length))]
    print("Guessing: " + decriphered)
    return decriphered

def decipherDouble(encrypted, words, filename, alphabet):
    results = []
    first = decipher(encrypted, words, filename, alphabet)
    for cipher in first:
        temp = decipher(cipher.sentence, words, filename, alphabet)
        for wordObject in temp:
            wordObject.sentence = "Final Sentence: " + wordObject.sentence + "First Sentence: " + cipher.sentence
            wordObject.password =  "Final Password: " + wordObject.password + "First Password: " + cipher.password
            results.append(wordObject)
        results.sort(key=lambda x: x.counter, reverse=True)
        results = results[:25]
