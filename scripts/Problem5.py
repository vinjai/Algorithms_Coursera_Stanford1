#!/usr/bin/env python

"""
In this programming problem you'll code up Dijkstra's shortest-path algorithm.

Download the following text file:

dijkstraData.txt
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.
Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge.
For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The
next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length
8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the
corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex,
and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between
a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,
197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these
vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should
be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string
should be in the same order in which the above ten vertices are given. The string should not contain any spaces.
Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's
algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the
heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some
kind of mapping between vertices and their positions in the heap.
"""

__author__ = 'Vinayak'

from fileIO import readAsListOfDict,writeSingleToFile
import heapq

MAX_DIST = 1000000

def runDijkstra(graph, s, nodeList):
    """returns array with shortest part for source vertex s"""

    unexploredNodes=set(nodeList)
    minHeap= [(0,s)] + [ (MAX_DIST,node) for node in nodeList if node != s]
    heapq.heapify(minHeap)
    shortestPath = dict()

    while len(minHeap) != 0:
        min_dist,curr_node = heapq.heappop(minHeap)
        indexHeap= {tup[1]:i  for i,tup in enumerate(minHeap)}
        unexploredNodes.remove(curr_node)
        shortestPath[curr_node]=min_dist
        for edge in graph[curr_node]:
            if edge[0] in unexploredNodes:
                dist,node = minHeap[indexHeap[edge[0]]]
                minHeap[indexHeap[edge[0]]] = (min(dist,min_dist+edge[1]),edge[0])
        heapq.heapify(minHeap)
    return shortestPath


if __name__=="__main__":
    inputList = readAsListOfDict("_dcf1d02570e57d23ab526b1e33ba6f12_dijkstraData.txt",'\s+'
                           ,2,["node","neighbourStr"],[int,str])
    graph = {details["node"]:[tuple(int(x) for x in neighbourDetails.split(',')) for neighbourDetails
                               in details["neighbourStr"].strip().split('\t')] for details in inputList }
    shortestPaths = runDijkstra(graph,1,list(range(1,201)))
    # print(shortestPaths)
    writeSingleToFile("Problem5.txt",",".join([str(shortestPaths[key]) for key in [7,37,59,82,99,115,133,165,188,197]]))