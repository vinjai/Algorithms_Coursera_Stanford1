#!/usr/bin/env python

"""
Download the following text file:

kargerMinCut.txt
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to
200. The first column in the file represents the vertex label, and the particular row (other entries except the first
column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6	155	56
52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices
with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above
graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions.
Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.
But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure
to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write
your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
"""
import time

__author__ = 'Vinayak'

from fileIO import readAsListOfDict,writeSingleToFile
import random
import math

def countKargersMinimumCuts(vertexSet,edgeSet):
    """Run Karger's Minimum Cut Algorithm to return minimum cuts whose edges are specified with edgeSet"""

    trialNumbers = int(math.pow(len(vertexSet),2)*math.log(len(vertexSet),math.e))
    minCuts = math.inf

    for i in range(trialNumbers):
        random.seed(i)
        edgesInGraph = list(edgeSet.copy())
        vertices = list(vertexSet.copy())
        # If possible avoid using random functions in loop because they take most time.
        # So here we use random shuffle instead of using random choice in while loop
        random.shuffle(edgesInGraph)
        deletedNodes = dict()
        while len(vertices) != 2:
            flag=True
            while flag:
                selectEdge=edgesInGraph.pop()
                randomEdge=(deletedNodes[selectEdge[0]] if selectEdge[0] in deletedNodes else selectEdge[0],
                            deletedNodes[selectEdge[1]] if selectEdge[1] in deletedNodes else selectEdge[1])
                if randomEdge[0] != randomEdge[1]:
                    flag = False
            vertices.remove(randomEdge[1])
            deletedNodes[randomEdge[1]]=randomEdge[0]
            for key,value in deletedNodes.items():
                if value == randomEdge[1]:
                    deletedNodes[key]=randomEdge[0]

        for i,e in enumerate(edgesInGraph):
            temp = [e[0],e[1]]
            if e[0] in deletedNodes:
                temp[0]=deletedNodes[e[0]]
            if e[1] in deletedNodes:
                temp[1]=deletedNodes[e[1]]
            edgesInGraph[i] = (temp[0],temp[1])
        edgesInGraph=list(filter(lambda v: v[0]!=v[1],edgesInGraph))
        minCuts = min(minCuts,len(edgesInGraph))

    return minCuts

if __name__=='__main__':
    inputList = readAsListOfDict('_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt','\s+',2,["vertex","neighbours"])
    vertexList=set([ int(item["vertex"]) for item in inputList])
    edgeList = set([ (min(int(item["vertex"]),int(neighbour)),max(int(item["vertex"]),int(neighbour))) for item in
                     inputList for neighbour in item["neighbours"].strip().split('\t') if int(item["vertex"]) != int(
            neighbour) ])
    start = time.time()
    writeSingleToFile('Problem3.txt',countKargersMinimumCuts(vertexList,edgeList))
    end=time.time()
    print(end-start)



