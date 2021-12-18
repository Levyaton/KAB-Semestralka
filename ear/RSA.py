import math


#Extend extended_gcd and inverse_modulo borrowed from https://github.com/ZeroBone/PollardRsaCracker
def find_mod_inv(a,m):

    for x in range(1,m):
        print(str(x))
        if((a%m)*(x%m) % m==1):
            return x

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def int_to_ASCII(integer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = str(integer)
    pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    result = ""
    for pair in pairs:
        result += alphabet[int(pair)%26]
    return result

def decipher(message, e, n):
    result = ""
    sections = message.split()
    for sect in sections:
        result += decrypt(sect,e,n)
    print(result)
def decrypt(message, e, n):
    pms = primes(n)
    if len(pms) != 2:
        print("BAD N, TOO MANY OR FEW PRIMES")
        return None
    p = pms[0]
    q = pms[1]
    phi = int((p-1)*(q-1))
    #d = (1 % phi)/e
    d = find_mod_inv(e,phi)
    #m = int(int(message)**d)%n
    m = int(message)**d%n
    return int_to_ASCII(m)

if __name__ == '__main__':
    print(int_to_ASCII("6333329"))