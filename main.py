import MonoalphabeticPass
import VignettCipher
import NumberCipher
import os
import Ceaser
import Task6Playground
import SimpleSubstitutionCipher
import ColumnTransposition
#Task1 is an Affine Cipher cipher. The key is svybehknqpwzcfiojruxatgdml, where the A coefficient is 3 and the B coefficient is 18. I used the website https://www.guballa.de/substitution-solver to decrypt the text. The text is hehadtolookstraightinfrontofhimobriencameinyouaskedmeoncehesaidwhatwasinroomisaidthatyouknewtheansweralready
task1= "NENSBXIZIIWUXRSQKNXQFHRIFXIHNQCIVRQEFYSCEQFMIASUWEBCEIFYENEUSQBGNSXGSUQFRIICQUSQBXNSXMIAWFEGXNESFUGERSZRESBM"

#Task2 is a monoalphabetic password cipher. The password was bowling. The deciphered text is heputitdownonthetablenearthedoortheworstthingintheworldsaidobrienisdifferentforeachpersonitmaybedeathbyfireorbywaterorfiftyotherdeathssometimesitissomethingquitesmallthatdoesnotevenkillyouhehadmovedtoonesideandwinstoncouldnowseewhatwasonthetable
task2= "AIMTSCSLKVJKJSAISBOFIJIBQSAILKKQSAIVKQRSSACJGCJSAIVKQFLRBCLKOQCIJCRLCNNIQIJSNKQIBWAMIQRKJCSHBYOILIBSAOYNCQIKQOYVBSIQKQNCNSYKSAIQLIBSARRKHISCHIRCSCRRKHISACJGPTCSIRHBFFSABSLKIRJKSIUIJECFFYKTAIABLHKUILSKKJIRCLIBJLVCJRSKJWKTFLJKVRIIVABSVBRKJSAISBOFI"

#Task3 is a Vignere cipher. I used the Class VignettCipher to decode it. The password was armenian. The deciphered text is: winstonhadbeenafraidbeforebutsuddenlyheunderstoodwhatthetubewasforhefeltveryverysickyoucantdothathescreamedobrienwhatdoyouwantmetodopainalonesaidobrienquietlyisnotalwaysenoughtherathecontinuedlikeateachergivingalessoneatsmeatinthepoorpartsofthetownamothercannotleaveherbabyoutsidebecauseintenminutestherewillonlybebonesleft
task3 = "WZZWGWNUAUNIRVASRRUHOMFBRVNYGAUQDVZPLPEHNUQVFBOBDNTEGBHRTLNIJISSOITISMLGVVDCIMRLSZOOLWUPAEFHBBHNTYQWPZENMVPSOZIRNNTEGLOLOLIEABMRTFPSCIIAACARRAAVDFNVVMNDUZQXYGIFNFFEYEALSVZSHOHGHVDEGPEPOEFMACEQLZWINBENCYQVTQVVNXMPRASBNVMXFUENTZZXUMPBOIBEEBSBFKTIGWWAADAXUMRPAEZSGTENVVTIEJAOYFGXFQDRBVOEHAEVNKQRZQNHTVEXUMRRWZXPBVLLBVNSAMSYEWF"

#Task4 is a Column Transposition Cipher. The column order is 0,3,2,4,1 and the size is 5x29. I used the class ColumnTransposition with the method decipherPassword to decipher the code. The Decrypted text is sometimes they attack the eyes first sometimes they eat through the face into the tongue one end of the tube was put over his face he could see the first rat its face its teeth xxx.
task4 = "SIHTHSTTTAOHETNNOTAOIEUEIAFTTTTTTESESERTCOOODEWTHCOEFRSIEXMEYCEIOMETGFNEUETBPEFEDHSICTXOMEAEFSIHTUEIHGEFUSVSHLTRTASHESAKYRMEYHHATTENHEURACSETTEEX"

#Task5 is a Table Cipher with a size of 2x143. I used the class ColumnTransposition with the method decipher to decrypt it. The deciphered text is: juliaidontcarewhatyoudotoherdestroyherfaceleaveonlybonesnotmejulianotmeheheardobrientouchtheswitchandknewhehadclosedthedoortothetubenotopeneditthechestnuttreecafewasalmostemptyitwasthelonelytimeoffifteenhoursmusiccamefromthetelescreensnowbutwinstonwaslisteningfornewsofthewarxxxxxxxxxxx
task5 = "JTUHLEICAHIEDSOTNNTUCTATRREEWEHCAATFYEOWUADSOATLOMHOESRTDEEMSPTTRYOIYTHWEARSFTAHCEELLOENAEVLEYOTNILMYEBOOFNFEISFNTOETEMNEHJOUULRISAMNUOSTIMCECHAEMHEEFARRODMOTBHREITEENLTEOSUCCRHETEHNESSNWOIWTBCUHTAWNIDNKSNTEOWNHWEAHSALDICSLTOESNEIDNTGHFEODRONOERWTSOOTFHTEHTEUWBAERNXOXTXOXPXEXNXEXDXIXTX"

#Hypotheses 1: There exists a common denomenator for each of the 8bit numbers - Result: Negative, the highest common denominator amongst the numbers is 1
#Hypotheses 2: Each 8-bit number converts to a number from 0-25 in mod 26, that can then be mapped to a monoalphabetic cipher - Result: It isn't a simple monoalphabetic password cipher, nor is it a monoalphabetic cypher with a shift
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

task7 = "FIFVVRKKUNYKKKYFRIRRDVLKJYUVVEPLCXYEUJYUNIUSVLVLYUUYAZZVVYYVESJUEVYJYYRYVKKTKWIVKERRZRRFVPCFVRURRKVVUVELYPRPYVYZFZUKEKWN"

task8 = "RYYYNPQMYOOKRKSKDRWKCODNBXOXYXOXCXDXXXXXYXCXIXSXBVDOKSXBBRDDBPDCNSGSFGIBEVXXXRXKXSXSXSXBXVXYXOXPOXFPLKLIDCBEOXBXDOOCKBOBIUXXHXGXCXDXQXKXVXBXMXXX"

task9 = "CELZCLRFXCLIPPRRYURFLTYVULEUEUWLETWDHWLBIXCUZYIYLLUTARXXLVCUXWEYTYXLUXXWRZORIZGUUYUXELCDZEXLRFTWIXFELXXMYXYRVHRXLNWICPHWXUTRBXZELRLIUUBLPULXLRWTKXCERNEVEXOWXYRWRVFROTTX"
alphabeticTasks = [task1,task2,task3,task4,task5,task7,task8,task9]

def getWords(filepath):
    #with open('english-words.txt') as f:
    with open(filepath) as f:
        return f.read().split()
def getWordsDefualt():
    #with open('english-words.txt') as f:
    with open('english-words.txt') as f:
        return f.read().split()

if __name__ == '__main__':

        result = []
        #result.extend(ColumnTransposition.decipherPassword(encrypted=task4.lower(), words=getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),filename="C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\task5.txt"))
        result.extend(ColumnTransposition.decipher(encrypted=task5.lower(),words=getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), filename="C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\task5.txt"))
        print("finished Task 5")
        #result.extend(ColumnTransposition.decipherPassword(encrypted=task7.lower(), words=getWords(
        #        "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),
        #                             filename="C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\task7.txt"))
        #print("finished Task 7")
        #result.extend(ColumnTransposition.decipherPassword(encrypted=task8.lower(), words=getWords(
        #        "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),
        #                             filename="C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\task8.txt"))
        #print("finished Task 8")
        #result.extend(ColumnTransposition.decipherPassword(encrypted=task9.lower(), words=getWords(
        #       "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),
        #                           filename="C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\task9.txt"))
        #print("finished Task 9")
        result.sort(key=lambda x: x.counter, reverse=True)
        file1 = open("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\result.txt", "w")
        for word in result:
                word.printToFile(file1, includePassword=True, includeShift=False)
        file1.close()

        #SimpleSubstitutionCipher.decipher(words=getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), encrypted=task1.lower())
        #numbers = Task6Playground.base26(task6)
        #analysis = Task6Playground.analyzeFrequencies(numbers)
        ##sentence = Task6Playground.convertToAlphabet(numbers)
        #MonoalphabeticPass.decipher(sentence,getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),"C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\task6.txt")
        #print('-------------------------------------')
        #print(sentence)
        #result = []
        #filename = "C:\\Users\\Levyaton\\PycharmProjects\\KAB-Semestralka\\test.txt"
        #for task in alphabeticTasks:
        #        result.extend(VignettCipher.decipher(task.lower(), getWords(
        #                "C:\\Users\\Levyaton\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),
        #                                      filename=filename))
        #result.sort(key=lambda x: x.counter, reverse=True)
        #file1 = open(filename, "w")
        #for sentece in result:
        #        sentece.printToFile(file1, includePassword=True, includeShift=True)
        #file1.close()



