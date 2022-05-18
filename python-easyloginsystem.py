from random import random
import secrets
import string
import re
import time
file = "accounts.txt"
root = [" ", "root" , "ROOT", "admin","ADMIN"]
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
    validation(userName, userPass)
    
def validation(userName, userPass):
    with open(file,"r") as f: 
        with open(file,"r") as f:
            for row in f.readlines():
             row = row.split()
             f.close()
             if userName in row:
                index = row.index(userName)+1
                foundPass = row[index]
                if userPass == foundPass and userName not in root:
                    print ("LOGGED IN, welcome back " + userName)
                    sleep(2)
                    main()
                elif userName in root and userPass == foundPass:
                    print("HI ADMIN, HERE IS THE LIST OF ACCOUNTS")
                    viewAccount()
                    print("Good-bye")
                    sleep(3)
                    main()
                else:
                    print ("Wrong user or password, please try again")
                    loginUser()
            else:
                print ("Wrong user or wrong password, please try again") 
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
                userPass = generatePass()
                print("your new password is "+ userPass)
                print("Register done. Please-log-in-to-check")
            else:
                userPass = validPass()
                print("Register done. Please-log-in-to-check")
        f.close()
        with open(file,"a") as f:
            f.write(userName)
            f.write(" ")
            f.write(userPass)
            f.write("\n")
            f.close()
        main()


def generatePass():
    randomString = string.ascii_letters + string.punctuation + string.digits
    randomPass = ''.join(secrets.choice(randomString) for i in range (10))
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
                return userPass;

def sleep(int):
    time.sleep(int)

def viewAccount():
    with open(file) as f:
        for line in f:
            print(line.strip())

main()
