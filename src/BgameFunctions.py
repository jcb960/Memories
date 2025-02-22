"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
"""

import AbasicFunctions as bF #Imports the file's functions to be used here

def headerSingle(counter, pairsFound):
    #For single Player
    #Prints the header with the counter of the game and Pairs found by the player
    print("▂"*63)
    print(" "*9, "Run Number:", counter, "| Pairs Found:", pairsFound)
    print("▂"*63)
    
def headerMulti(turn, counter, pairsFound):
    #For multiplayer
    #Prints the header with the counter of the game and Pairs found by the player
    print("▂"*63)
    print("Player",str(turn+1)+"'s Turn", "| Run Number:", counter, "| Pairs Found:", pairsFound)
    print("▂"*63)

def whoTurn(listStates):
    #To be displayed in the headerMulti to show who's turn is it
    for x in range(len(listStates)):
        if listStates[x]==True:
            break
    return x        

def gameInAction(shuffledCards, indexL):
    #For single and multi players game mode
    winState=False
    listInputs=bF.inputPicks(indexL, shuffledCards)
    firstIndex=listInputs[0]-1 #-1 because in python, it starts from 0 not 1, and the board starts from 1
    secondIndex=listInputs[1]-1
    
    firstPick=shuffledCards[firstIndex] #Their first card
    secondPick=shuffledCards[secondIndex] #Their second card
    
    if firstPick[:-1]==secondPick[:-1]: #Compares the charachters from the start index all the way to the second last index inclusive
        indexL.append(listInputs[0]) #Adds the values into the used index list if correct
        indexL.append(listInputs[1])
        winState=True
        
        print("\n'"+firstPick+"'", "and", "'"+secondPick+"'", "matches. Keep the streak going! ✔")
    else:
        print("\nThey do not match. Better luck next time! ✘")
    
    itemsToTransfer=[] #The list containing the chosen indexes and the state of winState
    itemsToTransfer.append(listInputs[0])
    itemsToTransfer.append(listInputs[1])
    itemsToTransfer.append(winState)
    
    return itemsToTransfer
