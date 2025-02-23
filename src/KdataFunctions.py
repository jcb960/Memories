"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

def distinctCards(memList): #Gets distinct items in the list, no duplicates
    distinctList=[]
    for item in memList:
        if item not in distinctList:
            distinctList.append(item)
    return distinctList

def frequencyTable(uniqueSet, allSet): #Gets the frequency of how many times a item appears in a list
    freqList=[]
    for uniqueItem in uniqueSet:
        freq=allSet.count(uniqueItem)
        freqList.append(freq)
    return freqList

def medianSet(setList): #Get the median of a list
    setList.sort()
    if len(setList)%2==0:
        middlePlusOne=len(setList)//2
        median=(setList[middlePlusOne-1]+setList[middlePlusOne])/2
    else:
        middle=len(setList)//2
        median=setList[middle]
    return median

#For Pairs Frequency of the shuffled cards, not for in game use
def allSelectionsFounder(setShuffled): #Finds all the selections, such as [1, 2, 3, 4] indexes being spades, so [1, 2], [1, 3], [3, 4] etc could be a pair
    fullSelections=[]
    for firstCardIndex in range(len(setShuffled)):
        firstCard=firstCardIndex+1
        singleSelections=[firstCard]
        
        for secondCardIndex in range(len(setShuffled)):
            secondCard=secondCardIndex+1
            
            if firstCardIndex!=secondCardIndex:
                gameCard1=setShuffled[firstCardIndex]
                gameCard2=setShuffled[secondCardIndex]
                
                if gameCard1[:-1]==gameCard2[:-1]:
                    singleSelections.append(secondCard)
        singleSelections.sort() #Sorted so it can be compared later on and does not get used more than once
        
        if singleSelections not in fullSelections:
            fullSelections.append(singleSelections)
    return fullSelections

def allPossiblePairsFounder(allSelectionsSet): #Finds all the possible combination/arrangements of the pair within the selections
    possiblePairsSet=[]
    for pairsList in allSelectionsSet:
        pairsSet=[]
        for cardIndex1 in range(len(pairsList)):
            for cardIndex2 in range(len(pairsList)):
                if cardIndex1!=cardIndex2:
                    pair=[]
                    pair.append(pairsList[cardIndex1])
                    pair.append(pairsList[cardIndex2])
                    pair.sort() #Sorted so it won't get used more than once
                    if pair not in pairsSet: #[1, 2] is not the same as [2, 1], so order matters, hence sorting
                        pairsSet.append(pair)
        possiblePairsSet.append(pairsSet)
    return possiblePairsSet

def singleListConversion(allPossiblePairs): #Taking all the pairs out of the step by step selections list and putting them all in one List
    finalPairsSet=[]
    for list1 in allPossiblePairs:
        for list2 in list1:
            finalPairsSet.append(list2)
    return finalPairsSet

def ongoingSelections(allPicksS, indexesUsed, setShuffled): #On going selections is the function used in game, and during games
    cardsNotUsed=[]
    for card in allPicksS:
        if card not in indexesUsed:
            cardsNotUsed.append(card)
    
    fullSelections=[]
    for firstCardIndex in range(len(cardsNotUsed)):
        firstCard=cardsNotUsed[firstCardIndex]
        singleSelections=[firstCard]
        
        for secondCardIndex in range(len(cardsNotUsed)):
            if firstCardIndex!=secondCardIndex:
                secondCard=cardsNotUsed[secondCardIndex]
                
                gameCard1=setShuffled[firstCard-1]
                gameCard2=setShuffled[secondCard-1]
                
                if gameCard1[:-1]==gameCard2[:-1]:
                    singleSelections.append(secondCard)
        singleSelections.sort() #Same reason as mentioned before
        
        if singleSelections not in fullSelections:
            fullSelections.append(singleSelections)
    return fullSelections
                    
def pairsMissedCounter(pairsInSelections):
    pairsMissed=0
    for possiblePairsList in pairsInSelections:
        if len(possiblePairsList)==6:
            pairsMissed+=2 #As there are 6 ways of picking a selection but only 2 pairs could be found, as once one card is gone, it cannot be reused
        elif 0<len(possiblePairsList)<6:
            pairsMissed+=1 #The next possible length is 3 within the selections, in which only one pair could be obtained
    return pairsMissed

def roundsOfMostPairsMissed(pairsMissedList, runsList): #Finds out which run number is the most pairs missed
    maxPairsMissed=max(pairsMissedList)
    roundsList=[]
    for pairsMissedIndex in range(len(pairsMissedList)):
        if pairsMissedList[pairsMissedIndex]==maxPairsMissed:
            roundsList.append(runsList[pairsMissedIndex])
    return roundsList
    
def highestStreak(trueFalseList): #Related to the streaks
    binaryList=[] #Converting Trues to 1s and Falses to 0s
    for streakState in trueFalseList:
        if streakState==True:
            binaryList.append(1)
        else:
            binaryList.append(0)
            
    zerosIndexList=[] #Finds out where are all the zeros are in terms of index(Pairs not found)
    for zerosIndexI in range(len(binaryList)):
        if binaryList[zerosIndexI]==0:
            zerosIndexList.append(zerosIndexI)
    
    streakList=[]        
    startingPoint=0 #The travelling variables from one zero to next, indexOfZeros=[1, 2, 5, 9]
    finishingPoint=1 #It checks values between 1 and 2, then 2 and 5, then 5 and 9 and so on...
    
    while True:
        firstPos=zerosIndexList[startingPoint]+1 #+1 because the zero index +1, is where True(1) is, and it is inclusive
        secondPos=zerosIndexList[finishingPoint] #no +1 here because this the ending of the zero, so it's not included but the second last value is, which is the last 1 in that line
        
        tempStreakList=binaryList[firstPos:secondPos] #indexOfZeros=[1, 2, 5, 9], so from 5 to 9 =>, 6, 7, 8 are 1s so 3 is the highest streak there
        streakFound=sum(tempStreakList)
        streakList.append(streakFound)
        
        startingPoint+=1 #Moves to the next values in the zeros index list
        finishingPoint+=1 #Moves to the next values in the zeros index list
        
        if finishingPoint==len(zerosIndexList): #breaks once finished
            break
    
    cleanedStreakList=[] #Removes all the 0s (no pair found) from the list
    for streak in streakList:
        if streak!=0:
            cleanedStreakList.append(streak)
    
    return cleanedStreakList

def amountStreaks(streakList): #Finds the numbers of streaks for that player
    numOfStreaks=0
    for streak in streakList:
        if streak>1: #Greater than 1 because finding 1 pair does not signal a beginning of a streak
            numOfStreaks+=1
    return numOfStreaks
