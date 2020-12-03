usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "Chanon" and passwordInput == "1234" :
    print("Welcome")
    print("-----Chanon Shop-----")
    print("1.Sandwich 20 THB")
    print("2.Burger 50 THB")
    print("3.Taco 40 THB")
    userSeleted = int(input(">>"))

    if userSeleted == 1:
        amount = int(input("How many pieces"))
        print("Total =", amount*20)
        print("Thanks")
    elif userSeleted == 2:
        amount = int(input("How many pieces"))
        print("Total =", amount*50)
        print("Thanks")
    elif userSeleted == 3:
        amount = int(input("How many pieces"))
        print("Total =", amount*40)
        print("Thanks")
    else:
        print("Please try again")
