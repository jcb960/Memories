import time
#Made for easy access to all important files

print("▂"*63)
print(" "*14, "Welcome to 'Memories'")
print("▂"*63)
print("Options:")
print(" ♠1 - Single Player (No Computer)")
print(" ♣2 - Single Player (Against Computer)")
print(" ♥3 - Multiplayer (2 players)")
print(" ♦4 - Multiplayer (3 players)")
print(" ♠5 - Multiplayer (4 players)")
print(" ♣6 - Simulation (Quick Games | For data purposes)")
print(" ♥7 - Simulation LIVE (One Game)")
print(" ♦8 - Graphical Representation of data")
print("▂"*63)

while True: #Asks for a valid value until give one
    while True:
        try:
            modeInt=int(input("Choose the number correspondant to the modes above: "))
            break
        except ValueError:
            print("Only from 1 to 8. Try again:\n")
    if modeInt not in range(1, 9):       
        print("Only from 1 to 8. Try again:\n")
    else:
        break

print("Game Loading: ", end="") #For aesthetics, game loader
for y in range(23):
    print("✈", end="")
    if y<15:
        time.sleep(0.1)
    if y>19:
        time.sleep(0.5)
print()    
print("\n"*20)

#imports the corresponding games according to their accompanied label for easy use
if modeInt==1:
    import CsinglePNoComputer
elif modeInt==2:
    import DsinglePlayerVSComputer
elif modeInt==3:
    import Emulti2Player
elif modeInt==4:
    import Fmulti3Player
elif modeInt==5:
    import GmultiGPlayer
elif modeInt==6:
    import IsimulationQuickGames
elif modeInt==7:
    import JsimulationLIVEGame
elif modeInt==8:
    import LgraphicalRepresentation
    
print("\nThank you for making memories with 'Memories'!")
print("Until next time, see you! ♠♣♥♦") #♠♣♥♦
