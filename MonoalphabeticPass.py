import WordPower

def encrypt(decrypted, password):
    dict = getAlphabetDict(password)
    encrypted = ""
    for char in decrypted:
        encrypted += [k for k, v in dict.items() if v == char][0]
    return encrypted
def decipher(encrypted,words,filename):
    results = []
    for word in words:
        temp = WordPower.WordPowerObject(password=word, shift=None, sentence=decrypt(encrypted,word), words=words)
        if temp.counter > 1:
            results.append(temp)
        print("Sentence: " + temp.sentence + " Strength: " + str(temp.counter))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for word in results:
        word.printToFile(file1,includePassword=True,includeShift=False)
    file1.close()
    return results


def decrypt(encrypted, password):
    dict = getAlphabetDict(password)
    decrypted = ""
    for char in encrypted:
        decrypted += dict[char]
    return decrypted
def getAlphabetDict(password):
    dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlph = alphabet
    counter = 0
    for char in password:
        if char not in dict.keys():
            dict[char] = alphabet[counter]
            counter += 1

    for char in newAlph:
        if char in password:
            newAlph = newAlph.replace(char, "")

    for char in newAlph:
        dict[char] = alphabet[counter]
        counter += 1

    return dict
