import MonoalphabeticPass
import VignettCipher
import NumberCipher
import os
task1= "NENSBXIZIIWUXRSQKNXQFHRIFXIHNQCIVRQEFYSCEQFMIASUWEBCEIFYENEUSQBGNSXGSUQFRIICQUSQBXNSXMIAWFEGXNESFUGERSZRESBM"

#Task2 is a monoalphabetic password cipher. The password was bowling. The deciphered text is heputitdownonthetablenearthedoortheworstthingintheworldsaidobrienisdifferentforeachpersonitmaybedeathbyfireorbywaterorfiftyotherdeathssometimesitissomethingquitesmallthatdoesnotevenkillyouhehadmovedtoonesideandwinstoncouldnowseewhatwasonthetable
task2= "AIMTSCSLKVJKJSAISBOFIJIBQSAILKKQSAIVKQRSSACJGCJSAIVKQFLRBCLKOQCIJCRLCNNIQIJSNKQIBWAMIQRKJCSHBYOILIBSAOYNCQIKQOYVBSIQKQNCNSYKSAIQLIBSARRKHISCHIRCSCRRKHISACJGPTCSIRHBFFSABSLKIRJKSIUIJECFFYKTAIABLHKUILSKKJIRCLIBJLVCJRSKJWKTFLJKVRIIVABSVBRKJSAISBOFI "

task3 = "WZZWGWNUAUNIRVASRRUHOMFBRVNYGAUQDVZPLPEHNUQVFBOBDNTEGBHRTLNIJISSOITISMLGVVDCIMRLSZOOLWUPAEFHBBHNTYQWPZENMVPSOZIRNNTEGLOLOLIEABMRTFPSCIIAACARRAAVDFNVVMNDUZQXYGIFNFFEYEALSVZSHOHGHVDEGPEPOEFMACEQLZWINBENCYQVTQVVNXMPRASBNVMXFUENTZZXUMPBOIBEEBSBFKTIGWWAADAXUMRPAEZSGTENVVTIEJAOYFGXFQDRBVOEHAEVNKQRZQNHTVEXUMRRWZXPBVLLBVNSAMSYEWF "

task4 = "SIHTHSTTTAOHETNNOTAOIEUEIAFTTTTTTESESERTCOOODEWTHCOEFRSIEXMEYCEIOMETGFNEUETBPEFEDHSICTXOMEAEFSIHTUEIHGEFUSVSHLTRTASHESAKYRMEYHHATTENHEURACSETTEEX"

task5 = "JTUHLEICAHIEDSOTNNTUCTATRREEWEHCAATFYEOWUADSOATLOMHOESRTDEEMSPTTRYOIYTHWEARSFTAHCEELLOENAEVLEYOTNILMYEBOOFNFEISFNTOETEMNEHJOUULRISAMNUOSTIMCECHAEMHEEFARRODMOTBHREITEENLTEOSUCCRHETEHNESSNWOIWTBCUHTAWNIDNKSNTEOWNHWEAHSALDICSLTOESNEIDNTGHFEODRONOERWTSOOTFHTEHTEUWBAERNXOXTXOXPXEXNXEXDXIXTX "

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


def getWords(filepath):
    #with open('english-words.txt') as f:
    with open(filepath) as f:
        return f.read().split()
def getWordsDefualt():
    #with open('english-words.txt') as f:
    with open('english-words.txt') as f:
        return f.read().split()

if __name__ == '__main__':
        test = "DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM OECBX SESCI YGUFP KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV OVVXH KWQIL IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF"
        test = test.replace(" ","")
        result = VignettCipher.decipher(test.lower(),getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), )

        #VignettCipher.decipher(task1.lower(),getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ShorterTask1.txt")
        #VignettCipher.decipher(task3.lower(), getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ShorterTask3.txt")
        #VignettCipher.decipher(task4.lower(), getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ShorterTask4.txt")
        #VignettCipher.decipher(task5.lower(), getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ShorterTask5.txt")
        #VignettCipher.decipher(task7.lower(), getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ShorterTask7.txt")
        #VignettCipher.decipher(task8.lower(), getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ShorterTask8.txt")
        #VignettCipher.decipher(task9.lower(), getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"), "C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\ShorterTask9.txt")
    #NumberCipher.decipher(task6,getWords("C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\english-words.txt"),"C:\\Users\\czech\\PycharmProjects\\KAB-Semestralka\\task6.txt")
    #print(VignettCipher.decrypt(dictionaries=VignettCipher.getDictionaries("lemon"), password="lemon",encrypted="lxfopvefrnhr"))
    #VignettCipher.decipher(task1.lower(), getWordsDefualt(), "task1.txt")
    #VignettCipher.decipher(task3.lower(), getWordsDefualt(), "task3.txt")
    #VignettCipher.decipher(task4.lower(), getWordsDefualt(), "task4.txt")
    #VignettCipher.decipher(task5.lower(), getWordsDefualt(), "task5.txt")
    #VignettCipher.decipher(task7.lower(), getWordsDefualt(), "task7.txt")
    #VignettCipher.decipher(task8.lower(), getWordsDefualt(), "task8.txt")
    #VignettCipher.decipher(task9.lower(), getWordsDefualt(), "task9.txt")

