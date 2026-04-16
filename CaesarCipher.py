import string

Alphabet = list(string.ascii_lowercase)

while True:
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    Do = input(">")

    if Do.lower() == "e" or Do.lower() == "d":
        break
    
    print("Inser 'e' or 'd'")

while True:
    print("Please enter the number to use.")
    Key = input(">")

    try:
        Key = int(Key)
        
    except:
        print("Insert a valid number")
        continue

    if Key < 1:
        print("Insert a valid number")
        continue
    break

Mode = "encrypt"

if Do.lower() == "e":
    Mode = "encrypt"
elif Do.lower() == "d":
    Mode = "decrypt"

print(f"Enter the message to {Mode}.")
Message = input(">").lower()

Translated = ""

for character in Message:
    index = 0
    
    try:
        character = int(character)
        Translated += str(character)
        continue
    except:
        pass

    if character == " ":
        Translated += " "
        continue
    elif type(character) == int:
        print(character)

    else:
        try:
            index = Alphabet.index(character)
        except:
            Translated += character
            continue
    
    if Mode == "encrypt":
        NewIndex = index + Key
    elif Mode == "decrypt":
        NewIndex = index - Key

    if Mode == "encrypt":
        while NewIndex > len(Alphabet) - 1:
            NewIndex -= len(Alphabet)
    elif Mode == "decrypt":
        while NewIndex < 0:
            NewIndex += len(Alphabet)

    Translated += Alphabet[NewIndex]

print()
print(Translated.capitalize())