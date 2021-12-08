from ear import Ceaser, MonoalphabeticSubstitution, VignettCipher, AffineCipher, ColumnTransposition, MonoalphabeticPass, NewColumnTransposition

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Task1 is an Affine Cipher cipher. The Keys are A = 3, B = 18 and the code is svybehknqpwzcfiojruxatgdml, where the A coefficient is 3 and the B coefficient is 18. I used the class AffineCipher with the method decipher to decrypt the text (the code is based on the one found at the following website, but slightly modefied: https://replit.com/@mx-raza/Brute-force-Affine-cypher. The text is hehadtolookstraightinfrontofhimobriencameinyouaskedmeoncehesaidwhatwasinroomisaidthatyouknewtheansweralready
task1 = "NENSBXIZIIWUXRSQKNXQFHRIFXIHNQCIVRQEFYSCEQFMIASUWEBCEIFYENEUSQBGNSXGSUQFRIICQUSQBXNSXMIAWFEGXNESFUGERSZRESBM"

# Task2 is a monoalphabetic password cipher. The password was bowling. The deciphered text is heputitdownonthetablenearthedoortheworstthingintheworldsaidobrienisdifferentforeachpersonitmaybedeathbyfireorbywaterorfiftyotherdeathssometimesitissomethingquitesmallthatdoesnotevenkillyouhehadmovedtoonesideandwinstoncouldnowseewhatwasonthetable
task2 = "AIMTSCSLKVJKJSAISBOFIJIBQSAILKKQSAIVKQRSSACJGCJSAIVKQFLRBCLKOQCIJCRLCNNIQIJSNKQIBWAMIQRKJCSHBYOILIBSAOYNCQIKQOYVBSIQKQNCNSYKSAIQLIBSARRKHISCHIRCSCRRKHISACJGPTCSIRHBFFSABSLKIRJKSIUIJECFFYKTAIABLHKUILSKKJIRCLIBJLVCJRSKJWKTFLJKVRIIVABSVBRKJSAISBOFI"

# Task3 is a Vignere cipher. I used this class I used was VignettCipher with the method decipher. The password was armenian. The deciphered text is winston had been afraid before but suddenly he understood what the tube was for he felt very very sick you cant do that he screamed obrien what do you want me to do pain alone said obrien quietly is not always enough the rathe continued like a teacher giving a lesson eats meat in the poor parts of the town a mother cannot leave her baby outside because in ten minutes there will only be bones left
task3 = "WZZWGWNUAUNIRVASRRUHOMFBRVNYGAUQDVZPLPEHNUQVFBOBDNTEGBHRTLNIJISSOITISMLGVVDCIMRLSZOOLWUPAEFHBBHNTYQWPZENMVPSOZIRNNTEGLOLOLIEABMRTFPSCIIAACARRAAVDFNVVMNDUZQXYGIFNFFEYEALSVZSHOHGHVDEGPEPOEFMACEQLZWINBENCYQVTQVVNXMPRASBNVMXFUENTZZXUMPBOIBEEBSBFKTIGWWAADAXUMRPAEZSGTENVVTIEJAOYFGXFQDRBVOEHAEVNKQRZQNHTVEXUMRRWZXPBVLLBVNSAMSYEWF"

# Task4 is a Column Transposition Cipher. The column order is 03241 and the class I used is ColumnTransposition with the method decipherPassword. The Decrypted text is sometimes they attack the eyes first sometimes they eat through the face into the tongue one end of the tube was put over his face he could see the first rat its face its teeth xxx.
task4 = "SIHTHSTTTAOHETNNOTAOIEUEIAFTTTTTTESESERTCOOODEWTHCOEFRSIEXMEYCEIOMETGFNEUETBPEFEDHSICTXOMEAEFSIHTUEIHGEFUSVSHLTRTASHESAKYRMEYHHATTENHEURACSETTEEX"

# Task5 is a Table Cipher with a size of 2x143. I used the class ColumnTransposition with the method decipher to decrypt it. The deciphered text is: juliaidontcarewhatyoudotoherdestroyherfaceleaveonlybonesnotmejulianotmeheheardobrientouchtheswitchandknewhehadclosedthedoortothetubenotopeneditthechestnuttreecafewasalmostemptyitwasthelonelytimeoffifteenhoursmusiccamefromthetelescreensnowbutwinstonwaslisteningfornewsofthewarxxxxxxxxxxx
task5 = "JTUHLEICAHIEDSOTNNTUCTATRREEWEHCAATFYEOWUADSOATLOMHOESRTDEEMSPTTRYOIYTHWEARSFTAHCEELLOENAEVLEYOTNILMYEBOOFNFEISFNTOETEMNEHJOUULRISAMNUOSTIMCECHAEMHEEFARRODMOTBHREITEENLTEOSUCCRHETEHNESSNWOIWTBCUHTAWNIDNKSNTEOWNHWEAHSALDICSLTOESNEIDNTGHFEODRONOERWTSOOTFHTEHTEUWBAERNXOXTXOXPXEXNXEXDXIXTX"

task6 = "05158764 66149595 40886493 " \
        "24319962 68162102 68480515 " \
        "43690900 53185321 21006618 " \
        "24349505 59270054 06788263 " \
        "33330648 22722272 07599406 " \
        "55661130 07069828 00180369 " \
        "53916978 04117024 67590900 " \
        "34901631 72903533 30907490 " \
        "44197415 00521430 21467556 " \
        "28573994 58073996 44600538 " \
        "00062247 42313260 48240714 " \
        "40893959 08377882 35502406 " \
        "41737641 35153692 71748792 " \
        "06491571 29662349 47123030 " \
        "40887522 42208553 69116239 " \
        "05461703 53996157 02178744 " \
        "24601716 06491571 25920814 " \
        "72623601 27236240 40682348 " \
        "08116576 69051754 43179942 " \
        "34096568 15050293 46964035 " \
        "51291235 42313260 70112055 " \
        "14242528 62143639 12646994 " \
        "45603571 36827528 06389789 " \
        "20439896 39812537 07423870 " \
        "14164187 41708602 34997021 " \
        "67287262 26227233 50093231 " \
        "09817160 29574294 24527110 " \
        "24125072 18295526 70992540 " \
        "02770816 65722590 04406687 " \
        "54380052 11620641 28680574 " \
        "06399380 63168173 63057009 " \
        "49443865 26164425 09269194 " \
        "63123695 60277199 39100574 " \
        "61368983 17106356 17647995 " \
        "46690787 44981935 39646461 " \
        "63922128 00960334 47828352 " \
        "58193613 28385026 49446434 " \
        "36571402 33347854 03148371 " \
        "46921086 26499037 55481537 " \
        "42360193 22625545 18314108 " \
        "42624946 21784033 44055218 "
#Ceaser? (Monoalphabetic Shift) + Table Column (Password) transposition)
task7 = "FIFVVRKKUNYKKKYFRIRRDVLKJYUVVEPLCXYEUJYUNIUSVLVLYUUYAZZVVYYVESJUEVYJYYRYVKKTKWIVKERRZRRFVPCFVRURRKVVUVELYPRPYVYZFZUKEKWN"

# Task 8 is a ceaser shift cipher, enciphered in a double column transposition cipher. I used the method decryptDoubleNoPassword from the file ColumnTransposition.py, to get my first list, then ran the decripher method from the file Ceaser.py on each element, and stored the results. The deciphered messege is: helovedbigbrotherthefirsttimeisawterrylennoxhewassittinginarollsroyceinfrontofafancyrestaurantandhewasverydrunknnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn. Table 1 has dimentions 48 x 3.0 and Table 2 has dimentions 2 x 72.0. The Ceaser shift is 10
task8 = "RYYYNPQMYOOKRKSKDRWKCODNBXOXYXOXCXDXXXXXYXCXIXSXBVDOKSXBBRDDBPDCNSGSFGIBEVXXXRXKXSXSXSXBXVXYXOXPOXFPLKLIDCBEOXBXDOOCKBOBIUXXHXGXCXDXQXKXVXBXMXXX"

#Affine + Complete table with no cipher
#Task 9 is an affine cipher, enciphered in a simple table cipher. I used the method affineWithTable and the deciphered message is: herhairwasaprettydarkredandshehadadistantsmileonherlipsihaveawonderfulideadarlingthewomansaidtryingtobenicewhydontwetakeataxitoyourplaceandgetyourlittlecaroutiiiiiiiiii, A = 21, B = 11. The table size is 14x12
task9 = "CELZCLRFXCLIPPRRYURFLTYVULEUEUWLETWDHWLBIXCUZYIYLLUTARXXLVCUXWEYTYXLUXXWRZORIZGUUYUXELCDZEXLRFTWIXFELXXMYXYRVHRXLNWICPHWXUTRBXZELRLIUUBLPULXLRWTKXCERNEVEXOWXYRWRVFROTTX"
alphabeticTasks = [task1, task2, task3, task4, task5, task7, task8, task9]


def getWords(filepath):
    # with open('english-words.txt') as f:
    with open(filepath) as f:
        return f.read().split()


def getWordsDefualt():
    # with open('english-words.txt') as f:
    with open('english-words.txt') as f:
        return f.read().split()


def ceaserDoubleTransposition(task, filename, words):
    return combineTwoMethods(Ceaser.decipher, ColumnTransposition.decipherDouble, filename=filename, words=words,
                             task=task, origin="ceaserDoubleTransposition")


def ceaserWithPasswordSubstitution(task, filename, words):
    return combineTwoMethods(Ceaser.decipher, MonoalphabeticPass.decipher, filename=filename, words=words, task=task,
                             origin="ceaserWithPasswordSubstitution")


def ceaserWithVignett(task, filename, words):
    return combineTwoMethods(Ceaser.decipher, VignettCipher.decipher, filename=filename, words=words, task=task,
                             origin="ceaserWithVignett")


def ceaserWithTable(task, filename, words):
    return combineTwoMethods(Ceaser.decipher, ColumnTransposition.decipher, filename=filename, words=words, task=task,
                             origin="ceaserWithTable")


def ceaserWithPasswordTransposition(task, filename, words):
    return combineTwoMethods(Ceaser.decipher, ColumnTransposition.decipherPassword, filename=filename, words=words,
                             task=task, origin="ceaserWithPasswordTransposition")


def passwordSubstitutionWithVignett(filename, words, task):
    return combineTwoMethods(MonoalphabeticPass.decipher, VignettCipher.decipher, filename=filename, words=words,
                             task=task, origin="passwordSubstitutionWithVignett")


def passwordSubstitutionWithColumnTransposition(filename, words, task):
    return combineTwoMethods(MonoalphabeticPass.decipher, ColumnTransposition.decipherPassword, filename=filename,
                             words=words,
                             task=task, origin="passwordSubstitutionWithColumnTransposition")


def passwordSubstitutionWithTable(filename, words, task):
    return combineTwoMethods(MonoalphabeticPass.decipher, ColumnTransposition.decipher, filename=filename, words=words,
                             task=task, origin="passwordSubstitutionWithTable")


def passwordSubstitutionWithDoubleTransposition(filename, words, task):
    return combineTwoMethods(MonoalphabeticPass.decipher, ColumnTransposition.decipherDouble, filename=filename,
                             words=words,
                             task=task, origin="passwordSubstitutionWithTable")


def passwordSubstitutionTableCipher(filename, words, task):
    return combineTwoMethods(MonoalphabeticPass.decipher, ColumnTransposition.decipher, filename=filename, words=words,
                             task=task, origin="passwordSubstitutionTableCipher")


def affinWithPasswordTransposition(filename, words, task):
    return combineTwoMethods(AffineCipher.decipher, ColumnTransposition.decipherPassword, filename=filename,
                             words=words, task=task, origin="affinWithPasswordTransposition")


def affineWithVignere(task, words, filename):
    return combineTwoMethods(AffineCipher.decipher, VignettCipher.decipher, filename=filename, words=words, task=task,
                             origin="affineWithVignere")


def affineWithPasswordSubstitution(filename, words, task):
    combineTwoMethods(AffineCipher.decipher, MonoalphabeticPass.decipher, filename=filename, words=words, task=task,
                      origin="affineWithPasswordSubstitution")


def affineWithColumnTransposition(filename, words, task):
    return combineTwoMethods(AffineCipher.decipher, ColumnTransposition.decipherPassword, filename=filename,
                             words=words, task=task, origin="affineWithColumnTransposition")


def affineWithTable(filename, words, task):
    return combineTwoMethods(AffineCipher.decipher, ColumnTransposition.decipher, filename=filename, words=words,
                             task=task, origin="affineWithTable")


def affineWithDoubleTransposition(filename, words, task):
    return combineTwoMethods(ColumnTransposition.decipherDouble, AffineCipher.decipher,filename=filename, words=words,
                             task=task, origin="affineWithDoubleTransposition")


def affineWithCeaser(filename, words, task):
    return combineTwoMethods(AffineCipher.decipher, Ceaser.decipher, filename=filename, words=words, task=task,
                             origin="affineWithCeaser")


def vignettWithTable(filename, words, task):
    return combineTwoMethods(VignettCipher.decipher, ColumnTransposition.decipher, filename=filename, words=words,
                             task=task, origin="vignettWithTable")


def vignettWithColumnTransposition(filename, words, task):
    return combineTwoMethods(VignettCipher.decipher, ColumnTransposition.decipherPassword, filename=filename,
                             words=words,
                             task=task, origin="vignettWithColumnTransposition")


def vignettWithDoubleTransposition(filename, words, task):
    return combineTwoMethods(VignettCipher.decipher, ColumnTransposition.decipherDouble, filename=filename, words=words,
                             task=task, origin="vignettWithDoubleTransposition")


def tableWithColumnTransposition(filename, words, task):
    return combineTwoMethods(ColumnTransposition.decipher, ColumnTransposition.decipherPassword, filename=filename,
                             words=words,
                             task=task, origin="tableWithColumnTransposition")


def tableWithDoubleTransposition(filename, words, task):
    return combineTwoMethods(ColumnTransposition.decipher, ColumnTransposition.decipherDouble, filename=filename,
                             words=words,
                             task=task, origin="tableWithDoubleTransposition")


def columnTranspositionWithDoubleTransposition(filename, words, task):
    return combineTwoMethods(ColumnTransposition.decipherPassword, ColumnTransposition.decipherDouble,
                             filename=filename,
                             words=words,
                             task=task, origin="columnTranspositionWithDoubleTransposition")


def storeInFile(filename, results):
    results.sort(key=lambda x: x.counter, reverse=True)
    file1 = open(filename, "w")
    results = results[0:25]
    for sentece in results:
        sentece.printToFile(file1, includePassword=True, includeShift=True)
    file1.close()
    return results


def combineTwoMethods(decipher1, decipher2, filename, words, task, origin):
    p1 = decipher1(encrypted=task, words=words, filename=filename, alphabet=alphabet)
    counter = 0
    results = []
    for element in p1:
        counter += 1
        print("Part 1: " + str(counter) + "/" + str(len(p1)))
        p2 = decipher2(words=words, encrypted=element.sentence, filename=filename, alphabet=alphabet)
        for el in p2:
            password = " Origin: " + origin
            if element.shift is not None:
                if el.shift is not None:
                    el.shift += element.shift
                else:
                    el.shift = element.shift
            if element.password is not None:
                password = element.password + password
            if el.password is not None:
                password += el.password + password
            el.password = password
        results.extend(p2)
        results.sort(key=lambda x: x.counter, reverse=True)
        if(len(results) > 0):
            print("Best guess: " + results[0].sentence)
    storeInFile(filename, results)
    return results



def bruteForceAllMethods(path, filename, suffix, task, words):
#The following are probably a waist of time:
#ceaserDoubleTransposition, ceaserWithPasswordSubstitution, ceaserWithVignett, ceaserWithTable,
         #      ceaserWithPasswordTransposition, passwordSubstitutionWithVignett,passwordSubstitutionWithColumnTransposition,
             #passwordSubstitutionWithTable,
               #passwordSubstitutionWithDoubleTransposition,


    methods = [
        ceaserDoubleTransposition, ceaserWithPasswordSubstitution, ceaserWithVignett, ceaserWithTable,
               ceaserWithPasswordTransposition, passwordSubstitutionWithVignett,passwordSubstitutionWithColumnTransposition,
             passwordSubstitutionWithTable,
               passwordSubstitutionWithDoubleTransposition,
                passwordSubstitutionTableCipher,
               affinWithPasswordTransposition,
               affineWithVignere, affineWithPasswordSubstitution,
               affineWithColumnTransposition,
               affineWithTable, affineWithDoubleTransposition, affineWithCeaser, vignettWithTable,
               vignettWithColumnTransposition,
               vignettWithDoubleTransposition, tableWithColumnTransposition, tableWithDoubleTransposition,
               columnTranspositionWithDoubleTransposition]

    results = []
    counter = 0
    for method in methods:
        counter+=1
        print("Step "+ str(counter) + " out of " + str(len(methods)))
        result = method(filename=path + "Step" + str(counter) + suffix, task=task, words=words)
        results.extend(result)
        results.sort(key=lambda x: x.counter, reverse=True)
        if len(results) > 1:
            print("Best Guess:  " + results[0].sentence + " With Password: " + results[0].password)
        storeInFile(filename=path + filename + suffix,results=results)





if __name__ == '__main__':
    path = "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ear\\"
    suffix = ".txt"
    filename = "testTask3"
    words = getWords(path+"10k-english.txt")
    task = task7
    #MonoalphabeticSubstitution.decipher("Tasisimjcmiwlokngch".upper(),words,None,alphabet=alphabet)

    #storeInFile(path+filename+suffix, ColumnTransposition.decipherPassword("TINESAXEOAHTFXHTLTHEYMAIIAIXTAPNGDLOSTNHMX".lower(),words,path+filename+suffix,alphabet))
    #results = combineTwoMethods(ColumnTransposition.decipherPassword,MonoalphabeticSubstitution.decipher,path+filename+suffix,words,task7.lower(),"columnTranspositionWithMonoalphabeticSubstitution")
    #results.extend(combineTwoMethods(MonoalphabeticSubstitution.decipher,ColumnTransposition.decipherPassword,path+filename+suffix,words,task7.lower(),"columnTranspositionWithMonoalphabeticSubstitution"))

    ceaserWithPasswordTransposition(task.lower(),path+filename+suffix,words)
    #results = ColumnTransposition.decipher(task5.lower(),words,path+filename+suffix,alphabet)
   # storeInFile(path+filename+suffix,results)
    #combineTwoMethods(MonoalphabeticSubstitution.decipher, ColumnTransposition.decipherDouble, path + filename + suffix, words, task.lower(), origin="columnTranspositionWithMonoalphabeticSubstitution")

   # result = passwordSubstitutionWithColumnTransposition(task=task, words=words,filename=path+filename+suffix)
    #storeInFile(path+filename+suffix,result)
    #Task6Playground.factorialsAnalysis(task)
    #task = Task6Playground.eightIsOneLetterToAlphabetConversion(task,alphabet,words)
    #result = MonoalphabeticPass.decipher(task,words,path+filename+suffix,alphabet)
    #print(task)
    #ceasers = Ceaser.decipher(task,words,path+filename+suffix,alphabet)
    #result = []
    #for ceaser in ceasers:
    #result.extend(VignettCipher.decipher(task,words,path+filename+suffix,alphabet))
    #result.extend(AffineCipher.decipher(task, words, path + filename + suffix, alphabet))
    #storeInFile(path+filename+suffix,result)
    #VignettCipher.decipher(encrypted=task, words=words,filename=path+filename+suffix,alphabet=alphabet)

    # affineWithVignere(task, words, filename)

    # result = []
    # filename = "C:\\Users\\Levyaton\\PycharmProjects\\KAB-Semestralka\\test.txt"
    # for task in alphabeticTasks:
    #        result.extend(VignettCipher.decipher(task.lower(), getWords(
    #                "C:\\Users\\Levyaton\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),
    #                                      filename=filename))
    # result.sort(key=lambda x: x.counter, reverse=True)
    # file1 = open(filename, "w")
    # for sentece in results:
    #        sentece.printToFile(file1, includePassword=True, includeShift=True)
    # file1.close()
