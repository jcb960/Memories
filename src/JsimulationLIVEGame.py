"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

import AbasicFunctions as bF
import BgameFunctions as gF
import HsimulationFunctions as sF
import time

#Computer vs Computer with 100% memory, showing LIVE Gameplay
#Same explanation as the simulation quickgame and multiplayer 

circleList=['⓪①', '⓪②', '⓪③', '⓪④', '⓪⑤', '⓪⑥', '⓪⑦', '⓪⑧', '⓪⑨', '①⓪', '①①', '①②', '①③', '①④', '①⑤', '①⑥', '①⑦', '①⑧', '①⑨', '②⓪', '②①', '②②', '②③', '②④', '②⑤', '②⑥', '②⑦', '②⑧', '②⑨', '③⓪', '③①', '③②', '③③', '③④', '③⑤', '③⑥', '③⑦', '③⑧', '③⑨', '④⓪', '④①', '④②', '④③', '④④', '④⑤', '④⑥', '④⑦', '④⑧', '④⑨', '⑤⓪', '⑤①', '⑤②', '⑤③', '⑤④']            
setShuffled=bF.shuffleCards()

indexesUsed: list=[]
compAMem: list=[]
compBMem: list=[]

p1Turn=True
p2Turn=False
runs=1

p1Pairs=0
p2Pairs=0
pairs=0

while True:
#Computer 1
    while p1Turn==True:
        pAllList=[]
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        
        gameBoard=bF.layoutCards(circleList)
        playerNumber=gF.whoTurn(pAllList)
        gF.headerMulti(playerNumber, runs, p1Pairs)
        print(gameBoard)
        
        memCheckUp=sF.memoryCheck(compAMem, setShuffled, indexesUsed)
        listInps=sF.computerInp(memCheckUp, compAMem, indexesUsed, setShuffled)
        
        firstPick=setShuffled[listInps[0]-1]
        secondPick=setShuffled[listInps[1]-1]
        print("\nFirst card:\t", circleList[listInps[0]-1], "➜", firstPick)
        print("Second card:\t", circleList[listInps[1]-1], "➜", secondPick)
        
        if firstPick[:-1]==secondPick[:-1]:
            print("\n'"+firstPick+"'", "and", "'"+secondPick+"'", "matches. Keep the streak going! ✔")
            circleList[listInps[0]-1]=firstPick
            circleList[listInps[1]-1]=secondPick
            
            indexesUsed.append(listInps[0])
            indexesUsed.append(listInps[1])
            p1Pairs+=1
            pairs+=1
            
        else:
            print("\nThey do not match. Better luck next time! ✘")
            p1Turn=False
            p2Turn=True
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
#Computer 2        
    while p2Turn==True:
        pAllList=[]
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        
        gameBoard=bF.layoutCards(circleList)
        playerNumber=gF.whoTurn(pAllList)
        gF.headerMulti(playerNumber, runs, p2Pairs)
        print(gameBoard)
        
        memCheckUp=sF.memoryCheck(compBMem, setShuffled, indexesUsed)
        listInps=sF.computerInp(memCheckUp, compBMem, indexesUsed, setShuffled)
        
        firstPick=setShuffled[listInps[0]-1]
        secondPick=setShuffled[listInps[1]-1]
        print("\nFirst card:\t", circleList[listInps[0]-1], "➜", firstPick)
        print("Second card:\t", circleList[listInps[1]-1], "➜", secondPick)

        if firstPick[:-1]==secondPick[:-1]:
            print("\n'"+firstPick+"'", "and", "'"+secondPick+"'", "matches. Keep the streak going! ✔")
            circleList[listInps[0]-1]=firstPick
            circleList[listInps[1]-1]=secondPick
            
            indexesUsed.append(listInps[0])
            indexesUsed.append(listInps[1])
            p2Pairs+=1
            pairs+=1
            
        else:
            print("\nThey do not match. Better luck next time! ✘")
            p1Turn=True
            p2Turn=False
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
               
    if pairs == 27:
        lastGameBoard=bF.layoutCards(circleList)
        print(lastGameBoard)
        print("\nGood job! All 27 pairs have been found in", runs-1, "runs!")
        print("Player 1:", p1Pairs, "| Player 2:", p2Pairs)
        break
