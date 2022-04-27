import random
import time

i1 = int(input('How many people are playing the game?\n'))

players = []

for x in range(i1):
  players.append(x + 1)

while len(players) != 1:
  num = random.choice(players)
  time.sleep(1)
  print("Players remaining:")
  for x in players:
    print("Player " + str(x))
  print("Player " + str(num) + ", you have the gun!")
  i2 = int(input("Who do you want to target the gun to? There are " + str(len(players)) +         " players\n"))
  exists = i2 in players
  if i2 == num:
    rand = random.randint(1,6)
    if rand == 1:
      print("you shot yourself and died nicee")
      players.remove(num)
    else:
      print("You aimed the gun at yourself and shot but luckily, there was no bullet.")
  elif exists == False:
    print("You can't kill a dead player u idiot")
  else:
    print("You are dueling " + str(i2))
    time.sleep(1)
    rand2 = random.randint(1,6)
    dueling = True
    rounds = 0
    while dueling:
      rando1 = random.randint(1,6)
      if rando1 == 1 or rounds == 6:
        time.sleep(1)
        print("Player " + str(num) + " shot and killed " + str(i2) + "!")
        players.remove(i2)
        dueling = False
        break
      else:
        time.sleep(2)
        print("Player " + str(num) + " shot but there was no bullet :/")
        rounds = rounds + 1
        rando2 = random.randint(1,6)
        if rando2 == 1 or rounds == 6:
          print("Player " + str(i2) + " shot and killed player " + str(num) + "!")
          players.remove(num)
          dueling = False
          break
        else:
          time.sleep(2)
          print("Player " + str(i2) + " shot but there was no bullet :/")
          rounds = rounds + 1
print("GG " + str(players[0]) + ", you won!")
