# My answer
import random
class Dice:
    def roll(self):
        diceValue = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6
        }
        return random.randint(diceValue, diceValue)


# Mosh's Answer
class Dice2:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice2()
print(dice.roll())
