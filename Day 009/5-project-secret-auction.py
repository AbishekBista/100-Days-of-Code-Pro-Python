from art import logo
from os import system

print(logo)
print('Welcome to the Mario Secret Auction Program')

bidding_list = {}

def add_to_bidding_list(name, bid):
    bidding_list[name] = bid

def find_highest_bidder():
    highest_bid = 0
    for bidder in bidding_list:
        if bidding_list[bidder] > highest_bid:
            highest_bid = bidding_list[bidder]
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


has_bidder = True

while has_bidder == True:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    
    add_to_bidding_list(name, bid)

    has_more_bidder = input("Are there any other bidder? Type 'yes' or 'no'. ")
    
    if has_more_bidder == 'yes':
        system('cls')
        
    else:
        has_bidder = False
        find_highest_bidder()







