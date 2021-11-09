import pyecm
import sys

def decipher(task):
    for element in breakCipher(task):
        print(str(element))

def breakCipher(task):
    q = 0
    p = 0
    factors = list(pyecm.factors(n=int(task),veb=False,ra=True,ov=10,pr=1))
    q = factors[0]
    p = factors[1]
    print(str(p))
    print(str(q))
    phi = (p-1)*(q-1)