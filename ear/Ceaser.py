from ear import WordPower


def decipher(encrypted, words,filename, alphabet):

    res = []
    for shift in range(1,26,1):
        dict = getDict(alphabet,shift)
        decrypted = decrypt(encrypted,dict)
        temp = WordPower.WordPowerObject(sentence=decrypted, shift=shift, password=None, words= words)
        res.append(temp)
    res.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for result in res:
        print(result.sentence)
    res = res[0:25]
    for sentece in res:
        sentece.printToFile(file1,includePassword=False,includeShift=True)
    file1.close()

    return res


def decrypt(encrypted, dictionary):
    deciphered = ""
    for char in encrypted:
        deciphered += dictionary[char]
    return deciphered

def getDict(alphabet, shift):
    dict = {}
    for y in range(0, 26, 1):
        dict[alphabet[(y + shift) % 26]] = alphabet[y]
    return dict