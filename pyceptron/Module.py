import random
import string

class Node:
    def __init__(self):
        self.weight = (random.random() - .5) * 2
        self.value = 0

    def reset(self):
        self.value = 0


class Perceptron:
    def __init__(self, nodes, learningRate, bias, super_bias):
        self.learned = 0
        self.nodeAmount = nodes
        self.learningRate = learningRate
        self.is_learning = True
        self.bias = bias
        self.biasNode = Node()
        self.biasNode.value = self.bias
        self.super_bias = super_bias
        self.nodeList = {}
        for i in range(nodes):
            self.nodeList[i] = Node()

    def learn(self, word, gotRight):
        self.reset()
        i = 0
        for character in word:
            i += 1
            position = self.get_letter_position(i, character)
            node = self.nodeList[position]
            node.value = 1
        result = self.get_weighted_sum() + self.super_bias

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
        self.learned += 1

    def input(self, word):
        self.reset()
        i = 0
        for character in word:
            i += 1
            position = self.get_letter_position(i, character)
            node = self.nodeList[position]
            node.value = 1
        sum = self.get_weighted_sum() + self.super_bias
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
