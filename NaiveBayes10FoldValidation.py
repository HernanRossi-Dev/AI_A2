from os import listdir
from os.path import isfile, join
import re
import math
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
        self.crossValidationSets = [99,199,299,399,499, 599, 699, 799, 899, 999]

    def parseInputFile(self):
        for validationSet in range(0,10):
            validationFileNamesNeg = []
            validationFileNamesPos = []
            positiveFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive')
                         if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive', f))]
            negativeFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative')
                         if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative', f))]
            for file in negativeFiles:
                if str(file[2:3]) == str(validationSet):
                    validationFileNamesNeg.append(file)
                else:
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
            for word in self.dicWordCounts:
                probability = (self.dicWordCounts[word] + 1)/1002
                self.conditionalProbabiltiesNegative[word] = probability


            self.wordCount = 0
            self.dicWordCounts = {'awful':0, 'bad':0, 'boring':0, 'dull':0,
                                     'effective':0, 'enjoyable':0, 'great':0, 'hilarious':0}
            for file in positiveFiles:
                if str(file[2:3]) == str(validationSet):
                    validationFileNamesPos.append(file)
                else:
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
            for word in self.dicWordCounts:
                probability = (self.dicWordCounts[word] +1) / 1002
                self.conditionalProbabiltiesPostive[word] = probability


            self.testPredict(validationFileNamesNeg, validationFileNamesPos, validationSet)


    def startNaiveBayes(self):
        self.parseInputFile()


    def testPredict(self,validationFileNamesNeg,  validationFileNamesPos, iter):
        probNegative = 0
        probPositive = 0
        predictedNegativeCount = 0
        predictedPositiveeCount = 0
        for file in validationFileNamesNeg:
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())
            featureVector = [0,0,0,0,0,0,0,0]
            for i in range(0, len(fileWords)):
                for j in range(0, 8):
                    if fileWords[i].lower() == self.dictionaryWords[j]:
                        featureVector[j] = 1
            for (n, m) in enumerate(self.conditionalProbabiltiesNegative):
                    if probNegative == 0:
                        probNegative = (self.conditionalProbabiltiesNegative[m] ** featureVector[n]) * (
                                (1 - self.conditionalProbabiltiesNegative[m]) ** (1 - featureVector[n]))
                    else:
                        probNegative *= (self.conditionalProbabiltiesNegative[m]**featureVector[n] ) * (
                            (1 -self.conditionalProbabiltiesNegative[m])**(1-featureVector[n]) )
            for (n,m) in enumerate(self.conditionalProbabiltiesPostive):
                    if probPositive == 0:
                        probPositive = (self.conditionalProbabiltiesNegative[m] ** featureVector[n]) * (
                                (1 - self.conditionalProbabiltiesNegative[m]) ** (1 - featureVector[n]))
                    else:
                        probPositive *= (self.conditionalProbabiltiesPostive[m]**featureVector[n] ) * (
                            (1 -self.conditionalProbabiltiesPostive[m])**(1-featureVector[n]) )

            if probNegative > probPositive:
                    predictedNegativeCount +=1
        print('Predicted ', predictedNegativeCount, ' files were negative when 1000 were actually negative')
        probNegative = 0
        probPositive = 0
        for file in validationFileNamesPos:
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(0, len(fileWords)):
                for j in range(0, 8):
                    if fileWords[i].lower() == self.dictionaryWords[j]:
                        featureVector[j] = 1
            for (n, m) in enumerate(self.conditionalProbabiltiesNegative):
                if probNegative == 0:
                    probNegative = (self.conditionalProbabiltiesNegative[m] ** featureVector[n]) * (
                            (1 - self.conditionalProbabiltiesNegative[m]) ** (1 - featureVector[n]))
                else:
                    probNegative *= (self.conditionalProbabiltiesNegative[m] ** featureVector[n]) * (
                            (1 - self.conditionalProbabiltiesNegative[m]) ** (1 - featureVector[n]))
            for (n, m) in enumerate(self.conditionalProbabiltiesPostive):
                if probPositive == 0:
                    probPositive = (self.conditionalProbabiltiesNegative[m] ** featureVector[n]) * (
                            (1 - self.conditionalProbabiltiesNegative[m]) ** (1 - featureVector[n]))
                else:
                    probPositive *= (self.conditionalProbabiltiesPostive[m] ** featureVector[n]) * (
                            (1 - self.conditionalProbabiltiesPostive[m]) ** (1 - featureVector[n]))
            if probPositive > probNegative:
                predictedPositiveeCount += 1
        print('Iteration: ', iter)
        print('Predicted ', predictedPositiveeCount, ' files were positive when 1000 were actually positive')
        print('')
startBayes = NaiveBayes()
startBayes.startNaiveBayes()