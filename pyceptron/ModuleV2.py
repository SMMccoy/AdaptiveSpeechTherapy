import random
import string

SPLIT = .02
BASE = -.125
vowels = ["a", "e", "i", "o", "u"]
hardletters = ["x", "y", "q", "z"]
LEARNING_MULTIPLIER = 2.5
LEARNING_TURNS = 25

def calculate_difficulty(word):
    vlist = 0
    hlist = 0
    worldLength = len(word) * 1.5
    for letter in word:
        if letter in vowels:
            vlist += .25
        if letter in hardletters:
            hlist += .5

    return worldLength + vlist + hlist

class Node:
    def __init__(self):
        self.weight = (random.random() - .5) * 2
        self.value = 0

    def reset(self):
        self.value = 0


class Perceptron:
    def __init__(self, nodes, learningRate, bias):
        self.nodeAmount = nodes
        self.learningRate = learningRate * LEARNING_MULTIPLIER
        self.learned = 0
        self.is_learning = True
        self.bias = bias
        self.biasNode = Node()
        self.biasNode.value = self.bias
        self.nodeList = {}
        for i in range(nodes):
            self.nodeList[i] = Node()

    def learn(self, word, gotRight):
        if self.is_learning and self.learned < LEARNING_TURNS:
            self.learned += 1
        elif self.is_learning:
            self.is_learning = False
            self.learningRate /= LEARNING_MULTIPLIER
            print("ALL DONE | Learning period is done")

        self.reset()
        i = 0
        for character in word:
            i += 1
            position = self.get_letter_position(i, character)
            node = self.nodeList[position]
            node.value = 1
        result = self.get_weighted_sum()

        if result > 0:
            result = 1
        else:
            result = 0
        expected = 0
        if gotRight:
            expected = 1

        error = expected - result
        if error != 0:
            self.propagate(error)
        else:
            #self.propagate(.1)
            pass

    def input(self, word):
        self.reset()
        i = 0
        for character in word:
            i += 1
            position = self.get_letter_position(i, character)
            node = self.nodeList[position]
            node.value = 1
        sum = self.get_weighted_sum()
        return sum > 0

    def get_weighted_sum(self):
        sum = 0
        for node in self.nodeList.values():
            sum += (node.value * node.weight)

        sum += self.biasNode.value * self.biasNode.weight
        # print(sum)
        sum /= self.nodeAmount + 1
        return sum

    def propagate(self, error):
        for node in self.nodeList.values():
            node.weight += error * node.value * self.learningRate
        self.biasNode.weight += error * self.biasNode.value * self.learningRate

    def get_letter_position(self, number, letter):
        return string.ascii_lowercase.index(str.lower(letter)) + ((number - 1) * 26)

    def reset(self):
        for node in self.nodeList.values():
            node.reset()
        self.biasNode.reset()
