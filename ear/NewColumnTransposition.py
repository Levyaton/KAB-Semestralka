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
import threading


def getKey(col_length):
    key = ""
    for x in range(int(col_length)):
        if x < 10 :
            key += "0"
        if x <100:
            key += "0"
        key += str(x)

    return [key[i:i+3] for i in range(0, len(key), 3)]

def keyToList(key):
   return [key[i:i + 3] for i in range(0, len(key), 3)]

def factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]



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
    threads = []
    for factor in f:
        counter += 1
        print(str(counter) + " / " + str(len(f)))
        column_length = length / factor
        thread = threading.Thread(target=breakCipher, args = (factor, column_length, encrypted, words, results))
        thread.start()
        threads.append(thread)
        results.sort(key=lambda x: x.counter, reverse=True)
     #   results = results[:25]
        if (len(results) > 0):
            print("Best Guess: " + results[0].sentence)
    for thread in threads:
        try:
            thread.join()
        except:
            print("woops")
    return results

def simplefyKey(key):
    result = ""
    for x in range(int(len(key)/3)):
        result+=str(int(key[x*3:x*3+3]))
    return result


def cipherThread(key,encrypted, column_length, column_count, password, words, results):
    #r = readColumn(key=key, encrypted=encrypted, col_length=column_length, col_count=column_count)
    #r = readRow(key=key, encrypted=encrypted, col_length=column_length, col_count=column_count)

    r = read(encrypted,keyToList(key))

    results.append(
        WordPower.WordPowerObject(
            sentence=r,
            shift=None, password=password, words=words))

def breakCipher(column_count, column_length, encrypted, words, r):
    results = []
    max = 9
    # Skip checking absurdly long tables, as they would make the program crash, due to memory consumption

    if max > column_count:
        perms = set([''.join(p) for p in permutations(getKey(column_count))])
        threads = []
        coutner = 0
        for p in perms:
            coutner += 1

            print(str(coutner) +"/" +str(len(perms)) +" Testing Key: " + simplefyKey(p))
            thread = threading.Thread(target = cipherThread, args=(p,encrypted,column_length,column_count,simplefyKey(p),words,results))
            thread.start()
            threads.append(thread)
            results.sort(key=lambda x: x.counter, reverse=True)
            results = results[:25]
        for thread in threads:
            try:
                thread.join()
            except:
                print("woops")
        if results is not None:
            r.extend(results)



def decipherTable(encrypted, words, filename, alphabet):
    length = len(encrypted)
    f = factors(length)
    results = []
    for factor in f:
        column_length = length / factor
        print(str(factor) +  " / " + str(column_length))
        results.append(WordPower.WordPowerObject(
            sentence=readColumn(key=getKey(column_length), encrypted=encrypted, col_length=int(column_length)), shift=None,
            password=str(factor) + " x " + str(column_length), words=words))
        results.append(WordPower.WordPowerObject(
            sentence=readRow(key=getKey(column_length), encrypted=encrypted, col_length=int(column_length),col_count=int(factor)), shift=None,
            password=str(factor) + " x " + str(column_length), words=words))
    return results

def readColumn(key, encrypted, col_length, col_count):

    deciphered = ""
    for x in range(int(col_length)):
            for index in keyToList(key):
                deciphered += encrypted[x + (int(index) * int(col_length))]
   # print("Guessing: " + deciphered)
    return deciphered

def read(cipher, key):
    msg = ""

    # track key indices
    k_indx = 0

    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    #key_lst = sorted(list(key))

    # create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg
def readRow(key, encrypted, col_length, col_count):
    deciphered = ""
    for index in keyToList(key):
        for x in range(int(col_length)):
            deciphered+= encrypted[x + (int(index) * int(col_length))]
    return deciphered
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
