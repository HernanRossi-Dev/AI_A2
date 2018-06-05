import random
class Player:
    def __init__(self, newID):
        self.cash = 500
        self.properties = []
        self.location = 0
        self.inJail = False
        self.inJailNonDoubleRolls = 0
        self.ID = newID
        self.boardLocationsKeyReverse = {0: 'Go', 1: 'Mediterranean Avenue', 2: 'Community Chest 1', 3: 'Baltic Avenue',
                                         4: 'Income Tax',
                                         5: 'Reading Railroad', 6: 'Oriental Avenue', 7: 'Chance 1',
                                         8: 'Vermont Avenue', 9: 'Connecticut Avenue',
                                         10: 'Just Visiting Jail / in Jail', 11: 'ST.Charles Place',
                                         12: 'Electric Company', 13: 'States Avenue', 14: 'Virginia Avenue',
                                         15: 'Pennsylvania Railroad',
                                         16: 'St.James Place', 17: 'Community Chest 2', 18: 'Tennessee Avenue',
                                         19: 'New York Avenue', 20: 'Free Parking',
                                         21: 'Kentucky Avenue', 22: 'Chance 2', 23: 'Indiana Avenue',
                                         24: 'Illinois Avenue', 25: 'B & O Railroad',
                                         26: 'Atlantic Avenue', 27: 'Ventnor Avenue', 28: 'Water Works',
                                         29: 'Marvin Gardens', 30: 'Go to Jail',
                                         31: 'Pacific Avenue', 32: 'North Carolina Avenue', 33: 'Community Chest 3',
                                         34: 'Pennsylvania Avenue',
                                         35: 'Short Line', 36: 'Chance 3', 37: 'Park Place', 38: 'Luxury Tax',
                                         39: 'Boardwalk'
                                         }
        self.propertyOwner = {0: -1, 1: 0, 2: -1, 3: 0, 4: -1,
                              5: 0, 6: 0, 7: -1, 8: 0, 9: 0,
                              10: -1, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
                              16: 0, 17: -1, 18: 0, 19: 0, 20: -1,
                              21: 0, 22: -1, 23: 0, 24: 0, 25: 0,
                              26: 0, 27: 0, 28: 0, 29: 0, 30: -1,
                              31: 0, 32: 0, 33: -1, 34: 0,
                              35: 0, 36: -1, 37: 0, 38: -1, 39: 0
                              }
        self.propertyValues = {0: 0, 1: 60, 2: 0, 3: 60, 4: -200,
                               5: 200, 6: 100, 7: 0, 8: 100, 9: 120,
                               10: 0, 11: 140, 12: 150, 13: 140, 14: 160, 15: 200,
                               16: 180, 17: 0, 18: 180, 19: 200, 20: 0,
                               21: 220, 22: 0, 23: 220, 24: 240, 25: 200,
                               26: 260, 27: 260, 28: 150, 29: 280, 30: 0,
                               31: 300, 32: 300, 33: 0, 34: 320,
                               35: 200, 36: 0, 37: 350, 38: -100, 39: 400
                               }
        self.propertyRents = {0: -1, 1: 2, 2: -1, 3: 4, 4: -1,
                               5: 100, 6: 6, 7: -1, 8: 6, 9: 8,
                               10: -1, 11: 10, 12: 100, 13: 10, 14: 12, 15: 100,
                               16: 14, 17: -1, 18: 14, 19: 16, 20: -1,
                               21: 18, 22: -1, 23: 18, 24: 20, 25: 100,
                               26: 22, 27: 22, 28: 100, 29: 24, 30: -1,
                               31: 26, 32: 26, 33: -1, 34: 28,
                               35: 100, 36: -1, 37: 35, 38: -100, 39: 50
                               }

    # Decide to buy or not or pay rent if it is owned by other player
    def buyRentSell(self, propertyOwners, otherPlayer, turn):
        propertyCost = self.propertyValues[self.location]
        if propertyCost < 0:
            if self.cash + propertyCost < 0:
                propertyOwners = self.tryToMortgageProperty(propertyOwners)
        if propertyOwners[self.location] == 0:
        #     will I buy or not?
            randomChoice = random.random()
            if randomChoice <= 0.75 and propertyCost < self.cash:
                print('Player ' + str(self.ID) + ' buying ' + self.boardLocationsKeyReverse[self.location] + ' for ' + str(propertyCost))
                self.cash = self.cash - propertyCost
                print('Remaining cash ' + str(self.cash))
                propertyOwners[self.location] = self.ID
        elif propertyOwners[self.location] == otherPlayer.ID:
        #     pay rent

            rent = self.propertyRents[self.location] * turn
            print('Player ' + str(self.ID) + ' paying ' + str(rent) + ' in rent ')
            print('Player ' + str(self.ID) + ' has ' + str(self.cash) )
            if self.cash < rent:
                propertyOwners = self.tryToMortgageProperty(propertyOwners)
        return propertyOwners

    # Try to mortgage enough to pay debts if not lose the game
    def tryToMortgageProperty(self, propertyOwners):
        # TODO
        for curProperty in propertyOwners:
            if propertyOwners[curProperty] == self.ID:
                self.cash += self.propertyValues[curProperty]
                propertyOwners[curProperty] = 0
                if self.cash > 0:
                    return propertyOwners

        print('Player ' + str(self.ID) + ' has run out of money and has lost the game')
        exit(0)