from functools import reduce
from math import sqrt
import WordPower
from itertools import permutations

class Table:
    table = []
    height = 0
    width = 0
    mode = ""
    def __init__(self, height, width, content, mode):
        self.height = height
        self.width = width
        self.mode = mode
        if mode == "V":
            for y in range(0, int(height),1):
                self.table.append([])
                for x in range(0,int(width),1):
                    self.table[y].append(content[y*int(width)+x])
        else:
            for x in range(0,int(width),1):
                self.table.append([])
                for y in range(0,int(height),1):
                    self.table[x].append(content[x*int(height)+y])

    def readPassword(self, columnOrder):
        result = ""
        for x in range(0, int(self.width), 1):
            for y in list(columnOrder):
                letter = self.table[int(y)][int(x)]
                result+=letter
        return result

    def read(self):
        result = ""
        var = 0
        if self.mode == "V":
            for x in range(0, int(self.width), 1):
                self.table.append([])
                for y in range(0, int(self.height), 1):
                    result += self.table[y][x]
        else:
            for y in range(0, int(self.height), 1):
                self.table.append([])
                for x in range(0, int(self.width), 1):
                    result += self.table[y][x]
        return result


class Pair:
    a = None
    b = None
    def __init__(self, a, b):
        self.a = a
        self.b = b


def decrypt(words,table):
    results = []
    height = table.height
    if height <= 7:
        p = ""
        for x in range(0,int(height),1):
            p+=str(x)

        passwords = [''.join(p) for p in permutations(p)]
        for password in passwords:
            results.append(WordPower.WordPowerObject(sentence=table.readPassword(list(password)), password= str(table.height) + " x " + str(table.width) + ": " + password, words=words,shift=None))
    return results

def decryptDouble(encrypted, words, table):
    height = table.height
    passwords = []
    for word in words:
        if len(word) == int(height):
            pairs
            passwords.append(word)
    p = ""
    for x in range(0, int(height), 1):
        p += str(x)

    passwords = [''.join(p) for p in permutations(p)]
    for password in passwords:
        results.append(WordPower.WordPowerObject(sentence=table.readPassword(list(password)),
                                                 password=str(table.height) + " x " + str(
                                                     table.width) + ": " + password, words=words, shift=None))
    return results
def decipherDouble(encrypted, words, filename):
    tables = createTables(encrypted)

def decipherPassword(encrypted, words, filename):
    tables = createTables(encrypted)
    results = []
    for table in tables:
        results.extend(decrypt(words=words,table=table))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for word in results:
        word.printToFile(file1, includePassword=True, includeShift=False)
    file1.close()
    return results
def decipher(encrypted, words, filename):
    tables = createTables(encrypted)
    results = []
    for table in tables:
        results.append(WordPower.WordPowerObject(sentence=table.read(), words=words, shift=None, password=str(table.width) + " x " + str(table.height)))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for word in results:
        word.printToFile(file1, includePassword=True, includeShift=False)
    file1.close()
    return results

def createTables(encrypted):
    p = len(encrypted)
    factorials = factors(p)
    factorials.remove(1)
    factorials.remove(p)
    deviders = []
    for factorial in factorials:
        b = p/factorial
        if b in factorials:
            deviders.append(Pair(factorial,b))

    tables = []
    for devider in deviders:
        tables.append(Table(devider.a,devider.b,encrypted,"H"))
        tables.append(Table(devider.a,devider.b,encrypted,"V"))
    return tables


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))