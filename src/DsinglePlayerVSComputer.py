"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
"""

import AbasicFunctions as bF
import BgameFunctions as gF
import HsimulationFunctions as sF
import time

#Rule: If a player get's a pair correct, it's still their turn

circleList=['⓪①', '⓪②', '⓪③', '⓪④', '⓪⑤', '⓪⑥', '⓪⑦', '⓪⑧', '⓪⑨', '①⓪', '①①', '①②', '①③', '①④', '①⑤', '①⑥', '①⑦', '①⑧', '①⑨', '②⓪', '②①', '②②', '②③', '②④', '②⑤', '②⑥', '②⑦', '②⑧', '②⑨', '③⓪', '③①', '③②', '③③', '③④', '③⑤', '③⑥', '③⑦', '③⑧', '③⑨', '④⓪', '④①', '④②', '④③', '④④', '④⑤', '④⑥', '④⑦', '④⑧', '④⑨', '⑤⓪', '⑤①', '⑤②', '⑤③', '⑤④']            

setShuffled=bF.shuffleCards()

indexesUsed: list=[]
compBMem: list=[] #Computer's Memory

#True = It's their turn
#False = It's not their their turn

p1Turn=True 

p2Turn=False

runs=1

p1Pairs=0
p2Pairs=0
pairs=0 #Total pairs found

while True:
#Player
    while p1Turn==True:
        pAllList=[] # This list is to determine who's turn is it
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        
        #playerNumber will determine what position the 'True' is, [False, True], True is at index 1, so index+1, 1+1=2, so player 2's turn
        
        gameBoard=bF.layoutCards(circleList)
        playerNumber=gF.whoTurn(pAllList)
        gF.headerMulti(playerNumber, runs, p1Pairs)
        print(gameBoard)
        
        itemsCollected=gF.gameInAction(setShuffled, indexesUsed)
        
        firstIndex=itemsCollected[0]-1
        secondIndex=itemsCollected[1]-1
    
        firstPick=setShuffled[firstIndex]
        secondPick=setShuffled[secondIndex]
    
        if itemsCollected[2] == True:            
            circleList[firstIndex]=firstPick
            circleList[secondIndex]=secondPick
            p1Pairs+=1
            pairs+=1
            #If guessed correctly, this while loops keeps repeating
        else:
            #If guessed incorrectly, this switches of their turn and switches on player 2's Turn and moves on to player 2's while loop
            p1Turn=False
            p2Turn=True
        runs+=1
        
        time.sleep(3)
        print("\n"*20)              

        if pairs == 27: #Checks if the game ended
            break
#Computer      
    while p2Turn==True:
        pAllList=[] #Explained with Player 1
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        
        gameBoard=bF.layoutCards(circleList)
        playerNumber=gF.whoTurn(pAllList)
        gF.headerMulti(playerNumber, runs, p2Pairs)
        print(gameBoard)
        
        memCheckUp=sF.memoryCheck(compBMem, setShuffled, indexesUsed) #Checks if a pair has been found using the cards it remembers
        listInps=sF.computerInp(memCheckUp, compBMem, indexesUsed, setShuffled) #Chooses a pair based on its memory of cards it picked
        
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
            #Repeats Computer's turn if guessed correctly, computer gets another turn
        else:
            print("\nThey do not match. Better luck next time! ✘")
            p1Turn=True
            p2Turn=False
            #Player 1 Turns swtiches on and Computer's Turn switches Off
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
        
    if pairs == 27:
        lastGameBoard=bF.layoutCards(circleList) #Final game board with all cards shown
        print(lastGameBoard)
        print("\nGood job! All 27 pairs have been found in", runs-1, "runs!")
        print("Player 1:", p1Pairs, "| Player 2:", p2Pairs)
        break
       