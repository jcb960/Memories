"""
Copyright (c) 2023, Colin J.B.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
"""

import random

"""
Set_S=["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠"]
Set_C=["A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"]
Set_H=["A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"]
Set_D=["A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"]
jokerSet=["JOKER", "JOKER"]
allSet=Set_S+Set_C+Set_H+Set_D+jokerSet

circleList1=["⓪①","⓪②","⓪③","⓪④","⓪⑤","⓪⑥","⓪⑦","⓪⑧","⓪⑨","①⓪","①①","①②","①③"]
circleList2=["①④","①⑤","①⑥","①⑦","①⑧","①⑨","②⓪","②①","②②","②③","②④","②⑤","②⑥"]
circleList3=["②⑦","②⑧","②⑨","③⓪","③①","③②","③③","③④","③⑤","③⑥","③⑦","③⑧","③⑨"]
circleList4=["④⓪","④①","④②","④③","④④","④⑤","④⑥","④⑦","④⑧","④⑨","⑤⓪","⑤①","⑤②"]
circleList5=["⑤③", "⑤④"]
circleList=['⓪①', '⓪②', '⓪③', '⓪④', '⓪⑤', '⓪⑥', '⓪⑦', '⓪⑧', '⓪⑨', '①⓪', '①①', '①②', '①③', '①④', '①⑤', '①⑥', '①⑦', '①⑧', '①⑨', '②⓪', '②①', '②②', '②③', '②④', '②⑤', '②⑥', '②⑦', '②⑧', '②⑨', '③⓪', '③①', '③②', '③③', '③④', '③⑤', '③⑥', '③⑦', '③⑧', '③⑨', '④⓪', '④①', '④②', '④③', '④④', '④⑤', '④⑥', '④⑦', '④⑧', '④⑨', '⑤⓪', '⑤①', '⑤②', '⑤③', '⑤④']            
"""

def shuffleCards():
    listCards=['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'JOKER', 'JOKER']
    
    #Randomizes the cards above in terms of index
    indexList: list=[]
    listOf54Cards: list= list(range(54))
    counter = 1
    while len(indexList) != len(listCards):
        randomIndex=random.randint(0, len(listCards)-counter)
        indexList.append(listOf54Cards[randomIndex])
        listOf54Cards.remove(listOf54Cards[randomIndex])
        counter+=1

    #Assigns the index values to the actual cards
    shuffledList=[]
    for loop1 in indexList:
        shuffledList.append(listCards[loop1])
    return shuffledList

def layoutCards(someList):
    #Prints a 7x7 grid, with an additional 5 cards
    stringList=""
    a=0
    b=7
    for loop2 in range(8):
        for loop3 in someList[a:b]:
            stringList+=(loop3+"\t")
        a=b
        if loop2==7: #Only happens when 7x7 grid is completed, then the 5 cards
            b+=5
        else:
            b+=7 #Adds the 7x7 grid
            stringList+="\n"
    return stringList
    
def inputPicks(usedNumbers, listForIndex): #usedNumbers and the shuffledSet
    #Conditions for the inputs taken by the user
    while True:
        while True:
            try:
                playerPick1=int(input("\nYour first card from 1 to 54: "))
                break
            except ValueError:
                print("No letters, decimals or other charachters. Try again:")
                
        if playerPick1 not in range(1, 55):
            print("Your card must be between 1 and 54. Try another:")
                
        elif playerPick1 in usedNumbers:
            print("That card has been already used. Try another:")
                
        else:
            print("You picked:", listForIndex[playerPick1-1])
            break
        
    while True:
        while True:
            try:
                playerPick2=int(input("\nYour second card from 1 to 54: "))
                break
            except ValueError:
                print("No letters, decimals or other charachters. Try again:")
                        
        if playerPick2 not in range(1, 55):
            print("Your card must be between 1 and 54. Try another:")
                
        elif playerPick2 in usedNumbers:
            print("That card has been used already. Try another:")
            
        elif playerPick2 == playerPick1:
            print("That card is your first pick. Try another:")
        else:
            print("You picked:", listForIndex[playerPick2-1])
            break
    
    inputPicksList=[] #Adds the valid picked inputs into a list to be sent away
    inputPicksList.append(playerPick1)
    inputPicksList.append(playerPick2)
    return inputPicksList
