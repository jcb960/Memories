"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
"""

import AbasicFunctions as bF
import HsimulationFunctions as sF
import KdataFunctions as dF
import random

hypothesisTest=False #For Hypothesis test only

p1FileGameData=open("p1GameData (0% Memory).csv", "a") #opens player 1's csv file for data to get stored
p2FileGameData=open("p2GameData (0% Memory).csv", "a") #opens player 2's csv file for data to get stored

#Between 2 computers
for gameRound in range(1000): #Plays 1000 games, or x amount of games
    #Variables inside as they change every game 

    setShuffled=bF.shuffleCards()

    indexesUsed: list=[] #type annotation to remove warnings given by thonny
    compAMem: list=[]
    compBMem: list=[]

    p1Turn=True
    p1PairsMissedList: list=[]
    p1InputHistory: list=[]
    p1WinStates: list=[]
    p1CompleteInputHistory: list=[]
    p1RunsList: list=[]

    p2Turn=False
    p2PairsMissedList: list=[]
    p2InputHistory: list=[]
    p2WinStates: list=[]
    p2CompleteInputHistory: list=[]
    p2RunsList: list=[]

    runs=1

    p1Pairs=0
    p2Pairs=0
    pairs=0

    while True:
    #Computer 1
        while p1Turn==True:
            p1RunsList.append(runs)
            
            if runs==1 and hypothesisTest==True: #Used to test if guessing a certain pair at the start of the game with Player 1 will increase your chance at winning
                listInps=[1, 2] #Testing the pair of index 1 and 2
                
            else:            
                randomChance=random.randint(1, 1) #To alter Computer Memory
                #if randomChance = 1, but they have to have in range(2, 3) to use the memCheckUp functions, which will be never, so its memory is 0%
                #But if randomChance is from [1, 2], and memCheckUp only happens if it lands on a 1, there is a 50% chance it lands on 1, so 50% chances it remembers the cards
                if randomChance in range(2, 3): #If randomChance is in this range, it will remember and pick a pair accordingly
                    memCheckUp=sF.memoryCheck(compAMem, setShuffled, indexesUsed)       
                    listInps=sF.computerInp(memCheckUp, compAMem, indexesUsed, setShuffled)
                else: #If not it guess randomly not knowing if it has a pair found in its memList
                    listInps=[]
                    while True:
                        randInp1=random.randint(1, 54)
                        if randInp1 not in indexesUsed:
                            listInps.append(randInp1)
                            if randInp1 not in compAMem:
                                compAMem.append(randInp1)
                            break
                    while True:
                        randInp2=random.randint(1, 54)
                        if randInp2 not in indexesUsed and randInp1!=randInp2:
                            listInps.append(randInp2)
                            if randInp1 not in compAMem:
                                compAMem.append(randInp2)
                            break
                    
            if listInps[0] not in p1InputHistory:
                p1InputHistory.append(listInps[0]) #Player 1's input history, no duplicates for card 1
                
            selectionsCheck=dF.ongoingSelections(p1InputHistory, indexesUsed, setShuffled) #Checks all the selections it can choose from, [10♠, 10♣, 10♥] is a selection
            pairsCheck=dF.allPossiblePairsFounder(selectionsCheck) #Using the selections, how many different ways could I pick a pair from this selection
            pairsMissed=dF.pairsMissedCounter(pairsCheck) #If there are pairs yet to be found but seen, it will add to the amount of pairs they missed
            
            if listInps[1] not in p1InputHistory:
                p1InputHistory.append(listInps[1]) #for card 2
            
            p1CompleteInputHistory.append(listInps[0]) #Used to see how many times it chose the same came card more than once
            p1CompleteInputHistory.append(listInps[1])
            
            firstPick=setShuffled[listInps[0]-1]
            secondPick=setShuffled[listInps[1]-1]
            
            if firstPick[:-1]==secondPick[:-1]:
                winState=True
                p1PairsMissedList.append(0)
                
                indexesUsed.append(listInps[0])
                indexesUsed.append(listInps[1])
                p1Pairs+=1
                pairs+=1
                
            else:
                winState=False
                p1PairsMissedList.append(pairsMissed)
                
                p1Turn=False
                p2Turn=True
            p1WinStates.append(winState)
            runs+=1
                
            if pairs == 27:
                break
    #Computer 2        
        while p2Turn==True: #Explained the concept above, hypothesis test doesn't affect player 2
            p2RunsList.append(runs)
            randomChance=random.randint(1, 1)
            if randomChance in range(2, 3):
                memCheckUp=sF.memoryCheck(compBMem, setShuffled, indexesUsed)       
                listInps=sF.computerInp(memCheckUp, compBMem, indexesUsed, setShuffled)
            else:
                listInps=[]
                while True:
                    randInp1=random.randint(1, 54)
                    if randInp1 not in indexesUsed:
                        listInps.append(randInp1)
                        if randInp1 not in compBMem:
                            compBMem.append(randInp1)
                        break
                while True:
                    randInp2=random.randint(1, 54)
                    if randInp2 not in indexesUsed and randInp1!=randInp2:
                        listInps.append(randInp2)
                        if randInp1 not in compBMem:
                            compBMem.append(randInp2)
                        break
                    
            if listInps[0] not in p2InputHistory:
                p2InputHistory.append(listInps[0])
                
            selectionsCheck=dF.ongoingSelections(p2InputHistory, indexesUsed, setShuffled)
            pairsCheck=dF.allPossiblePairsFounder(selectionsCheck)
            pairsMissed=dF.pairsMissedCounter(pairsCheck)
            
            if listInps[1] not in p2InputHistory:
                p2InputHistory.append(listInps[1])

            p2CompleteInputHistory.append(listInps[0])
            p2CompleteInputHistory.append(listInps[1])
            
            firstPick=setShuffled[listInps[0]-1]
            secondPick=setShuffled[listInps[1]-1]
            
            if firstPick[:-1]==secondPick[:-1]:
                winState=True
                p2PairsMissedList.append(0)
                
                indexesUsed.append(listInps[0])
                indexesUsed.append(listInps[1])
                p2Pairs+=1
                pairs+=1
                
            else:
                winState=False
                p2PairsMissedList.append(pairsMissed)            
                
                p1Turn=True
                p2Turn=False
            p2WinStates.append(winState)
            runs+=1
                
            if pairs == 27:
                break
                   
        if pairs == 27:
            p1WinStates.append(False) #Streak is found by calculating [0, 1, 1, 1, 0], all the 1 in between 2 zeros, so to count the last section, a 0 must be appended into the list 
            p2WinStates.append(False) #So it does not end on, [0, 1, 1, 1, 0, 1, 1], it would not count the last 2 wins it got because there is no zero at the end
            
            p1StreakList=dF.highestStreak(p1WinStates)
            p2StreakList=dF.highestStreak(p2WinStates)
            
            p1NumOfStreaks=dF.amountStreaks(p1StreakList)
            p2NumOfStreaks=dF.amountStreaks(p2StreakList)
            
            p1TotalCardsGuessed=len(p1CompleteInputHistory)
            p1TotalDistinctCardsG=len(dF.distinctCards(p1CompleteInputHistory))
            
            p2TotalCardsGuessed=len(p2CompleteInputHistory)
            p2TotalDistinctCardsG=len(dF.distinctCards(p2CompleteInputHistory))
            
            p1RoundsOfMostPairsMissed=dF.roundsOfMostPairsMissed(p1PairsMissedList, p1RunsList)
            p2RoundsOfMostPairsMissed=dF.roundsOfMostPairsMissed(p2PairsMissedList, p2RunsList)
            
            """
            print("\nGood job! All 27 pairs have been found in", runs-1, "runs!")
            print("Player 1:", p1Pairs, "| Player 2:", p2Pairs)
            print("Player 1:", sum(p1PairsMissedList), "| Player 2:", sum(p2PairsMissedList))
            print("Player 1:", p1StreakList, "| Player 2:", p2StreakList)
            print("Player 1:", max(p1StreakList), "| Player 2:", max(p2StreakList))
            print("Player 1:", p1NumOfStreaks, "| Player 2:", p2NumOfStreaks)
            print("Player 1:", [p1TotalCardsGuessed, p1TotalDistinctCardsG], "| Player 2:", [p2TotalCardsGuessed, p2TotalDistinctCardsG])
            print("Player 1:", p1RoundsOfMostPairsMissed, "| Player 2:", p2RoundsOfMostPairsMissed)
            print("Player 1:", max(p1PairsMissedList), "| Player 2:", max(p2PairsMissedList))
            """
            #Player 1's Data writing to csv file
            p1FileGameData.write("\n"+str(runs)+",")
            p1FileGameData.write(str(p1Pairs)+",")
            p1FileGameData.write(str(max(p1StreakList))+",")
            p1FileGameData.write(str(p1NumOfStreaks)+",")
            p1FileGameData.write(str(p1TotalDistinctCardsG)+",")
            p1FileGameData.write(str(p1TotalCardsGuessed)+",")
            p1FileGameData.write(str(sum(p1PairsMissedList))+",")
            p1FileGameData.write(str(max(p1PairsMissedList))+",")

            p1List1ToString="" #To convert the list into a string
            for p1Rounds1 in p1RoundsOfMostPairsMissed:
                p1List1ToString+=str(p1Rounds1)+" "
            p1List1ToString=p1List1ToString[:-1]
            p1FileGameData.write(p1List1ToString+",")
            
            p1List2ToString="" #since there are commas in the list, it would count as the delimiter, so space is replaced with the comma
            for p1Rounds2 in p1RunsList:
                p1List2ToString+=str(p1Rounds2)+" "
            p1List2ToString=p1List2ToString[:-1]
            p1FileGameData.write(p1List2ToString+",")
            
            p1List3ToString="" #same reason as above
            for p1Rounds3 in p1PairsMissedList:
                p1List3ToString+=str(p1Rounds3)+" "
            p1List3ToString=p1List3ToString[:-1]
            p1FileGameData.write(p1List3ToString+",")
            
            #Player 2's Data writing to csv file
            p2FileGameData.write("\n"+str(runs)+",")
            p2FileGameData.write(str(p2Pairs)+",")
            p2FileGameData.write(str(max(p2StreakList))+",")
            p2FileGameData.write(str(p2NumOfStreaks)+",")
            p2FileGameData.write(str(p2TotalDistinctCardsG)+",")
            p2FileGameData.write(str(p2TotalCardsGuessed)+",")
            p2FileGameData.write(str(sum(p2PairsMissedList))+",")
            p2FileGameData.write(str(max(p2PairsMissedList))+",")

            p2List1ToString="" #Explained above
            for p2Rounds1 in p2RoundsOfMostPairsMissed:
                p2List1ToString+=str(p2Rounds1)+" "
            p2List1ToString=p2List1ToString[:-1]
            p2FileGameData.write(p2List1ToString+",")

            p2List2ToString=""
            for p2Rounds2 in p2RunsList:
                p2List2ToString+=str(p2Rounds2)+" "
            p2List2ToString=p2List2ToString[:-1]
            p2FileGameData.write(p2List2ToString+",")
            
            p2List3ToString=""
            for p2Rounds3 in p2PairsMissedList:
                p2List3ToString+=str(p2Rounds3)+" "
            p2List3ToString=p2List3ToString[:-1]
            p2FileGameData.write(p2List3ToString+",")            
            
            break
        
    if gameRound in range(0, 10001, 100):
        print("Game Round:", gameRound+1, "| Finished!")

p1FileGameData.close() #Closes the file after the full x amount of games finishes
p2FileGameData.close() #The opening and closing of the file is not done every time a new game starts as it slows down the process
"""
p1FileHeadings=open("p1GameData (0% Memory).csv", "w")
p1FileHeadings.write("Runs,Pairs,Highest streak,No. of streaks,Distinct cards picked,Total cards picked,Pairs missed,Max pairs missed(MPM) in 1 round,Rounds of MPM,Runs list,Pairs missed list,")  
p1FileHeadings.close()

p2FileHeadings=open("p2GameData (0% Memory).csv", "w")
p2FileHeadings.write("Runs,Pairs,Highest streak,No. of streaks,Distinct cards picked,Total cards picked,Pairs missed,Max pairs missed(MPM) in 1 round,Rounds of MPM,Runs list,Pairs missed list,")  
p2FileHeadings.close()
#"""
#To overwrite the past data with the headings for new incoming data
