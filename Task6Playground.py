class Object:
    frequency = 0
    number = 0
    def __init__(self,number, frequency):
        self.number = number
        self.frequency = frequency

def base26(string):
    temp = string.split()
    numbers = []
    for word in temp:
        numbers.append(int(word)%26)
    return numbers

def analyzeFrequencies(numbers):
    unique = []
    result = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    for number in unique:
        result.append(Object(number,numbers.count(number)/len(numbers)))
    return result

def convertToAlphabet(numbers):
    dict = getDict(shift=0)
    result = ""
    for number in numbers:
        result += dict[number]
    return result



def getDict(shift):
    dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in range(0, 26, 1):
        dict[x] = alphabet[(x+shift)%26]
    return dict