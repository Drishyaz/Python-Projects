import string
import random

def keyGen(key,pasw):       #return a randomized key
    plen = len(pasw)        #10
    klen = len(key)         #6
    if plen > klen:
        gap = plen - klen   #4
    elif klen > plen:
        gap = klen -plen
   
    key = list(key)
    random.shuffle(key)
    key += ['0' for i in range(gap)]    #blabla0000

    k=""
    for i in key:
        k = k + i

    return k

def hashing(newKey,pasw):
    plen = len(pasw)            #10
    charRange = string.ascii_letters + string.digits # + string.punctuation
    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 and some punctustion
    crLen = len(charRange)      #62
    encrypted = []
    
    for _ in range(plen):   #0 to 9
        p = charRange.find(pasw[_])
        k = charRange.find(newKey[_])
        replacement_char = p + k

        if replacement_char > 62:
            replacement_char -= 62

        encrypted.append(charRange[replacement_char])

    return encrypted

    
pasw = input("Enter a password: ").strip()  #drishyaz99
key = input("Enter a key: ").strip()        #blabla

newKey = keyGen(key,pasw)
print("This is your new key:",newKey)

res = hashing(newKey,pasw)
encrypt = ""
for _ in res:
    encrypt += _
    
print("Encrypted password:",encrypt)

