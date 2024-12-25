# HEATH POTION

# you can change difficulty by three level 1,2,3.(by assinging the value to the difficulty variable)
import random


health  = 50

difficulty = 1#choose:- 1,2,3)

potion_health = random.randint(25,50) / difficulty


health = int(health + potion_health)

print(health)
