## password-generator

#The program takes user input from the user that is, how much length of password does the user want?
#Enter password length: 
#8

#Generates a random password of length 8. E.g,
#Your password is: 
#Ue=$tP&r

import string
import random

'''
This is how you can access the lowecase, uppercase, digits and punctuation characters of string class
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
'''

while True:
    try:
        pwd_len = int(input("\nEnter password length: "))
        #Handles Gibberish input other than integer

        s = string.printable.strip()
        s = list(s)

        print("Your password is: ")

        random.shuffle(s)
        print("".join(s[0:pwd_len]))

        #------ alternate way ------
        #print("".join(random.sample(s,pwd_len)))

    except ValueError:
        print("Please enter valid number input")
