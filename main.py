from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = []
bids_value = []
other_bidders = 'yes'
while other_bidders == 'yes':
    name = input("What is your name?\n")
    bid = int(input("what is your bid?\n$"))
    clear()
    other_bidders = input("are there any other bidders? Type 'yes' or 'no'\n")
    def add_bidders(bidder_name,bidder_bid):
        new_bid = {
            "name": bidder_name,
            "bid": bidder_bid
        }
        bids.append(new_bid)
        bids_value.append(bidder_bid)
    add_bidders(name,bid)
clear()
max_bid = max(bids_value)
winner_index = bids_value.index(max_bid)
print(f"The winner is {bids[winner_index]['name']} with a bid of ${max_bid}")

