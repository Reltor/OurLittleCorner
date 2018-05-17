import time
import random
import gameObjects
import art
ART = art.getArt("placeholdership")
def weakEnemy(NumOfEnemies):
    WList = []
    for a in range (NumOfEnemies):
        HP = random.randint(8,13)
        PHY = random.randint(13,18)
        ARM = random.randint(3,8)
        SPD = random.randint(13,18)
        ENG = random.randint(8,13)
        SHD = random.randint(13,18)
        LV = 0
        name = "Enemy Corvette"
        TempEnemy = gameObjects.Enemy(HP,PHY,ARM,SPD,ENG,SHD,LV,name,"")
        WList.append(TempEnemy)
    return WList

def medEnemy(NumOfEnemies):
    MList = []
    for b in range (NumOfEnemies):
        HP = random.randint(13,18)
        PHY = random.randint(8,18)
        ARM = random.randint(8,13)
        SPD = random.randint(8,13)
        ENG = random.randint(8,18)
        SHD = random.randint(8,13)
        LV = 1
        name = "Enemy Destroyer"
        TempEnemy = gameObjects.Enemy(HP,PHY,ARM,SPD,ENG,SHD,LV,name,"")
        MList.append(TempEnemy)
    return MList

def hardEnemy(NumOfEnemies):
    HList = []
    for c in range (NumOfEnemies):
        HP = random.randint(18,23)
        PHY = random.randint(13,18)
        ARM = random.randint(13,18)
        SPD = random.randint(3,8)
        ENG = random.randint(13,18)
        SHD = random.randint(3,8)
        LV = 2
        name = "Enemy Cruiser"
        TempEnemy = gameObjects.Enemy(HP,PHY,ARM,SPD,ENG,SHD,LV,name,"")
        HList.append(TempEnemy)
    return HList

def shEnemy(NumOfEnemies):
    SHList = []
    for d in range (NumOfEnemies):
        HP = random.randint(23,28)
        PHY = random.randint(15,18)
        ARM = random.randint(13,18)
        SPD = random.randint(1,1)
        ENG = random.randint(13,18)
        SHD = random.randint(1,3)
        LV = 3
        name = "Enemy Battleship"
        TempEnemy = gameObjects.Enemy(HP,PHY,ARM,SPD,ENG,SHD,LV,name,"")
        SHList.append(TempEnemy)
    return SHList

