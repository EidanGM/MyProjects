from random import randrange

Turns = 10
MyKeyWord = "Jugar"

print("")

def LetsPlay():
    HiddenNumber = randrange(100,999)

    #print(HiddenNumber)

    HiddenDijits = []

    for i in str(HiddenNumber):
        HiddenDijits.append(i)

    Tries = 0
    Guess = 0

    print(f"Adivina el numero de 3 dijitos en {Turns} turns, las reglas son las siguientes:", "\n", "")
    print('Por cada numero correcto en la posicion incorrecta, se imprimira "Pico"')
    print('Por cada numero correcto en la posicion correcta, se imprimira "Fermi"')
    print('Si ningun numero esta correcto se imprimira "Bagels"', "\n", "")

    def MakeGuess(guess): #It makes sure the user only insert a valid numer

        try:
            int(guess)
        except ValueError:
            guess = MakeGuess(input("Por favor inserte un numero de tres dijitos: "))
            

        if int(guess) < 100 or int(guess) > 999:
            guess = MakeGuess(input("Por favor inserte un numero de tres dijitos: "))
        else:
            return int(guess)
            print(guess)
        

    while Tries < Turns and Guess != HiddenNumber: #The loop that checks which numbers did you get in every try
        Tries += 1

        print(f"Guess #{Tries}:")
        Guess = MakeGuess(input("> "))

        Dijits = []
        BagelWords = []
        ChekedDijits = []

        for i in str(Guess):
            Dijits.append(i)

        for i in range(len(Dijits)):

            for x in range(len(HiddenDijits)):
                if HiddenDijits[i] == Dijits[x]:

                    if x == i: 
                        BagelWords.append("Fermi")
                    else:
                        if HiddenDijits[x] == Dijits[x]: continue
                        if HiddenDijits[i] == Dijits[i]:
                            BagelWords.append("Fermi")
                        else:
                            BagelWords.append("Pico")
                    break

        if len(BagelWords) == 0:
            print("Bagels")
        else:
            for i in range(len(BagelWords)):
                print(BagelWords[i], end = " ")
            
            print("")
        print("")

    if Guess == HiddenNumber: #Check if you get the number 
        print("Felicidades!")
    else:
        print("Mejor suerte la proxima vez, el numero era: ", HiddenNumber)

    print("")

    Again = input(f'Escribe "{MyKeyWord}" para volver a empezar: ')

    if Again == MyKeyWord:
        LetsPlay()
    else:
        print("Adios")

LetsPlay()