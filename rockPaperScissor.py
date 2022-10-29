import random as r
flag = "Y"
while flag =="Y" or flag == "y":

    ele = r.randint(0,2)
    lst = ["rock","paper","scissor"]
    inp = input("Rock/paper/scissor")
    user = inp.lower()
    comp = lst[ele]
    mess = "Your input is {} and comp input is {}"
    print(mess.format(user,comp))
    if user == comp:
        print("Draw")
    elif user[0] == "r":
        if comp[0] == "p":
            print("Computer wins")
        elif comp[0] == "s":
             print("You win")
    elif user[0] == "p":
        if comp[0] == "r":
            print("You win")
        elif comp[0] == "s":
            print("Computer wins")
    elif user[0] == "s":
        if comp[0] == "r":
            print("Computer wins")
        elif comp[0] == "p":
            print("You win")
    else:
        print("Enter correct input")
    flag = input("Enter Y to continue the game or enter N")
print("Thank you for playing the game")
