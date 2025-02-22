import AbasicFunctions as bF
import BgameFunctions as gF
import time

circleList=['⓪①', '⓪②', '⓪③', '⓪④', '⓪⑤', '⓪⑥', '⓪⑦', '⓪⑧', '⓪⑨', '①⓪', '①①', '①②', '①③', '①④', '①⑤', '①⑥', '①⑦', '①⑧', '①⑨', '②⓪', '②①', '②②', '②③', '②④', '②⑤', '②⑥', '②⑦', '②⑧', '②⑨', '③⓪', '③①', '③②', '③③', '③④', '③⑤', '③⑥', '③⑦', '③⑧', '③⑨', '④⓪', '④①', '④②', '④③', '④④', '④⑤', '④⑥', '④⑦', '④⑧', '④⑨', '⑤⓪', '⑤①', '⑤②', '⑤③', '⑤④']            
setShuffled=bF.shuffleCards()

indexesUsed: list=[]

p1Turn=True
p2Turn=False
runs=1

p1Pairs=0
p2Pairs=0
pairs=0

while True:
#Player 1
    while p1Turn==True:
        pAllList=[]
        pAllList.append(p1Turn) #Explained in DsinglePlayerVSComputer
        pAllList.append(p2Turn)
            
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
            p2Turn=True
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
            p1Turn=True
            p2Turn=False
        time.sleep(3)
        print("\n"*20)
        runs+=1
            
        if pairs == 27:
            break
               
    if pairs == 27:
        print("\nGood job! All 27 pairs have been found in", runs-1, "runs!") #runs-1 because the next round is run has not happened
        print("Player 1:", p1Pairs, "| Player 2:", p2Pairs)
        break
