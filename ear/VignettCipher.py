from ear import WordPower


def getAlphabetMatrix(alphabet):
    matrix = {}
    length = len(alphabet)
    prev = alphabet[length-1] + alphabet[0:length-1]

    for x in range(0,len(alphabet),1):
        char = alphabet[x]
        current =  prev[1:] + prev[0]
        matrix[char] = current
        prev = current
    return matrix


def getDictionaries(password, alphabet):
    dictionaries = []
    matrix = getAlphabetMatrix(alphabet)
    primeAlphabet = matrix["a"]
    for char in password:
        shiftedAlphabet = matrix[char]
        dictionary = {}
        for x in range(0,len(primeAlphabet),1):
            dictionary[shiftedAlphabet[x]]=primeAlphabet[x]
        dictionaries.append(dictionary)
    return dictionaries

def decipher(encrypted, words, filename,alphabet):
    results = []
    for password in words:
        dictionaries = getDictionaries(password,alphabet)
        decrypted = decrypt(dictionaries,encrypted,password)
        print(decrypted)
        results.append(WordPower.WordPowerObject(sentence=decrypted, shift=None, password=password, words=words))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    results = results[0:25]
    for word in results:
        word.printToFile(file1, includePassword=True, includeShift=False)
    file1.close()
    return results

def decrypt(dictionaries, encrypted, password):
    decrypted = ""
    passLen = len(password)
    for x in range(0, len(encrypted), 1):
        encryptedLetter = encrypted[x]
        passwordRow =  dictionaries[x%passLen]
        decryptedLetter =  passwordRow[encryptedLetter]
        decrypted+= decryptedLetter

    return decrypted


