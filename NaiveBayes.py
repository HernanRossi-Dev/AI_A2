from os import listdir
from os.path import isfile, join
import re
class NaiveBayes:

    def __init__(self):
        self.binaryVector = [0, 0, 0, 0, 0, 0, 0, 0]
        self.dictionaryWords = ['Awful', 'Bad', 'Boring', 'Dull',
                                 'Effective', 'Enjoyable', 'Great', 'Hilarious']
        self.dicWordCounts = {'awful':0, 'bad':0, 'boring':0, 'dull':0,
                                 'effective':0, 'enjoyable':0, 'great':0, 'hilarious':0}
        self.wordCount = 0

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
            print(word, ' appeared ', self.dicWordCounts[word], ' times with a probability of ' , probability)
        self.wordCount = 0
        self.dicWordCounts = {'awful':0, 'bad':0, 'boring':0, 'dull':0,
                                 'effective':0, 'enjoyable':0, 'great':0, 'hilarious':0}
        for file in positiveFiles:
            location = 'C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive\\' + file
            readFile = open(location, 'r')
            fileWords = re.findall(r"[\w]+", readFile.read())
            for i in range(0, len(fileWords)):
                self.wordCount += 1
                if fileWords[i].lower() in self.dicWordCounts:
                    # print('Word found ', fileWords[i].lower())
                    self.dicWordCounts[fileWords[i].lower()] += 1
        print('Positive Words')
        print('Word count: ', self.wordCount)
        for word in self.dicWordCounts:
            probability = self.dicWordCounts[word] / self.wordCount
            print(word, ' appeared ', self.dicWordCounts[word], ' times with a probability of ', probability)

    def startNaiveBayes(self):
        self.parseInputFile()


startBayes = NaiveBayes()
startBayes.startNaiveBayes()