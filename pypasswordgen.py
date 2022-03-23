import random
from os import system, name
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


go_again = True
while go_again:

    #User Prompts to build the Password
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #list to store variables
    sto_pwd = []

    #Chooses a random letter
    for char in range(1, nr_letters +1):
        sto_pwd += random.choice(letters)
        
    #Chooses a random symbol
    for char in range(1, nr_symbols +1):
        sto_pwd += random.choice(symbols)

    #Chooses a random number
    for char in range(1, nr_numbers +1):
        sto_pwd += random.choice(numbers)

    #shuffle the list
    random.shuffle(sto_pwd)

    #Set empty variable to hold the list
    pword = ""

    #populate the string with each term from the list
    for char in sto_pwd:
        pword += char

    #print the password as a complete string
    print(pword)

    again = input("Would you like another password? Type 'y' or 'n'.\n")
    if again == "n":
        go_again = False
    else:
        go_again = True
        clear()
        












    
    
