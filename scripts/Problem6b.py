#!/usr/bin/env python

"""
Download the following text file:

Median.txt
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 5 lecture on heap
applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat
this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk
is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among
x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That
is, you should compute (m1+m2+m3+?+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the
algorithm.
"""

__author__ = 'Vinayak'

from fileIO import readAsList,writeSingleToFile
import heapq

def simulateMedianHeap(inputList):
    """returns the cumulative sum of medians"""

    first=inputList.pop(0)

    minHeap,maxHeap=[],[first]

    medianSum=first

    for incomingValue in inputList:

        if incomingValue < maxHeap[0]:
            heapq.heappush(minHeap,-incomingValue)
        else:
            heapq.heappush(maxHeap,incomingValue)

        while abs(len(minHeap)-len(maxHeap))>1:
            if len(minHeap)+1<len(maxHeap):
                heapq.heappush(minHeap,-heapq.heappop(maxHeap))
            elif len(maxHeap)+1<len(minHeap):
                heapq.heappush(maxHeap,-heapq.heappop(minHeap))

        if len(minHeap)<len(maxHeap):
            medianSum+=maxHeap[0]
        else:
            medianSum+=(-minHeap[0])

    return medianSum


if __name__=="__main__":
    inputList = readAsList("_6ec67df2804ff4b58ab21c12edcb21f8_Median.txt",int)
    writeSingleToFile("Problem6b.txt",simulateMedianHeap(inputList)%10000)