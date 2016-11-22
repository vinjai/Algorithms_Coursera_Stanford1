#!/usr/bin/env python

"""
Download the following text file:

SCC.txt
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row
indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head
(recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex).
So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge
to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and
to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes,
separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500,
400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds
less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are
400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer
should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may
have to manage memory carefully. The best way to do this depends on your programming language and environment, and we
strongly suggest that you exchange tips for doing this on the discussion forums.
"""

__author__ = 'Vinayak'

from fileIO import readAsListOfDict,writeSingleToFile

def getStronglyConnectedComponents(edgesList):
    """Calculate Strongly connected components and return length of them in list"""

    graph=dict()
    graphRev=dict()
    finishTimes=list()
    for e in edgesList:
        if not e[0] in graph:
            graph[e[0]]={e[1]}
        else:
            graph[e[0]].add(e[1])
        if not e[1] in graphRev:
            graphRev[e[1]]={e[0]}
        else:
            graphRev[e[1]].add(e[0])

    t=0
    exploredNodes=set()
    # Recursive code led to stack overflow
    # def _DFS_on_Rev(i):
    #     nonlocal t
    #     nonlocal exploredNodes
    #     nonlocal finishTimes
    #     nonlocal graphRev
    #
    #     if not i in exploredNodes:
    #         exploredNodes.add(i)
    #         if i in graphRev:
    #             for node in graphRev[i]:
    #                 if node not in exploredNodes:
    #                     _DFS_on_Rev(node)
    #         finishTimes.append(i)
    #         t+=1
    def _DFS_on_Rev(i):
        nonlocal t
        nonlocal exploredNodes
        nonlocal finishTimes
        nonlocal graphRev
        stackDFS=[i]
        finish=list()
        while stackDFS:
            vertex=stackDFS.pop()
            if not vertex in exploredNodes:
                exploredNodes.add(vertex)
                if vertex in graphRev:
                    stackDFS.extend(graphRev[vertex]-exploredNodes)
                finish.append(vertex)
        finishTimes.extend(reversed(finish))

    graphRevKeys=list(graphRev.keys())

    graphRevKeys.sort(reverse=True)

    for vertex in graphRevKeys:
        if not vertex in exploredNodes:
            _DFS_on_Rev(vertex)

    countOfSCC = list()
    exploredNodes=set()
    count=0
    # Recursive code led to stack overflow
    # def _DFS(i):
    #     nonlocal exploredNodes
    #     nonlocal graph
    #     nonlocal count
    #
    #     if not i in exploredNodes:
    #         exploredNodes.add(i)
    #         if i in graph:
    #             for node in graph[i]:
    #                 if node not in exploredNodes:
    #                     _DFS(node)
    #
    #         count+=1

    def _DFS(i):
        nonlocal exploredNodes
        nonlocal graph
        nonlocal count

        stackDFS=[i]
        finish = set()
        while stackDFS:
            vertex=stackDFS.pop()
            if not vertex in exploredNodes:
                exploredNodes.add(vertex)
                if vertex in graph:
                    stackDFS.extend(graph[vertex]-exploredNodes)
                finish.add(vertex)
        count+=len(finish)
    for i in reversed(finishTimes):
        count=0
        if not i in exploredNodes:
            _DFS(i)
        countOfSCC.append(count)
    countOfSCC.sort(reverse=True)

    return countOfSCC



if __name__=="__main__":
    inputList = readAsListOfDict('_410e934e6553ac56409b2cb7096a44aa_SCC.txt','\s+',2,fieldDataList=[int,int])
    writeSingleToFile('Problem4.txt',','.join([str(i) for i in  getStronglyConnectedComponents(inputList)[0:5]]))