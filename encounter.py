import gameObjects, time
from os import system
from msvcrt import getch
def main(anomaly,player):
    system("cls")
    anomaly.showFlavorText()
    anomaly.applyEffect(player)
    print("press any key to continue")
    getch()
    system("cls")
    player.getStats()
    print("press any key to continue")
    getch()
    return player
