#imports are done
import string
import random

def genPassword():
    len = int(input("Enter the length of password..."))
    password = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    # string.ascii_letters print letters from a - Z
    # string.digits print 0-9
    randomPassword = []
    for i in range(len):
            randomPassword.append(random.choice(password))
            #random.choice is used to select a random element from a sequence
    passwordGenerated = ""
    for i in randomPassword:
        passwordGenerated = passwordGenerated + i
    print("\nPassword generation completed!!!\nYour new password is: {}".format(passwordGenerated))