import time
import random
import gameObjects
import EnemyCreator
import CharCreator
import items
from os import system
import os

itemList = items.createItems()
def combat(enemy,player):
    system("cls")
    print()
    print("An",enemy.name,"appears!")
    print("---------------------")
    print("Your Stats:")
    print("---------------------")
    player.getStats()
    time.sleep(1)
    print("")
    print("---------------------")
    print("Enemy Stats:")
    print("---------------------")
    enemy.getStats()
    if enemy.SPD > player.SPD:
        curTurn = "Enemy"
    elif player.SPD > enemy.SPD:
        curTurn = "Player"
    else:
        if random.randint(1,2) == 1:
            curTurn = "Player"
        else:
            curTurn = "Enemy"
    fled = False
    while player.HP > 0 and enemy.HP > 0 and not fled:
        if curTurn == "Player":
            print("Choose Your Action!")
            print("---------------------")
            print()
            print(">Physical    >Energy    >Flee    >Item")
            print()
            print (enemy.getArt())
            selection = ""
            while(selection not in ("Physical","Energy","Flee","Item")):
                selection = input("-->").title()
                if selection == "Physical":
                    print("You attack the",enemy.name,"with physical weapons")
                    time.sleep(1)
                    enemy.takePDamage(player.PHY)
                    curTurn = "Enemy"
                elif selection == "Energy":
                    print("You use energy weapons on the",enemy.name)
                    time.sleep(1)
                    enemy.takeEDamage(player.ENG)
                    curTurn = "Enemy"
                elif selection == "Item":
                    print("Pick an item to use: ")
                    player,curTurn = items.inventory(player)
                elif selection == "Flee":
                    if enemy.SPD != 1337:
                        roll = random.randint(1,100)
                        if player.SPD > enemy.SPD:
                            fleeChance = 90
                        else:
                            fleeChance = 50
                        if roll <= fleeChance:
                            print("-----------")
                            print("you Fled")
                            print("-----------")
                            fled = True
                            time.sleep(1)
                        else:
                            print("failed to flee")
                            time.sleep(1)
                            curTurn = "Enemy"
                    else:
                        print("failed to flee")
                        time.sleep(1)
        elif curTurn == "Enemy":
            atType = random.randint(1,100)
            if enemy.PHY >= enemy.ENG:
                if atType > 10:
                    print("The",enemy.name,"attacks with physical weapons!")
                    time.sleep(1)
                    player.takePDamage(enemy.PHY)
                else:
                    print("The",enemy.name,"uses energy weapons!")
                    time.sleep(1)
                    player.takeEDamage(enemy.ENG)
            elif enemy.PHY < enemy.ENG:
                if atType > 10:
                    print("The",enemy.name,"uses energy weapons!")
                    time.sleep(1)
                    player.takeEDamage(enemy.ENG)
                else:
                    print("The",enemy.name,"attacks with physical weapons!")
                    time.sleep(1)
                    player.takePDamage(enemy.PHY)
            else:
                print("An Error Occured...")
            curTurn = "Player"
    if player.HP <= 0:
        print("-----------------")
        print("You Died")
        print("-----------------")
        playerRes = "L"
    elif fled == True:
        playerRes = "R"
        pass
    else:
        player.encounter()
        ranDrop = random.randint(0,5)
        level = enemy.getLV()
        pickedItem = itemList[ranDrop][level]
        items.addItem(pickedItem)
        time.sleep(1.5)
        system("cls")
        print()
        print()
        print()
        oswidth = os.get_terminal_size().columns

        print("Item Drop Acquired!".center(oswidth))
        print("--------------------------".center(oswidth))
        string = "You got " + pickedItem.name
        print(string.center(oswidth))
        print("--------------------------".center(oswidth))
        time.sleep(3)
        playerRes = "W"
    return player, playerRes

def main():
    enemy = EnemyCreator.medEnemy(1)[0]
    player = CharCreator.main()
    combat(enemy,player)

