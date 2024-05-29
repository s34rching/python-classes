from logo import logo
import os

print(logo)
print("Welcome to the Secret Auction!")

bidders = []
is_any_bidder = True

while is_any_bidder:
    name_input = input("What is your name?: ")
    bid_input = input("What is your bid?: $")

    bidder = {}
    bidder["name"] = name_input
    bidder["bid"] = int(bid_input)

    bidders.append(bidder)

    any_other_bidder_input = input("Are there any other bidders ('yes' or 'no')?: ")

    os.system('clear')

    if (any_other_bidder_input == 'no'):
        is_any_bidder = False

winner = {}

for participant in bidders:
    biggest_bid = 0

    if (participant["bid"] > biggest_bid):
        biggest_bid = participant["bid"]
        winner = participant

print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")

