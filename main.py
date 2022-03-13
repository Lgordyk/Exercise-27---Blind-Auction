from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the Secret Auction program!")

name_of_bidder = ""
bid_value = ""
more_bidders = ""
continue_game = "yes"
dictionary_of_bidders = {}

while continue_game == "yes":
  name_of_bidder = input("What is your name?:")
  bid_value = input("What is your bid?:")
  continue_game = input("Are there more bidders? type 'yes' or 'no':")
  dictionary_of_bidders[name_of_bidder] = bid_value
  if continue_game == "yes":
    clear()
    
clear()
max_score = 0
highest_bidder = ""

for each_person in dictionary_of_bidders:
  if float(dictionary_of_bidders[each_person]) >= float(max_score):
    max_score = dictionary_of_bidders[each_person]
    highest_bidder = each_person

print(f"The winner is {highest_bidder} with a bid of ${max_score}.")


  
