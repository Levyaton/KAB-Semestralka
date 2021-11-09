import WordPower

def encrypt(decrypted, password, alphabet):
    dict = getAlphabetDict(password, alphabet)
    encrypted = ""
    for char in decrypted:
        encrypted += [k for k, v in dict.items() if v == char][0]
    return encrypted
def decipher(encrypted,words,filename, alphabet):
    results = []
    for word in words:
        temp = WordPower.WordPowerObject(password=word, shift=None, sentence=decrypt(encrypted,word,alphabet), words=words)
        if temp.counter > 1:
            results.append(temp)
        print("Sentence: " + temp.sentence + " Strength: " + str(temp.counter))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for word in results:
        word.printToFile(file1,includePassword=True,includeShift=False)
    file1.close()
    return results


def decrypt(encrypted, password,alphabet):
    dict = getAlphabetDict(password,alphabet)
    decrypted = ""
    for char in encrypted:
        decrypted += dict[char]
    return decrypted
def getAlphabetDict(password, alphabet):
    dict = {}

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
