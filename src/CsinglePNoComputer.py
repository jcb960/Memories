"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
"""

import AbasicFunctions as bF
import BgameFunctions as gF
import time

#Indexes in circle for aesthetics
circleList=['⓪①', '⓪②', '⓪③', '⓪④', '⓪⑤', '⓪⑥', '⓪⑦', '⓪⑧', '⓪⑨', '①⓪', '①①', '①②', '①③', '①④', '①⑤', '①⑥', '①⑦', '①⑧', '①⑨', '②⓪', '②①', '②②', '②③', '②④', '②⑤', '②⑥', '②⑦', '②⑧', '②⑨', '③⓪', '③①', '③②', '③③', '③④', '③⑤', '③⑥', '③⑦', '③⑧', '③⑨', '④⓪', '④①', '④②', '④③', '④④', '④⑤', '④⑥', '④⑦', '④⑧', '④⑨', '⑤⓪', '⑤①', '⑤②', '⑤③', '⑤④']            
setShuffled=bF.shuffleCards()
indexesUsed: list=[]

runs=1 #Runs start from 1 not 0, this is the game round
pairs=0 #Pairs found by the player
while True: #While loop until the 27 pairs has been found
    gameBoard=bF.layoutCards(circleList) #Game board
    gF.headerSingle(runs, pairs) #The header
    print(gameBoard)
    
    itemsCollected=gF.gameInAction(setShuffled, indexesUsed) #Goes to the main function in BgameFunctions file
    firstIndex=itemsCollected[0]-1 #itemsCollected[0] is the first index
    secondIndex=itemsCollected[1]-1 #itemsCollected[1] is the second index
    
    firstPick=setShuffled[firstIndex]
    secondPick=setShuffled[secondIndex] #Sets again the cards corresponding to the indexes chosen
    
    if itemsCollected[2] == True: #itemCollected[2] is the winState
        circleList[firstIndex]=firstPick #Replaces the position in the game board with the correct cards
        circleList[secondIndex]=secondPick
        pairs+=1
    runs+=1

    time.sleep(3) #Stops for 3 seconds to remember the cards chosen
    print("\n"*20) #Pushes the previous board out of the way
    
    if pairs == 27: #27 pairs is the max you could get and results in an end of the game
        print("\nGood job! You found all 27 pairs in", runs-1, "runs!")
        break
