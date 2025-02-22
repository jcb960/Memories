import AbasicFunctions as bF
import BgameFunctions as gF
import time

#Player 1 goes first, then player 2, then player 3, then player 4, then back to player 1

circleList=['⓪①', '⓪②', '⓪③', '⓪④', '⓪⑤', '⓪⑥', '⓪⑦', '⓪⑧', '⓪⑨', '①⓪', '①①', '①②', '①③', '①④', '①⑤', '①⑥', '①⑦', '①⑧', '①⑨', '②⓪', '②①', '②②', '②③', '②④', '②⑤', '②⑥', '②⑦', '②⑧', '②⑨', '③⓪', '③①', '③②', '③③', '③④', '③⑤', '③⑥', '③⑦', '③⑧', '③⑨', '④⓪', '④①', '④②', '④③', '④④', '④⑤', '④⑥', '④⑦', '④⑧', '④⑨', '⑤⓪', '⑤①', '⑤②', '⑤③', '⑤④']            
setShuffled=bF.shuffleCards()

indexesUsed: list=[]

p1Turn=True
p2Turn=False
p3Turn=False
p4Turn=False
runs=1

p1Pairs=0
p2Pairs=0
p3Pairs=0
p4Pairs=0
pairs=0

while True:
#Player 1
    while p1Turn==True:
        pAllList=[] #same concept but with 4 states
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        pAllList.append(p3Turn)
        pAllList.append(p4Turn)
            
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
            
        else:
            p1Turn=False
            p2Turn=True #activates player 2's turn while deactivating player 1's turn
            p3Turn=False
            p4Turn=False
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
#Player 2        
    while p2Turn==True:
        pAllList=[]
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        pAllList.append(p3Turn)
        pAllList.append(p4Turn)
            
        gameBoard=bF.layoutCards(circleList)
        playerNumber=gF.whoTurn(pAllList)
        gF.headerMulti(playerNumber, runs, p2Pairs)
        print(gameBoard)
    
        itemsCollected=gF.gameInAction(setShuffled, indexesUsed)
        firstIndex=itemsCollected[0]-1
        secondIndex=itemsCollected[1]-1
    
        firstPick=setShuffled[firstIndex]
        secondPick=setShuffled[secondIndex]
    
        if itemsCollected[2] == True:
            circleList[firstIndex]=firstPick
            circleList[secondIndex]=secondPick
            p2Pairs+=1
            pairs+=1
            
        else:
            p1Turn=False
            p2Turn=False
            p3Turn=True #activates player 3's turn while deactivating player 2's turn
            p4Turn=False
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
#Player 3        
    while p3Turn==True:
        pAllList=[]
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        pAllList.append(p3Turn)
        pAllList.append(p4Turn)
            
        gameBoard=bF.layoutCards(circleList)
        playerNumber=gF.whoTurn(pAllList)
        gF.headerMulti(playerNumber, runs, p3Pairs)
        print(gameBoard)
    
        itemsCollected=gF.gameInAction(setShuffled, indexesUsed)
        firstIndex=itemsCollected[0]-1
        secondIndex=itemsCollected[1]-1
    
        firstPick=setShuffled[firstIndex]
        secondPick=setShuffled[secondIndex]
    
        if itemsCollected[2] == True:
            circleList[firstIndex]=firstPick
            circleList[secondIndex]=secondPick
            p3Pairs+=1
            pairs+=1
            
        else:
            p1Turn=False
            p2Turn=False
            p3Turn=False
            p4Turn=True #activates player 4's turn while deactivating player 3's turn
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
#Player 4    
    while p4Turn==True:
        pAllList=[]
        pAllList.append(p1Turn)
        pAllList.append(p2Turn)
        pAllList.append(p3Turn)
        pAllList.append(p4Turn)
            
        gameBoard=bF.layoutCards(circleList)
        playerNumber=gF.whoTurn(pAllList)
        gF.headerMulti(playerNumber, runs, p4Pairs)
        print(gameBoard)
    
        itemsCollected=gF.gameInAction(setShuffled, indexesUsed)
        firstIndex=itemsCollected[0]-1
        secondIndex=itemsCollected[1]-1
    
        firstPick=setShuffled[firstIndex]
        secondPick=setShuffled[secondIndex]
    
        if itemsCollected[2] == True:
            circleList[firstIndex]=firstPick
            circleList[secondIndex]=secondPick
            p4Pairs+=1
            pairs+=1
            
        else:
            p1Turn=True #activates player 1's turn while deactivating player 4's turn
            p2Turn=False
            p3Turn=False
            p4Turn=False
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
               
    if pairs == 27:
        print("\nGood job! All 27 pairs have been found in", runs-1, "runs!")
        print("Player 1:", p1Pairs, "| Player 2:", p2Pairs, "| Player 3:", p3Pairs, "| Player 4:", p4Pairs)
        break
