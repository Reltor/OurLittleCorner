import time
import random
import gameObjects


def main():
    inventoryFile = open("inventory.inv","w")
    inventoryFile.close()
    Pclass = input("Please select a ship: >corvette >destroyer >cruiser >battle ship ")
    while(Pclass not in ("corvette","destroyer","cruiser","battle ship")):
        Pclass = input("-->")
    ShipName = input("Please name your ship: ")
    if ShipName == "Fire Fly":
        HP = 500
        PHY = 500
        ARM = 500
        SPD = 500
        ENG = 500
        SHD = 500
        encounter = 10
        #hero.save()
    else:
        if Pclass == "corvette":
            HP = random.randint(10,15)
            PHY = random.randint(15,20)
            ARM = random.randint(5,10)
            SPD = random.randint(15,20)
            ENG = random.randint(10,15)
            SHD = random.randint(15,20)
            encounter = 0
        elif Pclass == "destroyer":
            HP = random.randint(15,20)
            PHY = random.randint(10,20)
            ARM = random.randint(10,15)
            SPD = random.randint(10,15)
            ENG = random.randint(10,20)
            SHD = random.randint(10,15)
            encounter = 0
        elif Pclass == "cruiser":
            HP = random.randint(20,25)
            PHY = random.randint(15,20)
            ARM = random.randint(15,20)
            SPD = random.randint(5,10)
            ENG = random.randint(15,20)
            SHD = random.randint(5,10)
            encounter = 0
        elif Pclass == "battle ship":
            HP = random.randint(25,30)
            PHY = random.randint(17,20)
            ARM = random.randint(15,20)
            SPD = random.randint(0,3)
            ENG = random.randint(15,20)
            SHD = random.randint(1,5)
            encounter = 0
    hero = gameObjects.Player(HP,PHY,ARM,SPD,ENG,SHD,encounter,ShipName,Pclass)
    hero.getStats()
    #hero.save()
    return hero
