#!/usr/bin/env python

"""
Download the following text file:

IntegerArray.txt
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer
repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith
entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the
video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any
other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the
final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising.
Then post your best test cases to the discussion forums to help your fellow students!]
"""

__author__ = 'Vinayak'

from fileIO import readAsList,writeSingleToFile
import sys

sys.setrecursionlimit(1500)

def _merge(arr,start,end):
    """Merge two lists"""
    m=(start+end)//2
    i=start
    j=m+1
    ret=[]
    inversions=0

    while i<=m or j<=end:
        if i > m:
            ret.append(arr[j])
            j+=1
        elif j>end:
            ret.append(arr[i])
            #inversions+=(m+start-i+1)
            i+=1
        elif arr[i]<=arr[j]:
            ret.append(arr[i])
            i+=1
        elif arr[i]>arr[j]:
            ret.append(arr[j])
            inversions+=(m-i+1)
            j+=1

    for i in range(len(ret)):
        arr[start+i]=ret[i]

    return inversions



def _mergeInversionCount(arr,start,end):
    """MergeSort while counting inversions"""
    if start>=end:
        return 0
    else:
        m=(start+end)//2
        return _mergeInversionCount(arr,start,m) + _mergeInversionCount(arr,m+1,end) + _merge(arr,start,end)

def countInversions(arr):
    """Count no. of inversions"""
    return _mergeInversionCount(arr,0,len(arr)-1)

if __name__=="__main__":
    inputList = readAsList("_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt",int)
    writeSingleToFile("Problem1.txt",countInversions(inputList))
    pass