from random import random
import secrets
import string
import re
file = "accounts.txt"
root = [" ", "root" , "ROOT"]
def main():
    print("MAIN MENU")
    print("---------")
    print("Please choose your option")
    print("LOG IN - enter 1")
    print("REGISTER - enter 2")
    while True:
        option = input("choose an option 1 OR 2, my dear user : ")
        if option in ["1", "2"]:
            break
    if option == "1":
        loginUser()
    else:
        registerUser()


def loginUser():
    print("LOG-IN")
    print("---------")
    userName = str(input("UserName: "))
    userPass = str(input("Password: "))
    with open(file,"r") as f:
        for row in f.readlines():
            row = row.split()
            f.close()
            if userName in row:
                index = row.index(userName)+1
                foundPass = row[index]
                if userPass == foundPass:
                    print ("LOGGED IN, welcome back " + userName)
                    main()
                else:
                    print ("WRONG, please try again")
                    loginUser()


def registerUser():
    print("REGISTER")
    print("---------")
    userName = str(input("Please input user name: "))
    with open(file,"r") as f:
        info = f.read()
        if userName in info or userName in root:
            print("userName is already existing or invalid, please try again")
            registerUser()
        else: 
            print("Please choose your password option")
            print("Ramdom Password- enter 1")
            print("your own choice password - enter 2")
            while True:
                option = input("choose an option 1 OR 2, my dear user : ")
                if option in ["1", "2"]:
                     break
            if option == "1":
                generatePass()
                print("Register done. Please-log-in-to-check")
            else:
                validPass()  
        f.close()
        main()


def generatePass():
    randomString = string.ascii_letters + string.punctuation + string.digits
    randomPass = ' '.join(secrets.choice(randomString) for i in range (10))
    return randomPass


def validPass():
    while True:
        userPass = str(input("Pleanse input your Password : "))
        if len(userPass) < 8:
            print("your password minimun lenth is 8")
        elif re.search("[0-9]", userPass) is None:
            print("your password need to have at least one number")
        elif re.search('[A-Z]', userPass) is None:
            print("your password need to have at least one capital letter")
        else:
            userPass1 = str(input("please confirm your password: "))
            if(userPass != userPass1):
                print("please try again")
                validPass()
            else:
                print("Register done. Please log-in")


main()
