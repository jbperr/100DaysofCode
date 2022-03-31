import os
done = False
auction = {}
bidName = ''
bid = 0

while not done:
    name = input("Enter your name: ")
    amount = int(input("How much will you bid? $"))
    
    auction[name] = amount
    new = input("Is there another person? (yes/no): ")
    
    if new == "no":
        done = True
        
    os.system('clear')

for i in auction:
    if auction[i] > bid:
        bid = auction[i]
        bidName = i

print(f"Congrats to {bidName} with a bid for ${bid}")