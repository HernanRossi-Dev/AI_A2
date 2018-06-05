import random
class RollDice:
    def __init__(self, inJail):
        self.sum = 0
        self.doubles = False
        self.diceOne = 0
        self.diceTwo = 0
        self.roll = True
        self.inJail = inJail
        self.leaveJail = False

    def rollDice(self):
        rolledDoublesCount = 0
        while self.roll:
            self.assignDiceValues()
            self.sum += self.diceTwo + self.diceOne
            if self.diceOne == self.diceTwo:
                if self.inJail:
                    self.leaveJail = True
                    return
                rolledDoublesCount +=1
                if rolledDoublesCount == 3:
                    self.roll = False
                    self.sum = -1
                else:
                    self.roll = True
            else:
                self.roll = False

    def assignDiceValues(self):
        assignDiceOne = random.random()
        diceOne = 0
        if assignDiceOne <= 0.1666667:
            diceOne = 1
        elif assignDiceOne <= 0.333333:
            diceOne = 2
        elif assignDiceOne <= 0.5:
            diceOne = 3
        elif assignDiceOne <= 0.6666667:
            diceOne = 4
        elif assignDiceOne <= 0.83333333:
            diceOne = 5
        elif assignDiceOne <= 1.0:
            diceOne = 6
        assignDiceTwo = random.random()
        diceTwo = 0
        if assignDiceTwo <= 0.1666667:
            diceTwo = 1
        elif assignDiceTwo <= 0.333333:
            diceTwo = 2
        elif assignDiceTwo <= 0.5:
            diceTwo = 3
        elif assignDiceTwo <= 0.6666667:
            diceTwo = 4
        elif assignDiceTwo <= 0.83333333:
            diceTwo = 5
        elif assignDiceTwo <= 1.0:
            diceTwo = 6
        self.diceOne = diceOne
        self.diceTwo = diceTwo