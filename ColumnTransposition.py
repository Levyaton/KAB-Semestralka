from functools import reduce
from math import sqrt
import WordPower
from itertools import permutations

class Table:

    def __init__(self, width, height, content):
        self.table = []
        self.height = height
        self.width = width

        for x in range(0,int(height),1):
            self.table.append([])
            for y in range(0,int(width),1):
                self.table[x].append(content[x*int(width)+y])
        a = ""

    def readPassword(self, columnOrder):
        result = ""
        for x in range(0, int(self.width), 1):
            for y in list(columnOrder):
                letter = self.table[int(y)][int(x)]
                result+=letter
        return result
    def readHorizontal(self):
        result = ""
        for x in range(0, int(self.width), 1):
            for y in range(0, int(self.height), 1):
                result += self.table[y][x]
        return result
    def readVertical(self):
        result = ""
        for y in range(0, int(self.height), 1):
            for x in range(0, int(self.width), 1):
                result += self.table[y][x]
        return result

class Pair:
    a = None
    b = None
    def __init__(self, a, b):
        self.a = a
        self.b = b

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
        t1 = Table(devider.a,devider.b,encrypted)
        tables.append(t1)
        #print(t1.readVertical())

        a = ""
    return tables


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))


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





def decryptDoubleNoPassword(encrypted, words):
    tables = createTables(encrypted)
    firstTraspositions = []
    for table in tables:
        firstTraspositions.extend(createTables(table.readVertical()))
        firstTraspositions.extend(createTables(table.readHorizontal()))
    secondTranspositions = []
    for table in firstTraspositions:
        temp = []
        temp.extend(createTables(table.readVertical()))
        temp.extend(createTables(table.readHorizontal()))
        for element in temp:
            element.message = str(table.width) + " x " + str(table.height)
        secondTranspositions.extend(temp)
    results = []
    for table in secondTranspositions:
        password = "Table 1 has dimentions " + str(table.width) + " x " + str(table.height) + "Table 2 has dimentions " + table.message
        results.append(WordPower.WordPowerObject(sentence=table.readVertical(),shift=None,password= password,words=words))
        results.append(
            WordPower.WordPowerObject(sentence=table.readHorizontal(), shift=None, password=password, words=words))
    results.sort(key=lambda x: x.counter, reverse=True)
    print("Decrypted")
    return results

def decipherDouble(encrypted, words, filename):
    noPasswords = decryptDoubleNoPassword(encrypted=encrypted,words=words)
    return noPasswords



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
        results.append(WordPower.WordPowerObject(sentence=table.readVertical(), words=words, shift=None, password=str(table.width) + " x " + str(table.height)))
        results.append(WordPower.WordPowerObject(sentence=table.readHorizontal(), words=words, shift=None,
                                                 password=str(table.width) + " x " + str(table.height)))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for word in results:
        word.printToFile(file1, includePassword=True, includeShift=False)
    file1.close()
    return results


