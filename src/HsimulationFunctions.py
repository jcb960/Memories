import random #used for random choices if nothing correct appears in memory

def memoryCheck(memoryList, shuffledSet, usedNumbers): #memoryList = cards it picked
    state=False #state of having a pair in memoryList
    pickList=[] #the cards it's going to choose
    for index1 in range(len(memoryList)):
        pickOne=shuffledSet[memoryList[index1]-1]
        #Goes through the memoryList checking each possiblilty, [1, 2, 3, 4], so with 1, it check [1, 2], [1, 3] etc. then [2, 1]...
        
        for index2 in range(len(memoryList)):
            pickTwo=shuffledSet[memoryList[index2]-1]
            
            if index1!=index2: #To avoid picking the same card again, e.g. 8♦=8♦ which is not valid
                if pickOne[:-1]==pickTwo[:-1] and memoryList[index1] not in usedNumbers and memoryList[index2] not in usedNumbers:
                    #checks if they're valid and not used
                    pickList.append(memoryList[index1])
                    pickList.append(memoryList[index2])
                    state=True
                    break
        if state==True:
            break        
    pickList.append(state)
    return pickList

#Note that it has 100% memory, it remembers every card it chooses and doesn't repeat its cards unless to guess a pair
def computerInp(pickInfoList, memList, uNumbers, shuffleS):
    #Checks 4 Possibilities
    #If no pair is in its memoryList, it picks a random first choice
    #Then it does another memoryCheck to see if the first choice it chose gave a pair
    #If not, it's going to choose another random card
    #If it has found a pair, it will use the cards chosen from the memCheckUp function
    
    if pickInfoList[-1]==False: #False =state in memCheckUp, [-1] as it's always the last thing in the list
        while True: 
            randomInp1=random.randint(1, 54) #repeats randint until a valid option arises
            if randomInp1 in memList or randomInp1 in uNumbers:
                pass
            else:
                break
            
        if randomInp1 not in memList:    
            memList.append(randomInp1) #adds into memList
            
        memNow=memoryCheck(memList, shuffleS, uNumbers) #New memory check up with their first choice in its memory List
        if memNow[-1]==True: #If pair arises, it sets the new values for the pair
            randomInp1=memNow[0]
            randomInp2=memNow[1]
        else: #if not, get another random card
            while True:
                randomInp2=random.randint(1, 54)
                if randomInp2 in memList or randomInp2 in uNumbers:
                    pass
                else:
                    break
                
        if randomInp2 not in memList:
            memList.append(randomInp2) #Adds card into the memList       
    else:
        randomInp1=pickInfoList[0]
        randomInp2=pickInfoList[1] #If not(False), which means there is a pair in its memory List, it will just choose that
        #This situation only arises if the second card it chose, now made a pair with the cards in its memoryList
        
    inputList=[] #Final Inputs by computer ready to be used 
    inputList.append(randomInp1)
    inputList.append(randomInp2)
    return inputList
