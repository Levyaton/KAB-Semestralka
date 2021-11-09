import WordPower
import MonoalphabeticPass



def toAlphabet(encrypted, alphabet):
    formatted = encrypted.replace(" ","")
    result = ""
    for x in range(0, int(len(formatted)/2),1):
        segment = ""
        segment += formatted[2*x] + formatted[2*x+1]
        letter = alphabet[int(segment)%26]
        result += letter
    return result

def decipher(encrypted,words,filename,alphabet):
    results = []
    for word in words:
        dict = MonoalphabeticPass.getAlphabetDict(word, alphabet)
        alphabet = list(dict.keys())
        for x in range(0, 26, 1):
            temp = WordPower.WordPowerObject(password=word, shift=x,sentence=decrypt(toAlphabet(encrypted, alphabet[x:] + alphabet[:x]), word), words=words)
            if temp.counter > 1:
                results.append(temp)
            print("Sentence: " + temp.sentence + " Strength: " + str(temp.counter))
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    results = results[0:25]
    for word in results:
        word.printToFile(file1,includePassword=True,includeShift=False)
    file1.close()
    return results


def decrypt(encrypted, password, alphabet):
    dict = MonoalphabeticPass.getAlphabetDict(password, alphabet)
    decrypted = ""
    for char in encrypted:
        decrypted += dict[char]
    return decrypted
