from WordPower import  WordPowerObject
def decipher(words, encrypted):
    code = encrypted  # asking for the input of the code
    string_lenght = len(code)  # identifying the lenght of the code to decode
    i = 0  # setting initial character selection to 0
    a = 2
    mod = int(26)  # setting mod to 26
    results = []
    while a < mod:
        b = 0
        a1 = 1
        temp_a = a  # preserving value of a and for verifying GCD=1
        temp_mod = mod  # preserving value of mod
        while temp_mod != 0:  # exit by calculating GCD
            temp_a %= temp_mod  # finding mod of temp_a by temp_mod
            (temp_a, temp_mod) = (temp_mod, temp_a)  # exchanging values of temp_mod and temp_a
        if (temp_a == 1):  # moving forward only if the value of a is valid
            while a1 * a % mod != 1:  # break when the value of 1/a is found
                a1 += 1  # trying every possible multiple so moving to the next int
            while b < mod:
                i = 0
                string = ""
                while i < string_lenght:  # loop that ends when all the characters are decoded
                    character = code[i]  # selecting the character to decrypt
                    y = ord(character) - 97  # converting character to number
                    x = (a1 * (y - b)) % mod  # decrypting
                    answer = chr(x + 97)
                    string += answer
                      # printing the decrypted code
                    i += 1  # Moving to the next character
                word = WordPowerObject(sentence=string, words=words, shift=None,
                                       password="A = " + str(a) + " B = " + str(b))  # converting back to character
                results.append(word)
                b += 1
        a += 1
    results.sort(key=lambda x: x.counter, reverse=True)
    return results