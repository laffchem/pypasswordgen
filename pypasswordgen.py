import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#User Prompts to build the Password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#lists to store variables
sto_let = []
sto_sym = []
sto_num = []
sto_char = []
password = ("")

#Chooses a random letter
for x in range(0, nr_letters):
    x = random.choice(letters)
    sto_let.append(x)
print(sto_let)
#Chooses a random symbol
for y in range(0, nr_symbols):
    y = random.choice(symbols)
    sto_sym.append(y)
print(sto_sym)
#Chooses a random number
for z in range(0, nr_numbers):
    z = random.choice(numbers)
    sto_num.append(z)
print(sto_num)
#Add the lists together
sto_char = sto_sym + sto_num + sto_let

#Set empty variable to hold the lists
pword = ""

#populate the string with each term from the list
for i in sto_char:
    pword = pword + i

#randomly join the string to create the password
print("".join(random.sample(pword, len(pword))))












    
    
