import EnemyCreator
import os
#cheatCODE - PlayerName - Firefly (sets moves to max, all stats as high as possible, enemy counter high enough for final boss, displays coordinate of final boss)

#################################
######## Enemy and Player #######
#################################

class Entity(object):
    def __init__(self,HP,PHY,ARM,SPD,ENG,SHD,name,art):
        #T0-DO - Make Below Private, add getters/setters
        self.HP = HP
        self.PHY = PHY
        self.ARM = ARM
        self.SPD = SPD
        self.ENG = ENG
        self.SHD = SHD
        self.name = name
        self.__art = art
        #TO-DO - Add Ascii and Location support
    #attributes from Entity Class----
            #attack
            #energy attack
            #armor
            #shields
            #name
            #speed
            #ascii art
            #location
    #methods
        #takePDamage() - taking normal attack damage
    def takePDamage(self,ePHY):
        damage = ePHY - self.ARM / 2
        if damage < 1:
            damage = 1
        self.HP = self.HP - damage
        print("enemy health = ",self.HP)
        #takeEDamage() - taking energy attack damage
    def takeEDamage(self,eENG):
        damage = eENG - self.SHD / 2
        if damage < 1:
            damage = 1
        self.HP = self.HP - damage
        print("enemy health = ",self.HP)
        #showStats() - Summary of statistics relevant to the player
    def getStats(self):
        print("HP = ",self.HP)
        print("PHY = ",self.PHY)
        print("ARM = ",self.ARM)
        print("SPD = ",self.SPD)
        print("ENG = ",self.ENG)
        print("SHD = ",self.SHD)
        #__str__() - Prints everything including background data - for debugging
    def getArt(self):
        placeholderArt = '''
| \
=[_|H)--._____
=[+--,-------'
 [|_/""  

'''
        return placeholderArt

class Enemy(Entity):
    def __init__(self,HP,PHY,ARM,SPD,ENG,SHD,LV,name,art = ""):
        super().__init__(HP,PHY,ARM,SPD,ENG,SHD,name,art)
        self.__LV = LV
        #attributes from Entity Class----
            #attack
            #energy attack
            #armor
            #shields
            #name
            #speed
            #ascii art
            #location
        #own attributes - TODO
            #dropChances
            #isBoss (y/n)
            #enemyClass (pick from a list)
            #enemy object
        #methods from Entity
            #takeEDamage()
            #takePDamage()
            #save
        #overwritten Methods
            #__str__
            #showStats() - No need to overwrite yet
    def getLV(self):
        return self.__LV
    def setLV(self,newLV):
        self.__LV = newLV

            
        
class Player(Entity):
    def __init__(self,HP,PHY,ARM,SPD,ENG,SHD,encounter,name,shipClass,art=""):
        super().__init__(HP,PHY,ARM,SPD,ENG,SHD,name,art)
        self.__shipClass = shipClass
        self.__encounters = encounter
        self.__location = (0,0)
        self.__name = name
            #attributes----
                #from Entity class
                    #attack (Corv - High, Destroyer - Medium, Cruiser - High, Battleship - High)
                    #energy attack (Corv - Medium, Destroyer - High, Cruiser - Mid, Battleship - Mid)
                    #armor (Corv - Super Low, Destroyer - Low, Cruiser - Mid, Battleship - Very High)
                    #shields (Corv - Medium, Destroyer - Medium, Cruiser - High, Battleship - High)
                    #name (Player Input)
                    #speed (Corv - Super High, Destroyer - High, Cruiser - Mid, Battleship Low)
                    #location
                #other
                    #inventory (Bottomless v1)
                    #ship class (Corvette, Destroyer, Cruiser, Battleship)
                    #movement range (1-4)
                    #num enemies defeated (used to see if you can fight the final boss yet)
                #methods from Entity
                    #takeEDamage()
                    #takePDamage()
                    #save
                #overwritten Methods
                    #__str__
                    #showStats()
    def getStats(self):
        super().getStats()
        print("Number of encounters = ",self.__encounters)
        print("Player Name: " + self.__name)
        print("Ship Class: " + self.__shipClass)
    def setLoc(self,coord):
        self.__location = coord
    def getLoc(self):
        return self.__location
    def getEncounters(self):
        return self.__encounters
    def encounter(self):
        self.__encounters += 1
        
class Boss(Entity):
    def __init__(self,HP,PHY,ARM,SPD,ENG,SHD,LV,name):
        super().__init__(HP,PHY,ARM,SPD,ENG,SHD,name)
        self.__LV = LV
        self.__phrase = ["YOU CAN NOT HURT ME!","MWAHAHA, YOU THINK THAT WILL WORK?","Ouch, I mean, THAT DID NOTHING!"]
    def sayJunk(self):
        phrase = 1
        print(self.__phrase[phrase])

#################################
######## Map Tiles ##############
#################################

class MapTile(object):
    def __init__(self,playerOcc = False,occupied = False,boss = False,asciiArt = "",location = (0,0)):
        ##### attributes #####
        #empty/occupied (is there an enemy or anomaly here)
        self.__occupied = occupied
        #player occupied (y/n)
        self.__playerOccupied = playerOcc
        #is the boss here (y/n)
        self.__bossOccupied = boss
        #location (x,y coordinate)
        self.__location = location
        #ascii art
        self.__asciiArt = asciiArt
    def __str__ (self):
        if self.__playerOccupied == True:
            return "P"
        else:
            return "M"
    def getLoc(self):
        return self.__location
    def setPlayer(self,boolean):
        self.__playerOccupied = boolean
class AnomalyTile(MapTile):
    def __init__(self,anomaly,occupied = True, player = False, boss = False, asciiArt = "",location = (0,0)):
        super().__init__(occupied,player,boss,asciiArt,location)
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here (n)
                #location
                #ascii art
        #### seperate attributes ####
        self.__anomaly = anomaly
    def getAnomaly(self):
        return self.__anomaly
    def __str__(self):
        return "A"
        
class BlackHoleTile(AnomalyTile):
    def __init__(self,anomaly,occupied = True, player = False, boss = False,asciiArt = "",location = (0,0)):
        super().__init__(anomaly,occupied,player,boss,asciiArt,location)
        #attributes from AnomalyTile
            #empty/occupied (occupied)
            #player occupied (y/n)
            #is the boss here (n)
            #location
            #ascii art
        #seperate attributes
            #killPlayer()
        #use setHP() method on Entity class to kill player
        pass
    def __str__(self):
        return "H"
    
class EnemyTile(MapTile):
    def __init__(self,enemy,occupied = True,player = False,boss = False,asciiArt = "",location = (0,0)):
        super().__init__(occupied,player,boss,asciiArt,location)
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(n)
                #location
                #ascii art
        self.__enemy = enemy #enemy object
    def __str__(self):
        return "E"
    def getEnemy(self):
        return self.__enemy
    def removeEnemy(self):
        self.__enemy = None
class BossTile(MapTile):
    def __init__(self,boss="",occupied = True,player = False,bossOcc = True,asciiArt = "",location = (0,0)):
        super().__init__(occupied,player,bossOcc,asciiArt,location)
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(y)
                #location
                #ascii art
            #seperate
                #boss dialogue
                    #ready to encounter dialogue
                    #not ready (go away) dialogue
        HP = 34
        PHY = 21
        ARM = 21
        SPD = 1
        ENG = 21
        SHD = 5
        LV = 4
        name = "Boss"
        art = ""
        TempEnemy = Enemy(HP,PHY,ARM,SPD,ENG,SHD,LV,name,art)

        self.__boss = TempEnemy
    def __str__(self):
        return "B"
    def getBoss(self):
        return self.__boss
class PlayerTile(MapTile):
    def __init__(self,player,occupied = True,playerOcc = True,boss = False,asciiArt = "",location = (0,0)):
        super().__init__(occupied,playerOcc,boss,asciiArt,location)
        #attributes from MapTile
            #empty/occupied (occupied)
            #player occupied (y)
            #is the boss here(n)
            #location
            #ascii art
        self.__player = player
    def __str__(self):
        return "P"
        
class Board(object):
    def __init__(self,rowList):
        #takes a list of rows of map objects
        self.__board = rowList
        self.yLen = len(rowList)
        self.xLen = len(rowList[1])
    def getBoard(self):
        #returns the whole board
        return self.__board
    def printBasicBoard(self,oswidth):
        #prints a basic graphic representation of the board
        rowSep = "-------------------------------"
        for row in self.__board:
            print(rowSep.center(oswidth))
            rowString = "| "
            for column in row:
                rowString += str(column)
                rowString += " | "
            print(rowString.center(oswidth))
        print(rowSep.center(oswidth))
    def setTile(self,xCoord,yCoord,newTile):
        #replaces a tile at the given coordinates with a new tile
        #useful if an enemy dies, or an anomaly is cleared
        #or literally any time the player changes position
        self.__board[yCoord-1][xCoord-1] = newTile
    def getTile(self,xCoord,yCoord):
        return self.__board[yCoord-1][xCoord-1]
    def addPlayer(self,coord):
        tile = self.__board[coord[1]-1][coord[0]-1]
    def removePlayer(self,coord):
        tile = self.__board[coord[1]-1][coord[0]-1]
    def getY(self):
        return self.yLen
    def getX(self):
        return self.xLen
#################################
######## Misc Objects ###########
#################################            
    
class Anomaly(object):
    def __init__(self,effectItem,flavorText,art):
        self.__item = effectItem
        self.__flavorText = flavorText
        self.__art = art
    def getArt(self):
        return self.__art
    def get(self):
        return self.__item
    def showFlavorText(self):
        print(self.__flavorText)
    def applyEffect(self,player):
        player = self.__item.boostStat(player)
        return player
    
        


        
