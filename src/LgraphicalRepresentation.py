"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

import matplotlib.pyplot as plt #Imports all matplotlib.pylot functions
import KdataFunctions as dF #Imports all the data functions
import AbasicFunctions as bF #Imports all the basic game functions

fileName="p1GameData (0% Memory).csv"
filePM=open(fileName, "r")
dataPM=filePM.read()
filePM.close()

dataPM=dataPM.split(",")
dataPM=dataPM[:-1] #There is a "\n" at the end, so doing this will remove that

startPos=11 #Where the first line of each game starts (data in csv file)
finishPos=22 #Where the first line of each game ends (data in csv file)

perGameList=[] #A list containing all of the Game Data
while True:
    perGameL=dataPM[startPos:finishPos] #Arranging them so that each games get its own list
    firstItem=perGameL[0] 
    perGameL[0]=firstItem[1:] #To remove the "\n" at the start of the data(runs) as it was used to move to a new line
    
    perGameList.append(perGameL)
    
    if finishPos==len(dataPM):
        break

    startPos+=11 #New game data list
    finishPos+=11

#"""
#Pair missed in each run
def runsVsPM(alphaData):
    global fileName #Makes fileName visible to the function
    
    #Appending all the runs from all games to a single list
    allRunsList=[]
    for tempList1 in alphaData:
        runValue=int(tempList1[0])
        allRunsList.append(runValue)
    
    #Finding the max run and adding every run from 1 to max run in a list
    maxRuns=max(allRunsList)
    runningRunsList=[]
    for num in range(1, maxRuns+1):
        runningRunsList.append(num)
    
    #Putting runs in a list form (runs in which it was player's turn)
    listFormOfRuns=[]
    for tempList2 in alphaData:
        runsList=tempList2[9]
        runsList=runsList.split(" ")
        runsList=[int(item) for item in runsList]
        listFormOfRuns.append(runsList)
              
    #Putting pairs missed in a list form and adding that list into an alpha list
    listFormOfPML: list=[]
    for tempList3 in alphaData:
        listPM=tempList3[10]
        listPM=listPM.split(" ")
        listPM=[int(item) for item in listPM]
        listFormOfPML.append(listPM)
       
    #Calculating mean of PM in each run
    meanOfPMPerRunL: list=[]
    if fileName=="p2GameData (0% Memory).csv":
        meanOfPMPerRunL.append(0) #Game starts at run 1 but player 2 never gets to play round 1 so added a temporary value
    
    for perRun in runningRunsList: #Goes through each run upto the max run found in the allRunsList
        allPMThatRoundL=[] #Pair missed that round by that player
        for eachGameI in range(len(listFormOfRuns)):
            eachGameRL=listFormOfRuns[eachGameI] #Each Games Runs list for that player
            if perRun in eachGameRL:
                tempIndex1=eachGameRL.index(perRun) #Since the pairs missed and that run have the same index and there are no duplicates of runs, this can be used
                
                thatPMList=listFormOfPML[eachGameI] #Gets the pairs missed LIST of that run
                pairsMissedThatRound=thatPMList[tempIndex1] #In that LIST, it gets the eact Pairs Missed for that run
                
                allPMThatRoundL.append(pairsMissedThatRound) #Adds in to the List
            else:
                if len(allPMThatRoundL)!=0:
                    pass #Does nothing, used for when the player has not played that run anywhere throughout the games
                else:
                    allPMThatRoundL.append(meanOfPMPerRunL[-1]) #if not, it will add the previous value as a substitute value for continuity
        
        meanOfThatRound=round(sum(allPMThatRoundL)/len(allPMThatRoundL), 2) #Gets the mean of that all pairs missed that specific run
        meanOfPMPerRunL.append(meanOfThatRound)
                      
    itemsToTransfer=[] #Items to transfer for graphical use
    itemsToTransfer.append(runningRunsList)
    itemsToTransfer.append(meanOfPMPerRunL)
    
    return itemsToTransfer

dataCollectedRvsPM=runsVsPM(perGameList)
runsListX=dataCollectedRvsPM[0]
listPMY=dataCollectedRvsPM[1]

if fileName=="p2GameData (0% Memory).csv":
    listPMY.remove(listPMY[0]) #Removing the temporary value added in earlier

plt.scatter(runsListX, listPMY)
plt.title("MEAN | Runs VS Avg. Pairs Missed Per Run of Player 1 (0% Memory) over 10,000 Games")
plt.xlabel("Run Number")
plt.ylabel("Avg. Pairs Missed")
plt.show()
#"""
#"""
#Top 10 most frequent pairs
filePairCounter=open("possiblePairsData.csv", "w")
for roundOne in range(500): #Not related to the data of simulation quick play, done seperately
    shuffledSet=bF.shuffleCards() #Gets a shuffled list of cards
    allSelectionsL=dF.allSelectionsFounder(shuffledSet) #Gets all the selections as explained in KdataFunctions.py
    allPairsL=dF.allPossiblePairsFounder(allSelectionsL) #Gets all the pairs 
    allPairsInSingleL=dF.singleListConversion(allPairsL) #Converts into a single list
    
    allStringList=[]
    for item1 in allPairsInSingleL:
        pairSelected=str(item1[0])+" "+str(item1[1]) #"[1, 2]" => "1 2" for easier use and comma delimiter problem
        allStringList.append(pairSelected)
    
    for item2 in allStringList:
        filePairCounter.write(item2+",") #Adding it into the file
    
    filePairCounter.write("\n") #After each shuffled set (after each game)
filePairCounter.close()

fileReadPC=open("possiblePairsData.csv", "r")
dataCollectedPC=fileReadPC.read()
fileReadPC.close() #Reads back all the data

dataListPC=dataCollectedPC.split(",")
dataListPC=dataListPC[:-1] #Removes the "\n" at the very end

dataByGameSortPC=[] #Every Shuffled Set list
firstPosPC=0 #Starts at this positiion
secondPosPC=79 #Every individual game's data is in multiples of 79

while True:
    dataByGamePCL=dataListPC[firstPosPC:secondPosPC]
    if firstPosPC==0: #There is no "\n" in the first game set of data
        pass
    else:
        firstItemPC=dataByGamePCL[0]
        dataByGamePCL[0]=firstItemPC[1:] #Removes the "\n" at the start of every first data of the data set
    
    dataByGameSortPC.append(dataByGamePCL)
    
    if secondPosPC==len(dataListPC):
        break
    
    firstPosPC+=79 #Each shuffled set of each game is in multiples of 79
    secondPosPC+=79

singleListGamePC=dF.singleListConversion(dataByGameSortPC) #Converts all the pairs collected into a single list
distinctPairL=dF.distinctCards(singleListGamePC) #Finds all the dinctinct cards, hence sorting is needed so [1, 2] == [2, 1]
freqPCL=dF.frequencyTable(distinctPairL, singleListGamePC) #Returns a frequency table with the same index as the dinctinct cards list

secondFreqPCL=sorted(freqPCL, reverse=True) #Sorts the freqPCL from highest to lowest to find top 10 modes of the data

top10PairsNameL=[]
top10HighestPairL=secondFreqPCL[:10] #The top 10 frequencies found in the list

top10HPL2=dF.distinctCards(top10HighestPairL) #Incase if any frequency appears more than once

for freqItem1 in top10HPL2:
    
    
    indexListHPL=[]
    for freqItem2 in range(len(freqPCL)):
        if freqPCL[freqItem2]==freqItem1: #Gets all the indexes where freqItem1 == that item's index in freqPCL
            indexListHPL.append(freqItem2)
    
    for indexItem in indexListHPL:
        top10PairsNameL.append(distinctPairL[indexItem]) #Since freqPCL and distinctPairL has their indexes corresponding to each other, we could use this
        
        if len(top10PairsNameL)==10: #Only need top 10
            break
    
    if len(top10PairsNameL)==10: #Only need top 10
        break

for pair10Index in range(len(top10PairsNameL)):
    pair10Item="["+top10PairsNameL[pair10Index]+"]" #Add "[]" for aesthetics
    top10PairsNameL[pair10Index]=pair10Item

plt.bar(top10PairsNameL, top10HighestPairL)
plt.title("MODE | Top 10 Most Frequent Pairs in 10,000 games")
plt.xlabel("Pair")
plt.ylabel("Occurances")
plt.show()
#"""   
#"""
#Player 1 wis rate VS Player 2 win rate
playerPairsList=[] #All pairs list
for perGamePP in perGameList:
    playerPairsList.append(int(perGamePP[1])) #Gets all the pairs found by the player at the end of each game (int)
    
trueFalseWinList=[]
for playerPair in playerPairsList:
    if playerPair>=14: #Getting 14 or greater = win =True
        trueFalseWinList.append(True)
    else: #If not, the player lost = False
        trueFalseWinList.append(False)

winCounter=0
lostCounter=0

for trueFalse in trueFalseWinList:
    if trueFalse==True:
        winCounter+=1 #For every Win, add a win counter
    else:
        lostCounter+=1 #For every defeat, adds a lose counter

winRateList=[winCounter, lostCounter]
namesPP=["Player 1", "Player 2"]

if fileName=="p2GameData.csv":
    tempVariable=namesPP[0] #swapping variables 
    namesPP[0]=namesPP[1]
    namesPP[1]=tempVariable

plt.pie(winRateList, labels=namesPP, autopct='%1.1f%%') #autopct gets your percentages of each sector and display it in the graph
plt.title("Player 1 wins VS Player 2 wins in 10,000 games")
plt.show()
#"""
#"""
#Frequencies Runs at intervals of 100
allRunsListGP=[]
for perGameGP in perGameList:
    allRunsListGP.append(int(perGameGP[0])) #Gets all the runs of each game (int)

allRunsListGP.sort()
maxRunsGP=str(max(allRunsListGP)) #To see which is the highest runs in the entire data set

if len(maxRunsGP)==2: #This is incase if the highest runs in a games is a 2-digit number, this code is suitable for 3 digit runs, so to accomodate 2 digits, we add a 0 at the start
    maxRunsGP="0"+maxRunsGP

labelsList=["0-100", "100-200", "200-300", "300-400", "400-500", "500-600", "600-700", "700-800", "800-900", "900-1000"] #900-1000 runs is the max it could go
YfreqGPList=[]

for freqI in range(int(maxRunsGP[0])+1): #Example: 152, it would fit into 0-100, and 100-200, so 1 + 1 =2, so there will be 2 values in the graph
    YfreqGPList.append(0) #Setting frequency table

XlabelsFreq=labelsList[:len(YfreqGPList)] #See how far this frequencyTable has to be

for runGP in allRunsListGP:   
    strRunGP=str(runGP)
    if len(strRunGP)==2:
        strRunGP="0"+strRunGP #To accommodate 2 digit runs
    
    indexRGP=int(strRunGP[0]) #This works for example 178, the first digit 1, the index of the labelsList which belong in the category of 100-200
    YfreqGPList[indexRGP]+=1 #Adds frequency to it

plt.bar(XlabelsFreq, YfreqGPList)
plt.title("FREQUENCY | Frequencies of Runs per game in 10,000 games (100-200 => includes 100 but not 200)")
plt.xlabel("Intervals of per 100 Runs")
plt.ylabel("Frequencies")
plt.show()
#"""   
#"""
#Median of Highest Streak and Number of Streak
allHighestStreakL=[]
for gameHS in perGameList:
    allHighestStreakL.append(int(gameHS[2])) #Gets all the highest streak values

allNumOfStreakL=[]
for gameNOS in perGameList:
    allNumOfStreakL.append(int(gameNOS[3])) #Gets all the no. of streaks values

medianAHSL=dF.medianSet(allHighestStreakL) #Gets the median of the list
medianANOSL=dF.medianSet(allNumOfStreakL) #Gets the median of the list
medianAL=[medianAHSL, medianANOSL] #Median list

maxAHSL=max(allHighestStreakL) #Gets the max of the list
maxANOSL=max(allNumOfStreakL) #Gets the max of the list
maxAL=[maxAHSL, maxANOSL] #Max list

minAHSL=min(allHighestStreakL) #Gets the min of the list
minANOSL=min(allNumOfStreakL)#Gets the min of the list
minAL=[minAHSL, minANOSL] #Min list

namesAL=["Highest Streak", "No. Of Streaks"]

plt.bar(namesAL, maxAL) #All appears on the same graph, bar chart to compare
plt.bar(namesAL, medianAL)
plt.bar(namesAL, minAL)

plt.legend(["Max", "Median", "Min"]) #The legends to indicate which colour is what
plt.title("MEDIAN | Highest Streaks and No. Of Streaks of Player 1 in 10,000 games")
plt.xlabel("Streaks")
plt.ylabel("Values")
plt.show()
#"""