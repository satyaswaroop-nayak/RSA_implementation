from time import time_ns

def decrypt(c, d, p, q, n):
    # Using chinese remainder theorem to decrypt c
    dp = d % (p-1)
    dq = d % (q-1)
    cp = c%p
    cq = c%q
    qinv = extendedEuclid(p, q)[1]%p
    m1 = pow(cp, dp, p)
    m2 = pow(cq ,dq, q)
    h = (qinv*(m1-m2))%p
    m = m2+h*q
    return m

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

def convertToString(decryptedMessage):
    num = 255
    plainText = ""
    while decryptedMessage>0:
        lastChar = chr(decryptedMessage&num)
        decryptedMessage >>= 8
        plainText = lastChar+plainText
    return plainText

cipherTextFile = open("./Ciphertext.txt", "r")
encryptedMessage = int(cipherTextFile.readline())
cipherTextFile.close()

privateKeyFile = open("./PrivateKey.txt", "r")
privateKeyStr = privateKeyFile.readline().split(", ")
d = int(privateKeyStr[0])
p = int(privateKeyStr[1])
q = int(privateKeyStr[2])
privateKeyFile.close()

publicKeyFile = open("./PublicKey.txt", "r")
keyArr = publicKeyFile.readline().split(", ")
publicKeyFile.close()
e = int(keyArr[0])
n = int(keyArr[1])

startTime = time_ns()
decryptedMessage = decrypt(encryptedMessage, d, p, q, n)
endTime = time_ns()
print("time: ", endTime-startTime)
plainText = convertToString(decryptedMessage)
print(plainText)
decryptedTextFile = open("./Decrypted.txt", "w")
decryptedTextFile.write(plainText)
decryptedTextFile.close()