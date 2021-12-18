class WordPowerObject:



    def __init__(self, sentence, shift, password, words):
        self.sentence = sentence
        self.shift = shift
        self.counter = 0
        self.password = password
        for word in words:
            if len(word) >= 2:
                if word in self.sentence:
                    self.counter += 1


    def printToFile(self, file, includePassword, includeShift):
        output = "Sentence: " + self.sentence + " Strength: " + str(self.counter)
        if includePassword:
            output += " Password: " + str(self.password)
        if includeShift:
            output += " Shift: " + str(self.shift)
        output += "\n"
        file.write(output)