from os import listdir
from os.path import isfile, join
import re
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
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())

            for i in range(0, len(fileWords)):
                self.wordCount += 1
                if fileWords[i].lower() in self.dicWordCounts:
                    # print('Word found ', fileWords[i].lower())
                    self.dicWordCounts[fileWords[i].lower()] += 1
        print('Negative Reviews')
        print('Word count: ', self.wordCount)
        print(self.dicWordCounts)
        for word in self.dicWordCounts:
            probability = self.dicWordCounts[word]/self.wordCount
            self.conditionalProbabiltiesNegative[word] = probability/0.5
            # print(word, ' appeared ', self.dicWordCounts[word], ' P( word And class)= ', probability , ' P(word | class) = ', probability/ 0.5)
        # print(self.conditionalProbabiltiesNegative)


        self.wordCount = 0
        self.dicWordCounts = {'awful':0, 'bad':0, 'boring':0, 'dull':0,
                                 'effective':0, 'enjoyable':0, 'great':0, 'hilarious':0}
        for file in positiveFiles:
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())
            for i in range(0, len(fileWords)):
                self.wordCount += 1
                for dicWord in self.dictionaryWords:
                    if fileWords[i].lower() == dicWord:
                        # print('Word found ', fileWords[i].lower())
                        self.dicWordCounts[fileWords[i].lower()] += 1
        print('Positive Words')
        print('Word count: ', self.wordCount)
        print(self.dicWordCounts)
        for word in self.dicWordCounts:
            probability = self.dicWordCounts[word] / self.wordCount
            self.conditionalProbabiltiesPostive[word] = probability/0.5
            # print(word, ' appeared ', self.dicWordCounts[word], ' P( word And class)= ', probability , ' P(word | class) = ', probability/ 0.5)
        # print(self.conditionalProbabiltiesPostive)


    def startNaiveBayes(self):
        self.parseInputFile()
        self.testPredict()

    def testPredict(self):
        positiveFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive')
                         if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive', f))]
        negativeFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative')
                         if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative', f))]
        probNegative = 0
        probPositive = 0
        predictedNegativeCount = 0
        predictedPositiveeCount = 0
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
                    # print(n,m)
                    if probNegative == 0:
                        probNegative = (self.conditionalProbabiltiesNegative[m]**featureVector[n] ) * (
                                (1 -self.conditionalProbabiltiesNegative[m])**(1-featureVector[n]) )
                    else:
                        probNegative *= (self.conditionalProbabiltiesNegative[m]**featureVector[n] ) * (
                                (1 -self.conditionalProbabiltiesNegative[m])**(1-featureVector[n]) )

                for (n,m) in enumerate(self.conditionalProbabiltiesPostive):
                    # print(n,m)
                    if probPositive == 0:
                        probPositive = (self.conditionalProbabiltiesPostive[m]**featureVector[n] ) * (
                                (1 -self.conditionalProbabiltiesPostive[m])**(1-featureVector[n]) )
                    else:
                        probPositive *= (self.conditionalProbabiltiesPostive[m]**featureVector[n] ) * (
                                (1 -self.conditionalProbabiltiesPostive[m])**(1-featureVector[n]) )

                if probNegative > probPositive:
                    predictedNegativeCount +=1
        print('Predicted ', predictedNegativeCount, ' files were negative when 1000 were actually negative')
        probNegative = 0
        probPositive = 0
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
                # print(n,m)
                if probNegative == 0:
                    probNegative = (self.conditionalProbabiltiesNegative[m] ** featureVector[n]) * (
                                (1 - self.conditionalProbabiltiesNegative[m]) ** (1 - featureVector[n]))
                else:
                    probNegative *= (self.conditionalProbabiltiesNegative[m] ** featureVector[n]) * (
                                (1 - self.conditionalProbabiltiesNegative[m]) ** (1 - featureVector[n]))

            for (n, m) in enumerate(self.conditionalProbabiltiesPostive):
                # print(n,m)
                if probPositive == 0:
                    probPositive = (self.conditionalProbabiltiesPostive[m] ** featureVector[n]) * (
                                (1 - self.conditionalProbabiltiesPostive[m]) ** (1 - featureVector[n]))
                else:
                    probPositive *= (self.conditionalProbabiltiesPostive[m] ** featureVector[n]) * (
                                (1 - self.conditionalProbabiltiesPostive[m]) ** (1 - featureVector[n]))
            #
            # print('Prob file is negative ', probNegative)
            # print('Porb file is positive ',probPositive)
            if probPositive > probNegative:
                predictedPositiveeCount += 1
        print('Predicted ', predictedPositiveeCount, ' files were positive when 1000 were actually positive')
startBayes = NaiveBayes()
startBayes.startNaiveBayes()