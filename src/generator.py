import string 
import random 

#this line stores all the possible characters in a list we can extract data from later
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password(): 
    length = int(input("Enter Password Length: "))
    random.shuffle(characters)

    password = [] 
    for i in range(length): 
        password.append(random.choice(characters))
    random.shuffle(password)

    #print(str(password)) would simply just change all the values in the list to strings
    #to actually change the list into a string we need to do this: 
    print("".join(password))

generate_random_password()