from RollDice import RollDice
import random
class assignmentTwoAI:

    def __init__(self):
        self.boardLocations = {'Go': 0, 'Mediterranean Avenue': 1, 'Community Chest 1': 2, 'Baltic Avenue':3, 'Income Tax': 4,
                               'Reading Railroad':5, 'Oriental Avenue': 6, 'Chance 1': 7, 'Vermont Avenue': 8, 'Connecticut Avenue': 9,
                               'Just Visiting': 10, ' ST.Charles Place': 11, 'Electric Company': 12, 'States Avenue': 13, 'Virginia Avenue': 14,
                               'Pennsylvania Railroad': 15,
                               'St.James Place': 16, 'Community Chest 2': 17, 'Tennessee Avenue': 18, 'New York Avenue': 19, 'Free Parking': 20,
                               'Kentucky Avenue': 21, 'Chance 2': 22, 'Indiana Avenue': 23, 'Illinois Avenue': 24, 'B & O Railroad': 25,
                               'Atlantic Avenue': 26, 'Ventnor Avenue': 27, 'Water Works': 28, 'Marvin Gardens': 29, 'In Jail': 30,
                               'Pacific Avenue': 31, 'North Carolina Avenue': 32, 'Community Chest 3': 33, 'Pennsylvania Avenue': 34,
                               'Short Line': 35, 'Chance 3': 36, 'Park Place': 37, 'Luxury Tax': 38, 'Boardwalk': 39
                               }
        self.boardLocationsKeyReverse = {0:'Go', 1:'Mediterranean Avenue', 2:'Community Chest 1', 3:'Baltic Avenue', 4:'Income Tax',
                               5:'Reading Railroad', 6:'Oriental Avenue', 7:'Chance 1', 8:'Vermont Avenue', 9:'Connecticut Avenue',
                               10:'Just Visiting Jail / in Jail', 11:'ST.Charles Place', 12:'Electric Company', 13:'States Avenue', 14:'Virginia Avenue',
                               15:'Pennsylvania Railroad',
                               16:'St.James Place', 17:'Community Chest 2', 18:'Tennessee Avenue', 19:'New York Avenue', 20:'Free Parking',
                               21:'Kentucky Avenue', 22:'Chance 2', 23:'Indiana Avenue', 24:'Illinois Avenue', 25:'B & O Railroad',
                               26:'Atlantic Avenue', 27:'Ventnor Avenue', 28:'Water Works', 29:'Marvin Gardens', 30:'Go to Jail',
                               31:'Pacific Avenue', 32:'North Carolina Avenue', 33:'Community Chest 3', 34:'Pennsylvania Avenue',
                               35:'Short Line', 36:'Chance 3', 37:'Park Place', 38:'Luxury Tax', 39:'Boardwalk'
                               }

        self.boardLocationVisitedCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.boardNumberRep = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
                               31,32,33,34,35,36,37,38,39]
        self.currentPosition = 0
        self.chanceCards = {0:'Advance to Go', 1:'Advance to Illinois Ave', 2: 'Advance to St.Charles Place', 3:'Advance to nearest Utility',
                            4:'Advance to nearest Railroad', 5:'Bank pay\'s you $50', 6:'Get out of Jail Free', 7:'Go Back 3 Spaces',
                            8:'Go to Jail', 9:'Repairs', 10:'Pay $15', 11:'Go to Reading Railroad', 12:'Go to Boardwalk', 13:'Collect $150',
                            14:'Collect $100'}
        self.communityChestCards = {0:'Advance to Go', 1:'Collect $200', 2: 'Pay $50', 3:'Get $50',
                            4:'Get out of Jail free', 5:'Go to Jail', 6:'Get $50', 7:'Get $100',
                            8:'Get $20', 9:'Get $10 x #players', 10:'Get $100', 11:'Pay $150', 12:'Get $25', 13:'Pay $40 x #houses & $115 X #hotels',
                            14:'Get $10', 15: 'Get $100'}
        self.chanceLocations = [7, 22, 36]
        self.communityChestLocations = [2, 17, 33]
        self.goToJailLocation = 30
        self.goLocation = 0
        self.electricCompanyLocation = 12
        self.waterWorksLocation = 28
        self.jailLocation = 10
        self.jailNonDoubleRollCount = 0
        self.inJail = False

    def runProgram(self):
        totalLocationVisitCounts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(0,1001):
            self.boardLocationVisitedCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            updateCounts = self.startGame()
            for j in range(0,40):
                totalLocationVisitCounts[j] += updateCounts[j]
        print(totalLocationVisitCounts)
        sumTotalVisits = 0
        for i in range(0, 40):
            sumTotalVisits += totalLocationVisitCounts[i]

        for i in range(0, 40):
            location = self.boardLocationsKeyReverse[i]
            visited = totalLocationVisitCounts[i]
            visitedPercentage = visited/sumTotalVisits
            print(location , " was visited ", visited, ' times, with a probability of ', visitedPercentage)


    def startGame(self):
        for i in range(0,100):
            # print('\nStarting new turn')
            if self.jailNonDoubleRollCount == 3:
                self.inJail = False
            rollDice = RollDice(self.inJail)
            rollDice.rollDice()
            if self.inJail:
                if rollDice.leaveJail:
                    self.inJail = False
                    self.currentPosition = 10
                else:
                    self.jailNonDoubleRollCount +=1
                    continue
            currentRoll = rollDice.sum
            if currentRoll == -1:
            #     go to jail
                self.currentPosition = 10
                self.inJail = True
            elif self.currentPosition + currentRoll > 39:
                # loop through the positions if we pass go on this turn
                while self.currentPosition < 40:
                    self.currentPosition += 1
                    currentRoll -=1
                self.currentPosition = 0
            self.currentPosition += currentRoll
            if self.currentPosition == 30:
                # print('Go to jail')
                self.boardLocationVisitedCount[self.currentPosition] += 1
                self.currentPosition = 10
                self.inJail = True
            elif self.currentPosition == 7 or self.currentPosition == 22 or self.currentPosition == 36:
            #     Draw chance cards
                self.drawChanceCard()
            elif self.currentPosition == 2 or self.currentPosition == 17 or self.currentPosition == 33:
                #     Draw community chest card
                self.communityChestCard()
            self.boardLocationVisitedCount[self.currentPosition] +=1

        return self.boardLocationVisitedCount


    def drawChanceCard(self):
        drawCard = random.random()
        if drawCard <= 0.0625:
            self.boardLocationVisitedCount[self.currentPosition] += 1
            # print('Chance card: Go to Go')
            self.currentPosition = 0
        elif drawCard <= 0.125:
            self.boardLocationVisitedCount[self.currentPosition] += 1
            # print('Chance card: Go to Illinois Avenue')
            self.currentPosition = 24
        elif drawCard <= 0.1875:
            # print('Chance card: Go to St.Charles Place')
            self.currentPosition = 11
        elif drawCard <= 0.25:
            # print('Chance card: Go to nearest Utility')
            self.boardLocationVisitedCount[self.currentPosition] += 1
            if self.currentPosition <= 12:
                self.currentPosition = self.electricCompanyLocation
            elif self.currentPosition <= 28:
                self.currentPosition = self.waterWorksLocation
            else:
                self.currentPosition = self.electricCompanyLocation
        elif drawCard <= 0.3125:
            self.boardLocationVisitedCount[self.currentPosition] += 1
            # print('Chance card: Go to nearest Railroad')
            if self.currentPosition <= 5:
                self.currentPosition = 5
            elif self.currentPosition <= 15:
                self.currentPosition = 15
            elif self.currentPosition <= 25:
                self.currentPosition = 25
            elif self.currentPosition <= 35:
                self.currentPosition = 35
            else:
                self.currentPosition = 5
        elif drawCard <= 0.4375:
            pass
        elif drawCard <= 0.5:
            self.boardLocationVisitedCount[self.currentPosition] += 1
            # print('Chance card: Go back 3 space')
            self.currentPosition -=3
        elif drawCard <= 0.5625:
            # print('Chance card: Go to Jail')
            self.currentPosition = 10
        elif drawCard <= 0.75:
            pass
        elif drawCard <= 0.8125:
            # print('Chance card: Go to Reading Railroad')
            self.boardLocationVisitedCount[self.currentPosition] += 1
            self.currentPosition = 5
        elif drawCard <= 0.875:
            # print('Chance card: Go to BoardWalk')
            self.boardLocationVisitedCount[self.currentPosition] += 1
            self.currentPosition = 39
        else:
            pass

    def communityChestCard(self):
        drawCard = random.random()
        if drawCard <= 0.0626:
            self.boardLocationVisitedCount[self.currentPosition] += 1
            # print('Chance card: Go to Go')
            self.currentPosition = 0
        elif drawCard <= 0.125:
            self.boardLocationVisitedCount[self.currentPosition] += 1
            # print('Chance card: Go to Jail')
            self.currentPosition = 10
        else:
            pass

startExp = assignmentTwoAI()
startExp.runProgram()
