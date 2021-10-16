class WordPowerObject:

    sentence = ""
    counter = 0
    shift = None
    password = ""

    def __init__(self, sentence, shift, password, words):
        self.sentence = sentence
        self.shift = shift
        self.password = password
        for word in words:
            if len(word) >= 3:
                if word in self.sentence:
                    self.counter += 1


    def printToFile(self, file, includePassword, includeShift):
        output = "Sentence: " + self.sentence + " Strength: " + str(self.counter)
        if includePassword:
            output += " Password: " + self.password
        if includeShift:
            output += " Shift: " + str(self.shift)
        output += "\n"
        file.write(output)