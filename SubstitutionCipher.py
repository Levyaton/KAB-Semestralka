from pycipher import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score
from WordPower import WordPowerObject as WordPower

def decript(encrypted,quadrams,words):
    i = 0
    fitness = ngram_score(quadrams)  # load our quadgram statistics
    ctext = encrypted
    ctext = re.sub('[^A-Z]', '', ctext.upper())

    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maxscore = -99e9
    parentscore, parentkey = maxscore, maxkey[:]
    while i < 30:
        i = i+1
        random.shuffle(parentkey)
        deciphered = SimpleSub(parentkey).decipher(ctext)
        parentscore = fitness.score(deciphered)
        count = 0
        while count < 1000:
            a = random.randint(0,25)
            b = random.randint(0,25)
            child = parentkey[:]
            # swap two characters in the child
            child[a],child[b] = child[b],child[a]
            deciphered = SimpleSub(child).decipher(ctext)
            score = fitness.score(deciphered)
            # if the child was better, replace the parent with it
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count+1
        # keep track of best score seen so far
        if parentscore>maxscore:
            maxscore,maxkey = parentscore,parentkey[:]
            print ('\nbest score so far:',maxscore,'on iteration',i)
            ss = SimpleSub(maxkey)
            print ('    best key: '+''.join(maxkey))
            print ('    plaintext: '+ss.decipher(ctext))
    return WordPower(SimpleSub(maxkey).decipher(ctext),shift=None,password=str(maxkey),words=words)
