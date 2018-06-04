#!usr/bin/Python

# IF YOU ARE INTERESTED IN READING THE CODE ITSELF
# 1. Variables in lowercase
# 2. Methods in camelcase

import math
import operator
import csv
import random

class KNN():

    def __init__(self):
        self.training_set = []
        self.testing_set = []
        self.predictions = []


    def loadDataset(self, filename, split, columns):
        with open(filename, 'rb') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            for x in range(len(dataset) - 1):
                for y in range(columns):
                    dataset[x][y] = float(dataset[x][y])
                if random.random() < split:
                    self.training_set.append(dataset[x])
                else:
                    self.testing_set.append(dataset[x])

    def knn(self, instance, k):
        self.instance = instance
        self.k = k
        # for x in range(len(self.testing_set)):
        #     # self.neighbours = self.getNeighbours(self.training_set, self.instance, self.k) -- [ELIMINATE FOR-LOOP]
        #     self.neighbours = self.getNeighbours(self.training_set, self.testing_set[x], self.k)
        #     self.result = self.getResponse(self.neighbours)
        #     self.predictions.append(self.result)
        #     print('> predicted=' + repr(self.result) + ', actual=' + repr(self.testing_set[x][-1]))
        
        self.neighbours = self.getNeighbours(self.training_set, self.instance, self.k)
        self.result = self.getResponse(self.neighbours)
        self.predictions.append(self.result)
        print('> predicted=' + repr(self.result) )
        # self.accuracy = self.calculateAccuracy(self.testing_set, self.predictions)
        # print('Accuracy: ' + repr(self.accuracy) + '%')
    

    def euclideanDistance(self,instance1, instance2, length):
        distance = 0
        for i in range(length):
            distance += pow((instance1[i] - instance2[i]), 2)
        return math.sqrt(distance)

    def getNeighbours(self,training_set, test_instance, k):
        distances = []
        length = len(test_instance) - 1
        for x in range(len(training_set)):
            distance = self.euclideanDistance(test_instance, training_set[x], length)
            distances.append((training_set[x], distance))
        distances.sort(key=operator.itemgetter(1))
        neighbours = []
        for x in range(k):
            neighbours.append(distances[x][0])
        return neighbours

    #Get a definite string response for nearest neighbour
    #   instead of an (n*m) list
    def getResponse(self,neighbours):
        class_votes = {}
        for x in range(len(neighbours)):
            response = neighbours[x][-1]
            if response in class_votes:
                class_votes[response] += 1
            else:
                class_votes[response] = 1
        sorted_votes = sorted(class_votes.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sorted_votes[0][0]

    #Calculate the accuracy of the algorithm
    def calculateAccuracy(self,testing_set, predictions):
        correct = 0
        for x in range(len(testing_set)):
            if testing_set[x][-1] == predictions[x]:
                correct += 1
        return (correct / float(len(testing_set))) * 100.0




#Test 1  Euclidean Distance -- Test Passed

# data1 = [2,2,2,'Brian']
# data2 = [4,4,4,'Not Brian']
# distance = euclideanDistance(data1, data2, 3)
# print('Distance: {}'.format(distance))


#Test 2 -- Getting Neighbours  -- Test Passed

# train_set = [[2, 2, 2, 'a'],[4, 4, 4, 'b']]
# test_instance =[1, 3, 4]
# k = 1
# neighbours = getNeighbours(train_set, test_instance, k)
# print(neighbours)


#Test 3 -- Getting String Responses --Test Passed

# neighbours = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
# response = getResponse(neighbours)
# print(response)

#Test 4 -- Calculating Accuracy

# testing_set = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
# predictions = ['a', 'a', 'a']
# accuracy = calculateAccuracy(testing_set, predictions)
# print("The accuracy be : {}".format(accuracy))




