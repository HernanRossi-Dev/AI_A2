from Player import Player
from RollDice import RollDice
import random

class TwoPlayerCashGame:
    def __init__(self):
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
        self.chanceCards = {0: 'Advance to Go', 1: 'Advance to Illinois Ave', 2: 'Advance to St.Charles Place',
                            3: 'Advance to nearest Utility',
                            4: 'Advance to nearest Railroad', 5: 'Bank pay\'s you $50', 6: 'Get out of Jail Free',
                            7: 'Go Back 3 Spaces',
                            8: 'Go to Jail', 9: 'Repairs', 10: 'Pay $15', 11: 'Go to Reading Railroad',
                            12: 'Go to Boardwalk', 13: 'Collect $150',
                            14: 'Collect $100'}
        self.communityChestCards = {0: 'Advance to Go', 1: 'Collect $200', 2: 'Pay $50', 3: 'Get $50',
                                    4: 'Get out of Jail free', 5: 'Go to Jail', 6: 'Get $50', 7: 'Get $100',
                                    8: 'Get $20', 9: 'Get $10 x #players', 10: 'Get $100', 11: 'Pay $150',
                                    12: 'Get $25', 13: 'Pay $40 x #houses & $115 X #hotels',
                                    14: 'Get $10', 15: 'Get $100'}
        self.chanceLocations = [7, 22, 36]
        self.communityChestLocations = [2, 17, 33]
        self.chanceLocations = [7, 22, 36]
        self.communityChestLocations = [2, 17, 33]
        self.goToJailLocation = 30
        self.goLocation = 0
        self.electricCompanyLocation = 12
        self.waterWorksLocation = 28
        self.jailLocation = 10

    def drawChanceCard(self, player):
        drawCard = random.random()
        if drawCard <= 0.0624:
            print('Chance: Go to Go Collect $200 Player ' + str(player.ID))
            player.location = 0
            player.cash += 200
        elif drawCard <= 0.125:
            # print('Chance card: Go to Illinois Avenue')
            print('Chance: Go to Illinois Avenue Player ' + str(player.ID))
            player.location = 24
        elif drawCard <= 0.1875:
            # print('Chance card: Go to St.Charles Place')
            print('Chance: Go to St.Charles Place Player ' + str(player.ID))
            player.location = 11
        elif drawCard <= 0.25:
            # print('Chance card: Go to nearest Utility')
            print('Chance: Go to nearest Utility Player ' + str(player.ID))
            if player.location <= 12:
                player.location = self.electricCompanyLocation
            elif player.location <= 28:
                player.location = self.waterWorksLocation
            else:
                player.location = self.electricCompanyLocation
        elif drawCard <= 0.3125:
            # print('Chance card: Go to nearest Railroad')
            print('Chance: Go to nearest railroad Player ' + str(player.ID))
            if player.location <= 5:
                player.location = 5
            elif player.location <= 15:
                player.location = 15
            elif player.location <= 25:
                player.location = 25
            elif player.location <= 35:
                player.location = 35
            else:
                player.location = 5
        elif drawCard <= 0.375:
            print('Chance: collect $50 Player ' + str(player.ID))
            player.cash +=50
        elif drawCard <= 0.4375:
            # get out of jail free
            pass
        elif drawCard <= 0.5:
            # print('Chance card: Go back 3 space')
            print('Chance: Go back 3 spaces Player ' + str(player.ID))
            player.location -=3
        elif drawCard <= 0.5625:
            # print('Chance card: Go to Jail')
            print('Chance: Go to Jail Player ' + str(player.ID))
            player.location = 10
            player.inJail = True
        elif drawCard <= 0.625:
            #for each house pay 25 for each hotel pay 100
            pass
        elif drawCard <= 0.75:
            print('Chance: pay $15 Player ' + str(player.ID))
            player.cash -= 15
            pass
        elif drawCard <= 0.8125:
            # print('Chance card: Go to Reading Railroad')
            print('Chance: Go to Reading Railroad Player ' + str(player.ID))
            player.location = 5
        elif drawCard <= 0.875:
            # print('Chance card: Go to BoardWalk')
            print('Chance: Go to Boardwalk Player ' + str(player.ID))
            player.location = 39
        elif drawCard <= 0.9375:
            # collect 150
            print('Chance: Go collect $150 Player ' + str(player.ID))
            player.cash += 150
        elif drawCard <= 1:
            # collect 100
            print('Chance: Go collect $100 Player ' + str(player.ID))
            player.cash += 100
        else:
            pass

    def communityChestCard(self, player):
        drawCard = random.random()
        if drawCard <= 0.0626:
            print('Community Chest: Go to Go Player ' + str(player.ID))
            player.location = 0
            player.cash += 200
        elif drawCard <= 0.125:
            print('Community Chest: Go to Jail Player ' + str(player.ID))
            player.location = 10
            player.inJail = True
        elif drawCard <= 0.1875:
            # Collect $200
            print('Community Chest: collect $200 Player ' + str(player.ID))
            player.cash += 200
        elif drawCard <= 0.25:
            print('Community Chest: pay $50 Player ' + str(player.ID))
            player.cash -= 50
        elif drawCard <= 0.3125:
            # Get 50
            print('Community Chest: collect $50 Player ' + str(player.ID))
            player.cash += 50
        elif drawCard <= 0.375:
            # Get out of jail free
            pass
        elif drawCard <= 0.4375:
            print('Community Chest: collect $50 Player ' + str(player.ID))
            player.cash += 50
        elif drawCard <= 0.5:
            print('Community Chest: collect $100 Player ' + str(player.ID))
            player.cash += 100
        elif drawCard <= 0.5625:
            print('Community Chest: collect $20 Player ' + str(player.ID))
            player.cash += 20
        elif drawCard <= 0.625:
            print('Community Chest: collect $10 Player ' + str(player.ID))
            player.cash += 10
        elif drawCard <= 0.6875:
            print('Community Chest: collect $100 Player ' + str(player.ID))
            player.cash += 100
        elif drawCard <= 0.75:
            print('Community Chest: pay $150 Player ' + str(player.ID))
            player.cash -= 150
        elif drawCard <= 0.8125:
            print('Community Chest: collect $25 Player ' + str(player.ID))
            player.cash += 25
        elif drawCard <= 0.875:
            # Pay 40 X houses and 150 X hotels
            pass
        elif drawCard <= 0.9375:
            print('Community Chest: collect $10 Player ' + str(player.ID))
            player.cash += 10
        elif drawCard <= 1:
            print('Community Chest: collect $100 Player ' + str(player.ID))
            player.cash += 100
        else:
            pass



    def takeTurn(self, player):
        # print('\nStarting new turn')
        if player.inJailNonDoubleRolls == 3:
            player.inJail = False
            player.cash -= 50
            if player.cash <= 0:
                player.tryToMortgageProperty(self.propertyOwner)
            player.inJailNonDoubleRolls = 0
        rollDice = RollDice(player.inJail)
        rollDice.rollDice()
        if player.inJail:
            print('Player ' + str(player.ID) + ' is in Jail')

            if rollDice.leaveJail:
                player.inJail = False
                player.inJailNonDoubleRolls = 0
                player.location = 10
            else:
                player.inJailNonDoubleRolls += 1
                return
        currentRoll = rollDice.sum
        if currentRoll == -1:
            #  go to jail
            print('Player ' + str(player.ID) + ' is going to jail for speeding')
            player.location = 10
            player.inJail = True
        elif player.location + currentRoll > 39:
            # loop through the positions if we pass go on this turn
            while player.location  < 40:
                player.location += 1
                currentRoll -= 1
                player.location = 0
        player.location += currentRoll
        if player.location  == 30:
            # print('Go to jail')
            player.location = 10
            player.inJail = True
        elif player.location == 4:
            player.cash -= 100
            if player.cash <= 0:
                player.tryToMortgageProperty(self.propertyOwner)
        elif player.location == 38:
            player.cash -= 200
            if player.cash <= 0:
                player.tryToMortgageProperty(self.propertyOwner)
        elif player.location == 7 or player.location  == 22 or player.location  == 36:
            #     Draw chance cards
            self.drawChanceCard(player)
        elif player.location  == 2 or player.location  == 17 or player.location  == 33:
            #     Draw community chest card
            self.communityChestCard(player)
        if player.cash < 1:
            player.tryToMortgageProperty(self.propertyOwner)


    def simulateCashGame(self):
            playerOne = Player(1)
            playerTwo = Player(2)
            # while playerOne.cash > 0 and playerTwo.cash > 0:
            for i in range(0, 100):
                # take turns playing the game
                self.takeTurn(playerOne)
                print('player One turn ', self.boardLocationsKeyReverse[playerOne.location])
                self.processLocation(playerOne, playerTwo)
                self.takeTurn(playerTwo)
                print('player Two turn ', self.boardLocationsKeyReverse[playerTwo.location])

                self.processLocation(playerOne, playerTwo)
            print(self.propertyOwner, playerOne.cash, playerTwo.cash)

    def processLocation(self, playerOne, playerTwo):
        # check the current owner of the property the player is on, if they own it do nothing if nobody owns it
        # decide to either buy it or do nothing if the other player owns it pay rent
        self.propertyOwner = playerOne.buyRentSell(self.propertyOwner, playerTwo)

newGame = TwoPlayerCashGame()
newGame.simulateCashGame()