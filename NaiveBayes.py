from os import listdir
from os.path import isfile, join
import re
import math
import random
class NaiveBayes:

    def __init__(self):
        self.binaryVector = [0, 0, 0, 0, 0, 0, 0, 0]
        self.dictionaryWords = ['awful', 'bad', 'boring', 'dull',
                                 'effective', 'enjoyable', 'great', 'hilarious']
        self.dicWordCounts = {'awful':0, 'bad':0, 'boring':0, 'dull':0,
                                 'effective':0, 'enjoyable':0, 'great':0, 'hilarious':0}
        self.wordCount = 0
        self.conditionalProbabiltiesPostive = {'awful':0.0, 'bad':0.0, 'boring':0.0, 'dull':0.0,
                                 'effective':0.0, 'enjoyable':0.0, 'great':0.0, 'hilarious':0.0}
        self.conditionalProbabiltiesNegative = {'awful':0.0, 'bad':0.0, 'boring':0.0, 'dull':0.0,
                                 'effective':0.0, 'enjoyable':0.0, 'great':0.0, 'hilarious':0.0}
    def parseInputFile(self):
        positiveFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive')
                     if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive', f))]
        negativeFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative')
                     if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative', f))]
        for file in negativeFiles:
            dictionaryWordCurrent = ['awful', 'bad', 'boring', 'dull',
                               'effective', 'enjoyable', 'great', 'hilarious']
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())
            for i in range(0, len(fileWords)):
                for word in dictionaryWordCurrent:
                    if fileWords[i].lower() == word:
                        self.dicWordCounts[word] += 1
                        dictionaryWordCurrent.remove(word)
        print('Negative Reviews')
        print(self.dicWordCounts)
        for word in self.dicWordCounts:
            probability = (self.dicWordCounts[word] + 1)/1002
            self.conditionalProbabiltiesNegative[word] = probability
        print(self.conditionalProbabiltiesNegative)


        self.wordCount = 0
        self.dicWordCounts = {'awful':0, 'bad':0, 'boring':0, 'dull':0,
                                 'effective':0, 'enjoyable':0, 'great':0, 'hilarious':0}
        for file in positiveFiles:
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())
            dictionaryWordCurrent = ['awful', 'bad', 'boring', 'dull',
                                     'effective', 'enjoyable', 'great', 'hilarious']
            for i in range(0, len(fileWords)):
                for word in dictionaryWordCurrent:
                    if fileWords[i].lower() == word:
                        self.dicWordCounts[word] += 1
                        dictionaryWordCurrent.remove(word)
        print('Positive Words')
        print(self.dicWordCounts)
        for word in self.dicWordCounts:
            probability = (self.dicWordCounts[word] +1) / 1002
            self.conditionalProbabiltiesPostive[word] = probability
        print(self.conditionalProbabiltiesPostive)


    def startNaiveBayes(self):
        self.parseInputFile()
        self.generateReviewFromModel()
        self.testPredict()

    def testPredict(self):
        positiveFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive')
                         if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive', f))]
        negativeFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative')
                         if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative', f))]
        probNegative = math.log(0.5)
        probPositive = math.log(0.5)
        predictedNegativeCount = 0
        predictedPositiveCount = 0
        count = 0
        for file in negativeFiles:
                location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative\\' + file
                readFile = open(location, 'r')
                fileWords = re.findall(r"[\w]+", readFile.read())
                featureVector = [0,0,0,0,0,0,0,0]
                for i in range(0, len(fileWords)):
                    for j in range(0, 8):
                        if fileWords[i].lower() == self.dictionaryWords[j]:
                            featureVector[j] = 1
                for (n,m) in enumerate(self.conditionalProbabiltiesNegative):
                    if featureVector[n] == 1:
                        probNegative += math.log(self.conditionalProbabiltiesNegative[m])
                    else:
                        probNegative += math.log(1-self.conditionalProbabiltiesNegative[m])
                for (n,m) in enumerate(self.conditionalProbabiltiesPostive):
                    if featureVector[n] == 1:
                        probPositive += math.log(self.conditionalProbabiltiesPostive[m])
                    else:
                        probPositive += math.log(1 - self.conditionalProbabiltiesPostive[m])
                if probNegative > probPositive:
                    predictedNegativeCount +=1
        print('Predicted ', predictedNegativeCount, ' files were negative when 1000 were actually negative')


        probNegative = math.log(0.5)
        probPositive = math.log(0.5)
        for file in positiveFiles:
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(0, len(fileWords)):
                for j in range(0, 8):
                    if fileWords[i].lower() == self.dictionaryWords[j]:
                        featureVector[j] = 1
            for (n, m) in enumerate(self.conditionalProbabiltiesNegative):
                if featureVector[n] == 1:
                    probNegative += math.log(self.conditionalProbabiltiesNegative[m])
                else:
                    probNegative += math.log(1 - self.conditionalProbabiltiesNegative[m])
            for (n, m) in enumerate(self.conditionalProbabiltiesPostive):
                if featureVector[n] == 1:
                    probPositive += math.log(self.conditionalProbabiltiesPostive[m])
                else:
                    probPositive += math.log(1 - self.conditionalProbabiltiesPostive[m])
            if probPositive > probNegative:
                predictedPositiveCount += 1
        print('Predicted ', predictedPositiveCount, ' files were positive when 1000 were actually positive')

    def generateReviewFromModel(self):
        # generate 5 negative reviews
        for i in range(0,5):
            currentReview = ''
            for index, word in enumerate(self.conditionalProbabiltiesNegative):
                ranNum = random.random()
                wordProb = self.conditionalProbabiltiesNegative[word]
                wordNoPresProb = 1 - wordProb
                # print(word, wordProb, wordNoPresProb, ranNum)
                if wordProb > ranNum:
                    currentReview += word + ' '
                elif wordNoPresProb < ranNum:
                    currentReview += word + ' '
            print('Negative Review ', i)
            print(currentReview)
            print('')
        for i in range(0,5):
            currentReview = ''
            for index, word in enumerate(self.conditionalProbabiltiesPostive):
                ranNum = random.random()
                wordProb = self.conditionalProbabiltiesPostive[word]
                wordNoPresProb = 1 - wordProb
                # print(word, wordProb, wordNoPresProb, ranNum)
                if wordProb > ranNum:
                    currentReview += word + ' '
                elif wordNoPresProb < ranNum:
                    currentReview += word + ' '
            print('Positive Review ', i)
            print(currentReview)
            print('')

startBayes = NaiveBayes()
startBayes.startNaiveBayes()