import string

Alphabet = list(string.ascii_lowercase)

print("Insert the code to hack.")
Code = input("> ")

for i in range(len(Alphabet)):

    Translated = ""

    for character in Code:
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
            pass
        else:
            try:
                index = Alphabet.index(character.lower())
            except:
                Translated += character
                continue

        NewIndex = index + i

        while NewIndex > len(Alphabet) - 1:
            NewIndex -= len(Alphabet)

        Translated += Alphabet[NewIndex]
    
    print(Translated)
    print()

