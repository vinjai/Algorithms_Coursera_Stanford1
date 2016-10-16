#!/usr/bin/env python

__author__ = 'Vinayak'

import re

inputPathName="..\\Inputs\\"
outputPathName="..\\Outputs\\"

def readAsList(fileName,dataType=str):
    """return the file contents as List"""
    file=open(inputPathName+fileName,'r')
    return [dataType(line) for line in file]


def readAsListOfDict(fileName,expression='',fieldCount=1,keyList=None,fieldDataList=None,omitLines=0,splitOmitLines=0):
    """return the file content as List of Dictionary where line is split based on a regular expression"""
    if keyList==None:
        keyList=[x for x in range(fieldCount)]
    if fieldDataList==None:
        fieldDataList=[str for x in range(fieldCount)]

    if type(keyList)!=list:
        raise Exception("parameter keyList should be a list")
    if type(fieldDataList)!=list:
        raise Exception("parameter fieldDataList should be a list")

    if fieldCount<1:
        raise Exception("fieldCount should be greater than 0")

    if len(keyList)!=fieldCount:
        raise Exception("length of keyList not matching fieldCount")
    if len(fieldDataList)!=fieldCount:
        raise Exception("length of fieldDataList not matching fieldCount")

    file=open(inputPathName+fileName,'r')
    for i in range(omitLines):
        file.readline()
    returnList=[]
    for i in range(splitOmitLines):
        returnList.append(file.readline())
    for line in file:
        splitList=re.split(expression,line)
        tmpDict={}
        for i in range(fieldCount):
            tmpDict[keyList[i]]=fieldDataList[i](splitList[i])
        returnList.append(tmpDict)

    return returnList


def writeSingleToFile(fileName,value):
    """Write a Single Variable to a file"""
    file=open(outputPathName+fileName,'w')
    file.write(str(value))

if __name__=="__main__":
    #print(readAsList("_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt",int))
    #print([str for x in range(5)])
    print(readAsListOfDict('_642c2ce8f3abe387bdff636d708cdb26_jobs.txt','\s+',2,['weight','length'],[int,int],1,0))
    pass
