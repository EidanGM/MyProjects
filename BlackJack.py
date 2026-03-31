from random import randrange
import time

Rules = """
Rules
Try to get as close to 21 without going over
Kings, Queens, and Jacks are worth 10 points
Aces are worth 11 points, but if your hand in higher than 21, your Ace will be worth 1
Cards 2 through 10 are worth their face value
(H)it to take another card
(S)tand to stop taking cards
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing
In case of a tie, the bet is returned to the player
The dealer stops hitting at 17

"""
print(Rules)

Money = 5000

Symbols = ["♥","♠","♦","♣"]

HouseCards = []
GamblerCards = []

HouseHandValue = 0
GamblerHandValue = 0

Bet = 0

def MakeABet():
    global Money
    Bet = input(f"How much do you bet? (1$-{Money}$, or QUIT) >").upper()
    
    try:
        Bet = int(Bet)
        if Bet > Money:
            Bet = Money
        elif Bet <= 0:
            Bet = 1

        return Bet
    except ValueError:
        print("Make a valid bet")
        Bet = MakeABet()

def SetCard(Gambler, value):

    S = Symbols[randrange(0, len(Symbols) - 1)]
    x = value

    if value == 1: x = "A"
    elif value == 10:
        Figures = ["K", "Q", "J", 10]
        x = Figures[randrange(0, len(Figures) - 1)]

    Hands = []

    if Gambler == "House": 
        HouseCards.append([x, S])
        Hands = HouseCards
        print("House: ", HandValue(HouseCards))
    elif Gambler == "Gambler": 
        GamblerCards.append([x, S])
        Hands = GamblerCards
        if len(GamblerCards) == 1: return
        print("Player: ", HandValue(GamblerCards))

    for card in Hands:
        print(" ___ ", end="  ")
    print()
    for card in Hands:
        print(f"|{card[0]}  |", end="  ")
    print()
    for card in Hands:
        print(f"| {card[1]} |", end="  ")
    print()
    for card in Hands:
        print(f"|__{card[0]}|", end="  ")
    print()

def UseAces(handvalue, aces):
    while handvalue > 21 and aces > 0:
        aces -= 1
        handvalue -= 10
    
    return handvalue

def HandValue(Hands):

    global HouseCards 
    global GamblerCards
    global HouseHandValue 
    global GamblerHandValue

    HandValue = 0
    Aces = 0

    for card in Hands:
        if card[0] == "A": 
            HandValue += 11
            Aces += 1

        elif card[0] == "K" or card[0] == "J" or card[0] == "Q": HandValue += 10
        else: HandValue += card[0]

    if HandValue > 21 and Aces > 0:
        HandValue = UseAces(HandValue, Aces)
    
    if Hands == HouseCards:
        HouseHandValue = HandValue
        return HouseHandValue
    elif Hands == GamblerCards:
        GamblerHandValue = HandValue
        return GamblerHandValue


def BlackJack():
    global HouseCards 
    global GamblerCards
    global HouseHandValue 
    global GamblerHandValue
    global Bet
    global Money

    print("Money: ", Money,"$", sep="")
    
    HouseCards = []
    GamblerCards = []

    Bet = MakeABet()
    print()
    print("Bet: ",Bet,"$", sep="")

    randnum = randrange(1,11)

    SetCard("House", randnum)
    print()

    randnum1 = randrange(1,11)
    randnum2 = randrange(1,11)

    time.sleep(1)
    SetCard("Gambler", randnum1)
    SetCard("Gambler", randnum2)
    print()

    def play():
        
        global HouseCards 
        global GamblerCards
        global HouseHandValue 
        global GamblerHandValue
        global Bet
        global Money

        if len(GamblerCards) == 2 and Money >= (Bet * 2):
            print("(H)it, (S)tand, (D)ouble down")
        else:
            print("(H)it, (S)tand")

        Option = input("What you want to do now? >")

        if Option.lower() == "h":
            randnum = randrange(1,11)
            SetCard("Gambler", randnum)
            print()
            if GamblerHandValue > 21: return
            play()

        elif Option.lower() == "s":
            return
        
        elif Option.lower() == "d" and len(GamblerCards) == 2 and Money >= (Bet * 2):
            Bet *= 2
            randnum = randrange(1,11)
            print("Bet: ",Bet,"$", sep="")
            SetCard("Gambler", randnum)
            print()
            if GamblerHandValue > 21: return
            play()
        else:
            print("Insert a valid option")
            play()
    play()
    
    if GamblerHandValue > 21:
        print("You lost ",Bet,"$", sep="")
        Money -= Bet
        print("Money: ", Money,"$", sep="")
        print()
        if Money <= 0:
            print("You don't have more money to bet")
            return
         
        print("(Quit, or (A)gain)")
        Again = input(">").lower()
        
        if Again == "a":
            BlackJack()
        else: return
    
    while HouseHandValue < 17:
        randnum = randrange(1,11)

        SetCard("House", randnum)
        print()
        time.sleep(1)

    if HouseHandValue > 21:
        print("You won: ", Bet * 2,"$", sep="")
        Money += Bet * 2
        print("Money: ", Money)
        print()
        print("(Quit, or (A)gain)")
        Again = input(">").lower()
            
        if Again == "a":
            BlackJack()
        else: return
    
    if GamblerHandValue > HouseHandValue:
        print("You won: ", Bet * 2,"$", sep="")
        Money += Bet * 2
        print("Money: ", Money)
        print()
        print("(Quit, or (A)gain)")
        Again = input(">").lower()
        
        if Again == "a":
            BlackJack()
        else: return
    elif HouseHandValue > GamblerHandValue:
        print("You lost ",Bet,"$", sep="")
        Money -= Bet
        print("Money: ", Money,"$", sep="")
        print()
        if Money <= 0:
            print("You don't have more money to bet")
            return
         
        print("(Quit, or (A)gain)")
        Again = input(">").lower()
        
        if Again == "a":
            BlackJack()
        else: return
    else:
        print("It's a tie, you get your money back")
         
        print("(Quit, or (A)gain)")
        Again = input(">").lower()
        
        if Again == "a":
            BlackJack()
        else: return

BlackJack()