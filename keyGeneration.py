from random import randrange, getrandbits
import math

def generatePrime(k): 
    # Takes input k the number of bits the generated prime needs to be
    n = generatePrimeCandidate(k)
    while not isPrime(n, 128):
        n = generatePrimeCandidate(k)
    return n

def isPrime(n, rounds):
    # Takes a number and test whether the number id prime using miller-rabin test for primality
    # n: number to be tested
    # rounds: number of rounds

    if n<=1:
        return False
    
    # find s and d
    s = 0
    d = n-1
    while (d&1)==0:
        d = d >> 1
        s += 1

    while rounds>0:
        rounds -= 1
        a = randrange(2, n-1)
        if math.gcd(a, n)>1:
            return False
        x = pow(a, d, n)
        y = 0
        s_ = s
        while s_>0:
            s_ -= 1
            y = pow(x, 2, n)
            if y==1 and x != 1 and x != n-1:
                return False
            x = y
        if y!=1:
            return False
    return True



def generatePrimeCandidate(k):
    # Generates a k bit number which is a prime candidate
    p = getrandbits(k)
    p |= (1<<(k-1)) # Make MSB bit 1 to hold on to k bits
    p |= 1 # Make the number odd
    return p

def extendedEuclid(e, phiN):
    # Takes e, phiN as input and gives d, y such that e*d + phiN*y = 1
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1

    while e!=0:
        e1 = phiN % e
        q = phiN//e
        x2 = x0-q*x1
        y2 = y0-q*y1
        x0 = x1
        y0 = y1
        x1 = x2
        y1 = y2
        phiN = e
        e = e1
    return [x0, y0]
    
    

# Public Key Generation
p = generatePrime(512)
q = generatePrime(512)
while q==p:
    q = generatePrime(512)

# Public Key pair
e = 65537
n = p*q
# print(p, q) # debug

publicKeyFile = open("./PublicKey.txt", "w")
publicKeyFile.write("%s, %s" % (e, n))
publicKeyFile.close()

# Private Key Generation
phiN = (p-1)*(q-1)
d = extendedEuclid(e, phiN)[1] % phiN

privateKeyFile = open("./PrivateKey.txt", "w")
privateKeyFile.write("%s, %s, %s" % (d, p, q))
privateKeyFile.close()