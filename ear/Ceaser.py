from ear import WordPower


def decipher(encrypted, words,filename, alphabet):

    res = []
    for shift in range(1,26,1):
        dict = getDict(alphabet,shift)
        decrypted = decrypt(encrypted,dict)
        temp = WordPower.WordPowerObject(sentence=decrypted, shift=shift, password=None, words= words)
        res.append(temp)
    return res

def crack(encrypted, shift, alphabet):
    dict = getDict(alphabet,shift)
    return decrypt(encrypted,dict)

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