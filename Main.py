#imports are done
from GeneratePassword import *

def main():
    while True: #While loop is used to not close the program unless the user enters option 2
        print("\n!!!Welcome User!!!")
        print("\nDo you need to create a random password? 1) Yes 2) No")
        choice = int(input("Enter an option..."))
        if choice == 1:
            genPassword()
        elif choice == 2:
            print("\n!!!Bye, See you soon!!!")
            quit()
        else:
            print("\nInvalid option entered. Enter a valid option...")
main()