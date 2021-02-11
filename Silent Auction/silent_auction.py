from replit import clear
import os
import pyfiglet
from art import logo,item,text
os.system('clear')
print(text)
print("\n")
print(logo)
print("\n")
print("          The Item Up For Auctions Is :")
print(item)
print("\n")
print("Welcome to the secret auction program.")

bids = {}


def add_to_dict():
    ok = True
    while ok:
        name = input("Enter Your Name : ")
        print("\n")
        bid = int(input("Enter your bid amount : $"))
        print("\n")
        bids[name] = bid
        done = input(r"Are you done?If yes type 'done' or if not type 'no' : ")
        print("\n")

        if done == "done":
            ok = False
        elif done == "no":
            ok = True
            clear()
            os.system('clear')
            print(text)
            print("\n")
            print(logo)
            print("\n")
            print("          The Item Up For Auction Is        :")
            print(item)
        else:
            print("error incorrect option")
            done = input(r"Are you done?If yes type 'done' or if not type 'no' : ")
            print("\n")


add_to_dict()

print("The highest bid amount is : $", max((bids.values())), "   by : ",
      (list(bids.keys())[list(bids.values()).index(max((bids.values())))]))

result = pyfiglet.figlet_format(str(list(bids.keys())[list(bids.values()).index(max((bids.values())))]),font="doom")
result1 = pyfiglet.figlet_format(f"$ {str(max((bids.values())))}",font="doom")
print(result,"\n")

print(result1,"\n")