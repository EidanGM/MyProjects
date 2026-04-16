from random import randrange
import time

print("Player1: Insert a 3 character name")
Player1 = input(">")

print("Player2: Insert a 3 character name")
Player2 = input(">")

Pre1 = ""
Pre2 = ""

for i in range(3):
   Pre1 += Player1[i].upper()
   Pre2 += Player2[i].upper()

Carrot = randrange(1,3)
print(Carrot)

Boxes = f"""  
  __________      __________
 /         /|    /         /|
+---------+ |   +---------+ |
|   RED   | |   |   GOLD  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/ 
    {Pre1}             {Pre2}
"""

RedBoxWithCarrot = """
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|      __________
 /    ||   /|     /         /|
+---------+ |    +---------+ |
|   RED   | |    |   GOLD  | |
|   BOX   | /    |   BOX   | /
+---------+/     +---------+/
"""

RedBoxWithoutCarrot = """
   _________
  |         |
  |         |
  |_________|      __________
 /         /|     /         /|
+---------+ |    +---------+ |
|   RED   | |    |   GOLD  | |
|   BOX   | /    |   BOX   | /
+---------+/     +---------+/
"""

GoldBoxWithCarrot = """
   _________       ____VV____
  |         |     |    VV    |
  |         |     |    VV    |
  |_________|     |____||____|
 /         /|    /     ||   /|
+---------+ |    +---------+ |
|   RED   | |    |   GOLD  | |
|   BOX   | /    |   BOX   | /
+---------+/     +---------+/
"""
RedBoxWithCarrot2 = """
   ___VV____        _________
  |   VV    |      |         |
  |   VV    |      |         |
  |___||____|      |_________|
 /    ||   /|     /         /|
+---------+ |    +---------+ |
|   RED   | |    |   GOLD  | |
|   BOX   | /    |   BOX   | /
+---------+/     +---------+/
"""

print(Boxes)

print(f"{Pre1}, you have a RED box in front of you.")
print(f"{Pre2}, you have a GOLD box in front of you.")
EnterInput = input("Press Enter to continue...")
print("--snip--")
EnterInput = input(f"When {Pre2} has closed their eyes, press Enter...")
print(f"{Pre1} here is the inside of your box:")
time.sleep(1)

if Carrot == 1:
   print(RedBoxWithCarrot)
else:
   print(RedBoxWithoutCarrot)

EnterInput = input("Press Enter to continue...")
print("--snip--")
print('\n' * 100) # Clear the screen by printing several newlines.
print(Pre1 + ', tell ' + Pre2 + ' to open their eyes.')
input('Press Enter to continue...')
print()
print(f"Now both of you want to end up with the box that contains the carrot.")
print("You can lie or tell the truth")
print()
response = ""
time.sleep(3)
print(Pre2 + ', do you want to swap boxes with ' + Pre1 + '? YES/NO')
while True:
   response = input('> ').upper()
   if response == "YES" or response == "NO":
      if response == "YES":
         Pre1, Pre2 = Pre2, Pre1
      break
   else:
      print(Pre2 + ', please enter "YES" or "NO".')

print("HERE ARE THE TWO BOXES:")
Boxes = f"""  
  __________      __________
 /         /|    /         /|
+---------+ |   +---------+ |
|   RED   | |   |   GOLD  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/ 
    {Pre1}             {Pre2}
"""
print(Boxes)
input('Press Enter to reveal the winner...')

if Carrot == 2:
   print(GoldBoxWithCarrot)
else:
   print(RedBoxWithCarrot2)

if Carrot == 1:
   if response == "YES":
      print(f"The winner is {Pre1}")
   else:
      print(f"The winner is {Pre2}")
else:
   if response == "YES":
      print(f"The winner is {Pre2}")
   else:
      print(f"The winner is {Pre1}")
