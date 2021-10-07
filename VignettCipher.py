import WordPower
alphabetMatrix = {
    "a":"abcdefghijklmnopqrstuvwxyz",
    "b":"bcdefghijklmnopqrstuvwxyza",
    "c":"cdefghijklmnopqrstuvwxyzab",
    "d":"defghijklmnopqrstuvwxyzabc",
    "e":"efghijklmnopqrstuvwxyzabcd",
    "f":"fghijklmnopqrstuvwxyzabcde",
    "g":"ghijklmnopqrstuvwxyzabcdef",
    "h":"hijklmnopqrstuvwxyzabcdefg",
    "i":"ijklmnopqrstuvwxyzabcdefgh",
    "j":"jklmnopqrstuvwxyzabcdefghi",
    "k":"klmnopqrstuvwxyzabcdefghij",
    "l":"lmnopqrstuvwxyzabcdefghijk",
    "m":"mnopqrstuvwxyzabcdefghijkl",
    "n":"nopqrstuvwxyzabcdefghijklm",
    "o":"opqrstuvwxyzabcdefghijklmn",
    "p":"pqrstuvwxyzabcdefghijklmno",
    "q":"qrstuvwxyzabcdefghijklmnop",
    "r":"rstuvwxyzabcdefghijklmnopq",
    "s":"stuvwxyzabcdefghijklmnopqr",
    "t":"tuvwxyzabcdefghijklmnopqrs",
    "u":"uvwxyzabcdefghijklmnopqrst",
    "v":"vwxyzabcdefghijklmnopqrstu",
    "w":"wxyzabcdefghijklmnopqrstuv",
    "x":"xyzabcdefghijklmnopqrstuvw",
    "y":"yzabcdefghijklmnopqrstuvwx",
    "z":"zabcdefghijklmnopqrstuvwxy",
}


def getDictionaries(password):
    dictionaries = []
    primeAlphabet = alphabetMatrix["a"]
    for char in password:
        shiftedAlphabet = alphabetMatrix[char]
        dictionary = {}
        for x in range(0,len(primeAlphabet),1):
            dictionary[shiftedAlphabet[x]]=primeAlphabet[x]
        dictionaries.append(dictionary)
    return dictionaries

def decipher(encrypted, words, filename):
    results = []
    for password in words:
        dictionaries = getDictionaries(password)
        decrypted = decrypt(dictionaries,encrypted,password)
        print(decrypted)
        results.append(WordPower.WordPowerObject(sentence=decrypted,shift=None,password=password,words=words))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for word in results:
        word.printToFile(file1, includePassword=True, includeShift=False)
    file1.close()
    return results

def decrypt(dictionaries, encrypted, password):
    decrypted = ""
    passLen = len(password)
    for x in range(0, len(encrypted), 1):
        encryptedLetter = encrypted[x]
        passwordRow = dictionaries[x%passLen]["a"]
        decryptedLetter =  dictionaries[x%passLen][encryptedLetter]
        decrypted+= decryptedLetter

    return decrypted


