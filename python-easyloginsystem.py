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
    with open("accounts.txt", "r") as file:
        for row in file:
            row = row.split()
            if row[0] == userName:
                userFound = [row[0], row[1]]
                if userFound[1] == userPass:
                    print("Log in Success")
                    print("Do you want to log out? ")
                    while True:
                        option = input("Y / N")
                        if option == "Y":
                            main()
                        else:
                            break
                break;
            else:
                print("your user name or password are incorrect")


def registerUser():
    print("REGISTER")
    print("---------")
    while True:
        userName = str(input("Please input user name: "))
        userPass = str(input("Please input your password: "))

main()