def encrypt(m, e, n):
    # takes 3 inputs m, e and n and encrypts the message m
    return pow(m, e, n)

def convertToBinary(plainText):
    plainTextLength = len(plainText)
    if plainTextLength==0:
        return 0
    plainTextbin = 0
    plainTextbin |= ord(plainText[0])
    if plainTextLength==1:
        return plainTextbin
    for i in range(1, plainTextLength):
        plainTextbin <<= 8
        plainTextbin |= ord(plainText[i])
    return plainTextbin


plainTextFile = open("./Plaintext.txt", "r")
plainText = plainTextFile.readline()
plainTextbin = convertToBinary(plainText)
plainTextFile.close()

publicKeyFile = open("./PublicKey.txt", "r")
keyArr = publicKeyFile.readline().split(", ")
publicKeyFile.close()
e = int(keyArr[0])
n = int(keyArr[1])

encryptedMessage = encrypt(plainTextbin, e, n)
cipherTextFile = open("./Ciphertext.txt", "w")
cipherTextFile.write("%s" % encryptedMessage)
cipherTextFile.close()