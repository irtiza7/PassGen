import random
import sqlite3


def generatePassword():

    #ask the length of password
    print("Password Length?")
    passwordLength = input(">")
    passwordLength = int(passwordLength)

    #ask the type of password the user wants
    print()
    print("Password Type?")
    print("[Enter N or n for Numeric Only Password]")
    print("[Enter A or a for Alphabetic Only Password]")
    print("[Enter M or m for Aplpha + Numeric Password]")
    passwordType = input(">")

    passwordType = passwordType.lower()

    #randomly generating a string of length and type given by the user
    if passwordType == "n":
        password = random.choices("0123456789", k = passwordLength)
        return password
    elif passwordType == "a":
        password = random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k = passwordLength)
        return password
    elif passwordType == "m":
        password = random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k = passwordLength)
        return password
    else: 
        print("Invalid Type Entered")
        return None



def savePassword():

    #get data from user
    print("Enter Email")
    userEmail = input(">")
    print("Enter Password")
    userPassword = input(">")
    print("Enter Account Type") #such as facebook, google, linkedln
    accountType = input(">")

    #connecting to database
    connection = sqlite3.connect("credentials.db")
    c = connection.cursor()

    #query to insert user data
    c.execute("""INSERT INTO credentials VALUES (:email, :password, :type)""", {"email": userEmail, "password": userPassword, "type": accountType})

    #commiting to database *important step*
    connection.commit()

    #disconnecting from database
    connection.close()


def findPassword():

    state = True

    #connecting to database
    connection = sqlite3.connect("credentials.db")
    c = connection.cursor()

    while state == True:
        #setting the type of search according to user's choice
        print("Enter 1 to Search with Email and Account Type")
        print("Enter 0 to Search with Only Account Type")
        choice = input(">")
        print()
        choice = int(choice)

        if choice == 1:
            
            #getting the data on which query has to be made
            print("Enter Email")
            userEmail = input(">")
            print("Enter Account Type")
            accountType = input(">")
            print()

            #query to find user data
            c.execute("""SELECT * FROM credentials WHERE email=:email AND type=:type""", {"email": userEmail, "type": accountType})
        
            #printing all results containing email, password and type
            print(c.fetchall())
    
            #commiting to database *important step*
            connection.commit()

            #breaking the loop
            state = False

        elif choice == 0:
            #getting the data on which query has to be made
            print("Enter Account Type")
            accountType = input(">")
            print()
        
            #query to find user data
            c.execute("""SELECT * FROM credentials WHERE type=:type""", {"type": accountType})
        
            #printing all results containing email, password and type
            print(c.fetchall())
    
            #commiting to database *important step*
            connection.commit()

            #breaking the loop
            state = False

        else:
            print("Invalid Search Type Entered, Try Again!")
            print()    

    #disconnecting from database
    connection.close()


#print welcome screen 
#ask what the user wants to do
state = True
while(state == True):

    print("[Enter G or g to Generate Password]")
    print("[Enter S or s to Save Password]")
    print("[Enter F or f to Find Password]")
    print("[Enter E or e to Exit Application]")
    actionType = input(">")
    print()

    actionType = actionType.lower()

    if actionType == "g":
        password = generatePassword()
        print("Password: " + ''.join(password))
        print()
    elif actionType == "s":
        savePassword()
        print()
    elif actionType == "f":
        findPassword()
        print()
    elif actionType == "e":
        print("Exiting Password Generator")
        print()
        state = False
    else:
        print("Invalid Option Entered, Try Again")
        print()

