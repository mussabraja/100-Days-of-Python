import art
print(art.logo)

total_bids = {}
new_bids = True
while new_bids:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $ "))
    total_bids[name] = price
    new_bids_question = input("Are there any new bidders, Yes or No ").lower()
    if new_bids_question == "yes":
        print("\n" * 100)
    else:
        new_bids = False

max_bid = 0
winner = ''
for bidder in total_bids:
    x = (total_bids[bidder])
    if x > max_bid:
        max_bid = x
        winner = bidder
print(f"Highest bid is {max_bid} by {winner}")
