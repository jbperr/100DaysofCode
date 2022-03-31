print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

print('''You open your eyes to the sun rising to your left. The last thing you
remember is a massive storm appearing out of nowhere. You look around and see
your boat grounded on the rocky beach. You decide to gather what you can from
the shipwreck and explore the island. You think you can see another ship to your
right and a river to your left.''' )

beachDirection = (input("Which direction do you explore first? (L) or (R) ")).upper()

if beachDirection == "L":
    print('''\nYou decide to head towards the sun. After some time of walking you
    get to the river. The river is moving quite fast, but you think you can make
    it across with your swimming abilities. Or you could wait and think.''')

    riverDecision = (input("Do you risk it and swim or wait it out and think? (S) or (W) ")).upper()

    if riverDecision == "S":
        print(''' While the current is swift and you feel yourself getting swept
        away, you are able to make it across. As you get your bearing on the shore,
        you can see a path on the ground and decide to follow it. After some time
        you find a temple with three doors. You can make out traps on the doors
        that seem like they would close off the doors you don't choose. The red
        door on the left has a symbol of fire. The blue door in the middle has a
        symbol of a river. Finally, the yellow door has a symbol of a lightning
        bolt. ''')

        doorDecision = (input("Which door do you enter? (R) or (B) or (Y) or (G)")).upper()

        if doorDecision == "R":
            print('''You move towards the red door feeling the hot sun up above.
            You reach your hand out and grab the red door handle. Instantly a trap
            slings out and cuffs your hand to the door. Before you can react to that,
            you realize your hand is burning. Your body is burning. The door wasn't
            red from paint. The door was red due to how hot it was. You are stuck to
            the door as you slowly burn to death from your hand to your body. Maybe
            sun wasn't so hot. ''')
        elif doorDecision == "Y":
            print('''You cautiously open the yellow door, half expecting to be
            killed by an electric shock. To your surprise the door swings open
            welcomingly. You enter the room and look around slowly. You are amazed
            at how much gold you see. From floor to ceiling, gold coins are stuffed
            into this tiny room. You pack as much as possible into your bag and
            make many trips back to your boat to load up the emergency skiff. Looks
            like this trip wasn't a total waste after all.''')
        elif doorDecision == "B":
            print('''You take a couple steps up to the blue door. You can hear the
            river rushing in the background. You reach your hand out and the door
            swings open. You let out a triumphant yell as you walk proudly into
            the room. Suddenly, the door slams shut and you realize you walked into
            an empty room. You realize somehow the sound of water rushing is even
            louder in this room. Before you can realize that you shouldn't be
            able to hear the river from where you are, the stone bricks on the wall
            are pushed out from their position and water starts flooding into the
            tiny room. You slowly rise as the water fills the room. You try your
            hardest to get out as the water gets to your neck. You realize that
            no amount of swimming will get you out of here. Your last thoughts are
            of your home.''')
        elif doorDecision == "G":
            print('''You find a nice book outside the door. You sit on a stump next
            to the door with a corn cob pipe. You start the book entitled
            \' Politically Correct Holiday Stories: For an Enlightened Yuletide Season\'
            You chuckle heartily to yourself as you read about Frosty the SnowPerson.''')

    elif riverDecision == "W":
        print('''You wait on the shore a little bit and the sun gets directly
        overhead. It starts to get warmer by the river and you can hear some rustling
        and swishing sounds in the water. Crocodiles emerge from the water to
        sunbathe on the river shore. Before you know it you are being dragged
        underwater for an afternoon snack. Looks like you ended up swimming anyways.''')

elif beachDirection == "R":
    print('''You walk to your right away from the sun. You happen upon another
    shipwreck you decide it would be a good idea to salvage some more supplies
    before heading too far from your ship. As you enter the ship you see a part
    of the ship that is still underwater, you think you can make out a door in
    the water. Swimming closer, you try to open it and it swings open with some
    force. You dive into the now open door to see what it hides. As you pass the
    doorframe, you are able to see clearly what is in the room. Four bodies are
    decomposing in this room and the door slams shut as you completely enter the
    room.
    Five bodies are decomposing in this room.''')
