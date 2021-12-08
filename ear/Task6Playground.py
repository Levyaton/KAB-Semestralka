from functools import reduce
from math import sqrt
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def factorialsAnalysis(task):
    fact = []
    temp = 0
    for foursome in task:
        for member in foursome:
            temp += int(member)
        fact.append(factors(temp))
    gcd = fact[0]

    for factor in fact:
        gcd = list(filter(lambda x: x not in gcd, factor))
    return fact

def getAddition(cipherArray):
    fact = []
    temp = 0
    for foursome in cipherArray:
        for member in foursome:
            temp += int(member)
        fact.append(temp)
    return fact
def getFactors(cipherArray):
    fact = []
    temp = 0
    for foursome in cipherArray:
        for member in foursome:
            temp += int(member)
        fact.append(factors(temp))
    return fact

def gcdOfFoursomeConversion(cipherArray):
    cipher = []
    add = getAddition(cipherArray)
    fact = getFactors(cipherArray)
    for x in range(0,len(fact),1):
        l = list(fact[x])
        l.sort()
        cipher.append((add[x]/l[0]) % 26)
    return cipher
def multiplicationConversion(cipherArray):
    cipher = []
    for foursome in cipherArray:
        multiplication = 1
        for num in foursome:
            multiplication = multiplication * num
        cipher.append(multiplication % 26)
    return cipher
def additionConversion(cipherArray):
    cipher = []
    for foursome in cipherArray:
        addition = 0
        for num in foursome:
            addition += num
        cipher.append(addition % 26)
    return cipher

def prepareTwoForOne(task):
    encrypted = task.replace(" ", "")
    groupsOfFour = []

    for x in range(0, len(encrypted), 8):
        temp = []
        for y in range(0, 8, 2):
            num = int(encrypted[x + y] + encrypted[x + y + 1])
            temp.append(num)
        groupsOfFour.append(temp)
    return groupsOfFour
def prepareOneForOne(task):
    encrypted = task.replace(" ", "")
    groupsOfEight = []

    for x in range(0, len(encrypted), 8):
        temp = []
        for y in range(0, 8, 1):
            num = int(encrypted[x + y])
            temp.append(num)
        groupsOfEight.append(temp)
    return groupsOfEight

def combinationConversion(cipherArray):
    cipher = []
    for foursome in cipherArray:
        string = ""
        for num in foursome:
            string += str(num)
        cipher.append(int(string))
    return cipher

def averageConversion(cipherArray):
    cipher = []
    for foursome in cipherArray:
        temp = 0
        for num in foursome:
            temp += num
        cipher.append(temp/4)
    return cipher


def eightIsOneLetterToAlphabetConversion(task, alphabet, dictionary):
    groups = prepareTwoForOne(task)
    cipher = additionConversion(groups) #- This is not the correct formula
    #cipher = multiplicationConversion(groups)# - This is not the correct formula
    #Some of the foursomes contain 0, so a gcd would be impossible to find
    #cipher = gcdOfFoursomeConversion(groups)# - This is not the correct formula
    #cipher = combinationConversion(groups)# - This is not the correct formula
    #cipher = averageConversion(groups)

    string = ""
    for num in cipher:
        string += str(alphabet[int(num)%26])
    print(string)
    return string