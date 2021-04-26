import random
import sqlite3


def pass_type():
    
    l = input("Enter the Length of Password You Want: ")
    l = int(l)

    #ask the type of password from user
    print()
    print("Enter the Type of Password You Want: ")
    t = input(
        "[H/h for Hexadecimal]\n[O/o for Octatal]\n[B/b for Binary]\n[D/d for Decimal]\n>")
    t = t.lower()

    if t == "h":
        p_list = random.choices("0123456789ABCDEF", k=l)
        print("Password: " + ''.join(p_list))
        return None
    elif t == "o":
        p_list = random.choices("01234567", k=l)
        print("Password: " + ''.join(p_list))
        return None
    elif t == "b":
        p_list = random.choices("01", k=l)
        print("Password: " + ''.join(p_list))
        return None
    elif t == "d":
        p_list = random.choices("0123456789", k=l)
        print("Password: " + ''.join(p_list))
    else:
        print("Invalid Type Entered!")
        return None

    
def generatePassword():
    print("Password Length?")
    passwordLength = input(">")
    passwordLength = int(passwordLength)

    print()
    print("Password Type?")
    print("[Enter N or n for Numeric Only Password]")
    print("[Enter A or a for Alphabetic Only Password]")
    print("[Enter M or m for Aplpha + Numeric Password]")
    passwordType = input(">")

    passwordType = passwordType.lower()

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
    c = conn.cursor()

    #query to insert user data
    c.execute("""INSERT INTO credentials VALUES (:email, :password, :type)""", {"emial": userEmail, "password": userPassword, "type": accountType})

    #commiting to database *important step*
    connection.commit()

    #disconnecting from database
    connection.close()



def findPassword():
    pass


#print welcome screen 
#ask what the user wants to do
state = True
while(state == True):

    print("[Enter G or g to Generate Password]")
    print("[Enter S or s to Save Password]")
    print("[Enter F or f to Find Password]")
    actionType = input(">")
    print()

    actionType = actionType.lower()

    if actionType == "g":
        password = generatePassword()
        print("Password: " + ''.join(password))
        print()
    elif actionType == "s":
        savePassword()
    elif actionType == "f":
        findPassword()
    else:
        print("Exiting Password Generator")
        state = False

