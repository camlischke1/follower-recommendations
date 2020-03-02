'''
 This program will read the ﬁles A16.txt and A1024.txt, which are input matrices representing follower graphs.
 The input ﬁles are formatted using one line per row and spaces between columns (each entry is either 0 or 1). Computes
 recommendations (based on number of two-paths) for each vertex using both matrix multiplication and a new adjacency-list based algorithm.
 This program uses 1-indexing (the ﬁrst row of the matrix corresponds to user 1, not user 0).

LANGUAGE IS PYTHON 3

@author Cam Lischke <lisccd18@wfu.edu>
CSC 222 -- Dr. Ballard
Feb. 17, 2020
'''
import math
import collections
import time

""" This class will represent a Node on the graph. It will store the Node id as an integer and the Node's adjacency list.
# In the adjacency list, the integers represent the id of other nodes to which it is connected.
"""
class Node:
    def __init__(self, id):    # constructor, passes one-index id number
        self.id = id
        self.adList = []            # list of all id's of adjacent nodes
        self.twoPaths = []          # list of all the two paths that this Node has
        self.recommendation = 0
        self.outputEl = []
        self.outputVal = []

    # boolean that checks if the 2-path has already been followed by the user or is the user itself
    def follows(self, check):
        if self.id == check:
            return True
        for i in range(len(self.adList)):
            if self.adList[i] == check:
                return True
        return False

    # finds the mode of the twoPaths list, source: tutorialspoint finding the mode
    def getMode(self):
        temp = sorted(self.twoPaths)
        self.twoPaths = temp
        if len(self.twoPaths) > 0:
            data = collections.Counter(self.twoPaths)             # calculate the frequency of each item
            data_list = dict(data)
            max_value = max(list(data.values()))             # Find the highest frequency
            mode_val = [num for num, freq in data_list.items() if freq == max_value]
            self.recommendation = mode_val[0] + 1


    # this creates the outputted weighted graph
    def tally(self):
        cnt = collections.Counter()
        for id in self.twoPaths:
            cnt[id] += 1
        self.outputEl = list(cnt)
        self.outputVal = list(cnt.values())

        for i in range(len(self.outputEl)):
            self.outputEl[i] += 1
        print("Index " + str(self.id + 1) + ": elements" + str(self.outputEl) + " values" + str(self.outputVal))


""" This method will take the list of all nodes, and using their adjacency lists, will determine all two paths of each Node.
# The destination with the most two-paths will be the recommendation for the source Node to follow.
"""
def findTwoPaths(nodeList):
    # this puts the two paths into each node instances' twopathlist
    for i in range(len(nodeList)):
        current = nodeList[i]
        currentList = current.adList
        for j in range(len(currentList)):
            followedNode = currentList[j]
            followedList = nodeList[followedNode].adList
            for k in range(len(followedList)):
                if not current.follows(followedList[k]):
                    current.twoPaths.append(followedList[k])


""" This function will take the recommendations and print them to separate text files. use 1-indexing (the ﬁrst row of 
    the matrix corresponds to user 1, not user 0); • break ties by choosing the smallest index; • list a 0 recommendation 
    for users who are not connected by a two-path to another user. 
"""
def writeRec(nodeList, filename):
    f = open(filename, 'w')
    for i in range(len(nodeList)):
        f.write(str(nodeList[i].recommendation) + "\n")
    f.close()


""" This function reads an input text file of integers and converts it and returns in matrix representation
#   @return matrix
"""
def read(filename):
    input = ""
    with open(filename, 'r') as file:             #CHANGE FILE NAME HERE
        for line in file:
            if line == '\n':
                break
            else:
                input += line
    temp = input.split()

    # translates the input lines into a matr
    n = int(math.sqrt(len(temp)))
    matrix = [[0 for x in range(n)] for x in range(n)]
    x = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(temp[x])
            x += 1

    return matrix

def main():
    print("================================================================")
    matrix = read('A16.txt')

    # creating adjacency lists for all nodes using the input adjacency matrix
    # initialize all the nodes in the nodeList first
    nodeList = []
    n = len(matrix)
    for i in range(n):
        nodeList.append(Node(i))

    # construct the adjacency lists next
    for i in range(n):
        for j in range(n):
            if (matrix[i][j] > 0):
                nodeList[i].adList.append(j)

    findTwoPaths(nodeList)
    for i in range(len(nodeList)):
        nodeList[i].getMode()
        nodeList[i].tally()

    writeRec(nodeList, 'rec16.txt')

def main2():
    print("================================================================")
    bigMatrix = read('A1024.txt')

    # creating adjacency lists for all nodes using the input adjacency matrix
    # initialize all the nodes in the nodeList first
    nodeList = []
    n = len(bigMatrix)
    for i in range(n):
        nodeList.append(Node(i))

    # construct the adjacency lists next
    for i in range(n):
        for j in range(n):
            if (bigMatrix[i][j] > 0):
                nodeList[i].adList.append(j)           #for some reason this puts the number in everyone's adjacency list

    findTwoPaths(nodeList)
    for i in range(len(nodeList)):
        nodeList[i].getMode()
        nodeList[i].tally()

    writeRec(nodeList, 'rec1024.txt')


if __name__ == "__main__":
    start_time = time.time()
    main()
    main2()
    print("--- %s seconds for adjacency list algorithm---" % (time.time() - start_time))
