import sys


master_pwd = input("What is the master Password? ")

def view():
    pass

def view():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("passwords.txt", 'a')as f:
        


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add) or q to quit? ")
    if mode == "q":
        quit

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

