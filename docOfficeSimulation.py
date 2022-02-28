#!/usr/bin/env python3

import numpy
import random

def nextBigger(t,someList):
    if len(someList) == 0:
        raise Exception('Looks like you entered a list to nextBigger which had length 0!')
    result = float('inf')
    for val in someList:
        if t < val and val < result:
            result = val
    return result

def oneSimulation(scale = 10, totalMinutes = 420, minVisitTime = 5, maxVisitTime = 20, numDocs = 3):
    firstArrivalUnif = random.uniform(0,1)
    firstArrivalTime = -scale*numpy.log(1-firstArrivalUnif)

    timeArrived = [firstArrivalTime]

    while max(timeArrived) <= totalMinutes:
        unifDraw = random.uniform(0,1)
        exponDraw = -scale*numpy.log(1-unifDraw)
        timeArrived.append(max(timeArrived)+exponDraw)

    timeArrived.remove(max(timeArrived))

    numPatients = len(timeArrived)
    
    firstPatTimes = [minVisitTime + (maxVisitTime - minVisitTime)*random.uniform(0,1) for i in range(numDocs)]

    docStarted = []
    docStopped = []

    for i in range(numDocs):
        docStarted.append([timeArrived[i]])
        docStopped.append([timeArrived[i] + firstPatTimes[i]])

    timeSeen = timeArrived[0:numDocs]

    t = timeArrived[numDocs -1]
    
    while len(timeSeen) < numPatients:
        visitTime = minVisitTime + (maxVisitTime - minVisitTime)*random.uniform(0,1)
        
        nBList = [nextBigger(t,timeArrived)]

        for i in range(numDocs):
            nBList.append(nextBigger(t,docStopped[i]))
        
        if nBList[0] == min(nBList):
            t = nBList[0]
            for i in range(numDocs):
                if max(docStopped[i]) <= t:
                    docStarted[i].append(t)
                    docStopped[i].append(t+visitTime)
                    timeSeen.append(t)
                    break

        for i in range(numDocs):
            if nBList[i+1] == min(nBList):
                t = nBList[i+1]
                if timeArrived[len(timeSeen)] <= t:
                    docStarted[i].append(t)
                    docStopped[i].append(t+visitTime)
                    timeSeen.append(t)
                break
    print([timeSeen[i] - timeArrived[i] for i in range(len(timeArrived))])
    return

if __name__ == '__main__':
    oneSimulation()
