class WordPower:

    sentence = ""
    counter = 0
    shift = None
    def __init__(self, sentence, shift):
        self.sentence = sentence
        self.shift = shift

    def increment(self):
        self.counter += 1

def decipher(encrypted, words,filename):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for shift in range(1,26,1):
        dict = getDict(alphabet,shift)
        decrypted = decrypt(encrypted,dict)
        temp = WordPower(decrypted,shift)
        for word in words:
            if word in temp.sentence:
                temp.increment()
        res.append(temp)
    res.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    for sentece in res:
        file1.write(
            "Sentence: " + sentece.sentence + " Strength: " + str(sentece.counter) + " Password: " + sentece.shift + "\n")
    file1.close()


def decrypt(encrypted, dictionary):
    deciphered = ""
    for char in encrypted:
        deciphered += dict[char]
    return deciphered
def getDict(alphabet, shift):
    dict = {}
    for y in range(0, 26, 1):
        dict[(y + shift) % 26] = alphabet[y]
    return dict