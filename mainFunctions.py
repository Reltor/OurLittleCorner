from os import system
from msvcrt import getch
import random, gameObjects, CharCreator, EnemyCreator, combat, items, pickle, logging, time, encounter, bossCombat, anomalyCreator, os

#################################
######## Creator Functions ######
#################################
def generateCoordinates(coordList,numCoordinates,boardX,boardY):
    newCoords = []
    for point in range(numCoordinates):
        validCoord = False
        while not validCoord:
            xCoord = random.randint(1,boardX)
            yCoord = random.randint(1,boardX)
            coordPair = (xCoord,yCoord)
            if coordPair not in coordList:
                coordList.append(coordPair)
                newCoords.append(coordPair)
                validCoord = True
            else:
                validCoord = False
    return newCoords

def createBoard(rows,columns,player): #rework player placement
    #create a board of size x size dimensions via nested lists.
    rowList = []
    for row in range(rows):
        columnList = []
        for column in range(columns):
            columnList.append("")
        rowList.append(columnList)
    numEnemies = random.randint(4,8) #number range currently hardcoded, want to change
    masterCoordList = []
    
    enemyCoordList = generateCoordinates(masterCoordList[:],numEnemies,columns,rows)
    for coord in enemyCoordList:
        masterCoordList.append(coord)
        
    numAnomalies = random.randint(4,8)
    anomalyCoordList = generateCoordinates(masterCoordList[:],numAnomalies,columns,rows)
    for coord in anomalyCoordList:
        masterCoordList.append(coord)
        
    #create enemy or anomaly tiles for those points
    for coord in enemyCoordList:
        enemyTile = createEnemyTile(coord)
        rowList[coord[1]-1][coord[0]-1] = enemyTile
        
    for coord in anomalyCoordList:
        anomalyTile = createAnomalyTile(coord)
        rowList[coord[1]-1][coord[0]-1] = anomalyTile
        
    #randomly place one "major/boss" enemy at another points
    bossCoord = generateCoordinates(masterCoordList[:],1,columns,rows)[0]
    masterCoordList.append(bossCoord)
    bossTile = gameObjects.BossTile()
    rowList[bossCoord[1]-1][bossCoord[0]-1] = bossTile
    
    #random chance for a black hole, insta-death at another point
    blackHoleChance = 10
    blackHoleInt = random.randint(0,blackHoleChance)
    if blackHoleInt == 1:
        anomalyFile = open("anomaly.anome")
        pickle.load(anomalyFile)
        blackHole = pickle.load(anomalyFile)
        anomalyFile.close()
        blackHoleTile = gameObjects.BlackHoleTile(anomaly)
        blackHoleCoord = generateCoordinates(masterCoordList[:],1,columns,rows)[0]
        rowList[coord[1]-1][coord[0]-1] = blackHoleTile
    
    #place the player
    playerTile = gameObjects.MapTile(playerOcc = True) #create the tile with the player
    playerCoord = generateCoordinates(masterCoordList[:],1,columns,rows)[0]
    player.setLoc(playerCoord)
    masterCoordList.append(playerCoord)
    #print("player at: " + str(playerCoord))
    time.sleep(1)
    rowList[playerCoord[1]-1][playerCoord[0]-1] = playerTile #place it on the board
    
    #create empty tiles for all other points
    for row in rowList:
        for tile in row:
            if type(tile) is str:
                tileIndex = row.index(tile)
                row[tileIndex] = gameObjects.MapTile()
    gameBoard = gameObjects.Board(rowList)
    oswidth = os.get_terminal_size().columns
    gameBoard.printBasicBoard(oswidth)
    
    return gameBoard


def createEnemyTile(coord):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    SUPERHARD = 4
    enemyClass = random.randint(1,4)
    if enemyClass == EASY:
        newEnemy = EnemyCreator.weakEnemy(1)[0]
    elif enemyClass == MEDIUM:
        newEnemy = EnemyCreator.medEnemy(1)[0]
    elif enemyClass == HARD:
        newEnemy = EnemyCreator.hardEnemy(1)[0]
    elif enemyClass == SUPERHARD:
        newEnemy = EnemyCreator.shEnemy(1)[0]
    #finish adding other enemy types
    enemyTile = gameObjects.EnemyTile(newEnemy, location = coord)
    return enemyTile

def createAnomalyTile(coord):
    #load anomaly definitions file
    anomalyImport =  open("anomaly.anome","rb")
    anomalyList = pickle.load(anomalyImport)
    anomaly = random.choice(anomalyList)
    anomalyImport.close()
    #randomly select one and load its object (pickle)
    anomalyTile = gameObjects.AnomalyTile(anomaly,location = coord)
    #return the object
    return anomalyTile



#################################
##### Gameplay Functions ########
#################################
    
def move(board,player,num):
    UP = 72
    DOWN = 80
    LEFT = 75 
    RIGHT = 77
    valid = False
    if num == UP:
        oldCoord = player.getLoc()
        newY = player.getLoc()[1] - 1
        if newY > 0 and newY <= board.getY():
            newCoord = (player.getLoc()[0],newY)
            player.setLoc(newCoord)
            oldTile = board.getTile(oldCoord[0],oldCoord[1])
            oldTile.setPlayer(False)
            board.setTile(oldCoord[0],oldCoord[1],oldTile)
            newTile = board.getTile(newCoord[0],newCoord[1])
            newTile.setPlayer(True)
            board.setTile(newCoord[0],newCoord[1],newTile)
            valid = True
    elif num == DOWN:
        oldCoord = player.getLoc()
        newY = player.getLoc()[1] + 1
        if newY > 0 and newY <= board.getY():
            newCoord = (oldCoord[0],newY)
            player.setLoc(newCoord)
            oldTile = board.getTile(oldCoord[0],oldCoord[1])
            oldTile.setPlayer(False)
            board.setTile(oldCoord[0],oldCoord[1],oldTile)
            newTile = board.getTile(newCoord[0],newCoord[1])
            newTile.setPlayer(True)
            board.setTile(newCoord[0],newCoord[1],newTile)
            valid = True
    elif num == LEFT:
        oldCoord = player.getLoc()
        newX = player.getLoc()[0] - 1
        if newX > 0 and newX <= board.getX():
            newCoord = (newX,player.getLoc()[1])
            player.setLoc(newCoord)
            oldTile = board.getTile(oldCoord[0],oldCoord[1])
            oldTile.setPlayer(False)
            board.setTile(oldCoord[0],oldCoord[1],oldTile)
            newTile = board.getTile(newCoord[0],newCoord[1])
            newTile.setPlayer(True)
            board.setTile(newCoord[0],newCoord[1],newTile)
            valid = True
    elif num == RIGHT:
        oldCoord = player.getLoc()
        newX = player.getLoc()[0] + 1
        if newX > 0 and newX <= board.getX():
            newCoord = (newX,player.getLoc()[1])
            player.setLoc(newCoord)
            oldTile = board.getTile(oldCoord[0],oldCoord[1])
            oldTile.setPlayer(False)
            board.setTile(oldCoord[0],oldCoord[1],oldTile)
            newTile = board.getTile(newCoord[0],newCoord[1])
            newTile.setPlayer(True)
            board.setTile(newCoord[0],newCoord[1],newTile)
            valid = True
    if valid == True:
        #print("called move")
        #print("player was at" + str(oldCoord))
        #print("player now at" + str(newCoord))
        #print("loc variable reads" + str(player.getLoc()))
        pass
    return board,player
def moveAway(board,player):
    UP = 72
    DOWN = 80
    LEFT = 75 
    RIGHT = 77
    oldCoord = player.getLoc()
    ordList = [UP,DOWN,LEFT,RIGHT]
    if oldCoord[0] >= board.getX():
        ordList.remove(RIGHT)
    if oldCoord[0] <= 0:
        ordList.remove(LEFT)
    if oldCoord[1] >= board.getY():
        ordList.remove(DOWN)
    if oldCoord[1] <= 0:
        ordList.remove(UP)
    direction = random.choice(ordList)
    board,player = move(board,player,direction)
    safe = False
    while not safe:
        
        newCoord = player.getLoc()
        currentTile = board.getBoard()[newCoord[1]-1][newCoord[0]-1]
        if not isinstance(currentTile,gameObjects.AnomalyTile) and not isinstance(currentTile,gameObjects.EnemyTile):
            safe = True
        else:
            board,player = moveAway(board,player)
    return board,player
def save(board,player):
##    in1 = int(input("Where is the boss"))
##    in2 = int(input("Where is the boss"))

    pickle_out = open("test.save","wb")
    #playerLoc = playerT.getLoc()
##    boardDataList = boardT.getTile(in1,in2).getEnemy()
##    print(boardDataList)
##    time.sleep(10)
    pickle.dump(board,pickle_out)
    pickle.dump(player,pickle_out)

    pickle_out.close()


def load(fileName):
    fileName = "test.save"
    pickle_in = open(fileName,"rb")
    board = pickle.load(pickle_in)
    player = pickle.load(pickle_in)
                          
    return board, player
#################################
############# Main ##############
#################################

def main():


    try:
        oswidth = os.get_terminal_size().columns
        validResponse = False
        while not validResponse:
            loadSave = str(input("Would you like to load an existing save? [Y/N]? "))
            if loadSave == "Y" or loadSave == "N":
                validResponse = True
            else:
                print("That is not yes or no")
        if loadSave == "N":
            print("Beginning Game")
            player = CharCreator.main()
            board = createBoard(7,7,player)
        elif loadSave == "Y":
            fileName = str(input("Input Saved Game's FileName: "))
            board,player = load(fileName + ".sav")
            board.printBasicBoard(oswidth)
        openingBanner =  '''

####################################################################################
                 WELCOME TO OUR LITTLE CORNER OF THE GALAXY
###################################################################################


YOUR GOAL IS TO DESTROY THE FINAL BOSS, LOCATED SOMEWHERE IN THE GALAXY (B)
You may Encounter
Anomalies (A) which will apply effects to your ship
Enemies (E) to fight
Or just lots of empty space (M)

You may pick up items along your travels, these will not automatically apply but must be used in battle or on the map screen.


'''
        
        system("cls")
        print(openingBanner.center(oswidth))
        print("Press Any Key to continue")
        key = ord(getch())
       
    #main - handles the overarching game
        #load save (y/n)?
        #if no
            #create the player
            #create the board
        #if yes, load given save file.
            #check to make sure the file is a pickle file containing a legit save.
            #display the board
            #display character stats and other relevant info

        playerWon = False
        playerDead = False
        
        SPECIALCHAR = 100
        UP = 72
        DOWN = 80
        LEFT = 75 
        RIGHT = 77
        Q = 113
        S = 115
        I = 105
        D = 100
        T = 116
        ordList = [SPECIALCHAR,UP,DOWN,LEFT,RIGHT,Q,S,I,D,T,224]

        while not playerWon and not playerDead:
        #check if the player has won, or is dead. if either is true move to the appropriate endGame function, else move on
            system("cls")
            board.printBasicBoard(oswidth)
            print("Use the Arrow Keys to move, Q to Quit, S to Save, I to access inventory, or D to access stats: ".center(oswidth))

            currentLoc = player.getLoc()
            startTile = board.getBoard()[currentLoc[1]-1][currentLoc[0]-1]

            playerChoice = ord(getch())
            if playerChoice in ordList:
                if playerChoice == 224:
                    playerMove = ord(getch())
                    board, player = move(board,player,playerMove)
                    newCoord = player.getLoc()
                    currentTile = board.getBoard()[newCoord[1]-1][newCoord[0]-1]
                    if isinstance(currentTile,gameObjects.EnemyTile):
                        player,combatResolution = combat.combat(currentTile.getEnemy(),player)
                        if combatResolution == "W":
                            currentTile.removeEnemy()
                            board.setTile(newCoord[0],newCoord[1],gameObjects.MapTile(playerOcc = True))
                        elif combatResolution == "L":
                            playerDead = True
                            break
                        elif combatResolution == "R":
                            board,player = moveAway(board,player)
                        time.sleep(2)
                    elif isinstance(currentTile,gameObjects.BossTile):
                        encountersNeeded = 5
                        if player.getEncounters() >= 5:
                            player,combatResolution = bossCombat.combat(currentTile.getBoss(),player)
                            if combatResolution == "W":
                                playerWon = True
                                break
                            elif combatResolution == "L":
                                playerLost = True
                                break
                        else:
                            print("You are not yet strong enough to face the boss, you must prove your mettle against at least 5 enemies first")
                            moveAway(board,player)
                    elif isinstance(currentTile,gameObjects.AnomalyTile):
                        anomaly = currentTile.getAnomaly()
                        player = encounter.main(anomaly,player)
                        board.setTile(newCoord[0],newCoord[1],gameObjects.MapTile(playerOcc = True))
                elif playerChoice == I:
                    player,curTurn = items.inventory(player)
                elif playerChoice == Q:
                    print("Press Q to quit immediately or S to save first")
                    playerChoice = ord(getch())
                    if playerChoice == Q:
                        break
                    elif playerChoice == S:
                        save(board,player)
                elif playerChoice == S:
                    save(board,player)
                    system("cls")
                    print("Game Saved")
                    print("Press Any Key to Exit")
                    key = ord(getch())
                    #command to close window
                    break
                elif playerChoice == D:
                    player.getStats()
                    print("------------")
                    input("Press Enter to Continue")
                elif playerChoice == T:
                    player.getStats()
                    print("Press Any Key to Continue...")
                    playerKey = getch()
                else:
                    print("Invalid")
            #player presses key move -> [UP/DOWN/LEFT/RIGHT ARROWS] OR Q [Quit] OR S [Save] OR I [Inventory]
                #player moves
                    #MOVE()
                    #player moves to an occupied tile
                        #encounter = True
                        #check if the tile contains the final boss
                            #if the tile does contain the boss check the players number of enemy defeats
                                #if the player has defeated enough enemies ask the player if they want to fight the boss
                                    #if yes initiate a battle with the final boss - combat.py
                                        #if you lose game over   -playerLoses()
                                        #elif you win game won   -playerWins()
                            #else if player doesnt have enough encounters or dont want to fight, move the player away
                                #move the player one tile based on RNG and position (Up,down,left,right)
                                #loop random moves until a valid move is found. 
                                #while not valid move
                                    #moveAway()
                                    
                        #if the tile doesnt contain the boss, check for an enemy or anomaly
                            #if there is an enemy, fight it
                                #if the player wins, display {encouragment} {celebration} and replace their current tile with a PlayerTile
                                #elif the player loses, end the game {possibly lose a life}?
                                #elif the player runs, move them 1 tile randomly
                                    #update the enemyTile with the enemies state after battle
                                    
                            #else if there is an anomaly, player encounters the anomaly
                                #set anomaly tile to player occupied
                    #player moves to unoccupied tile
                #redraw board
                
            
                #use item
                    #asks the player to choose an item from their inventory or cancel
                    #if the player wants to use an item that is single use, warn them it will be wasted
                        #if they still want to use it, use the item
                        #else loop back to top
            
                #save
                    #use a save function to save the board.
                    #the board contains all objects and tiles and everything in play, so we should just need to save that one object.

            
                #quit
                    #warns the player to save first [Q] to quit, [S] to save
                        #if they choose to save, run the save function
                 #else terminate the program.
        if playerWon == True:
            system("cls")
            print("You have emerged victorious from a dangerous galaxy")
            time.sleep(2)
            print("By defeating the galactic boss you have earned the praises of all who know you, rest well hero")
            time.sleep(2)
            print("Your Final Stats")
            print("-------------")
            player.getStats()
            time.sleep(10)
        elif playerLost == True:
            print("You have fallen to the evils of the galaxy")
            print("Fare thee well in the next life")
            time.sleep(10)
        else:
            pass
    except Exception as e:
        logging.basicConfig(filename='app.log',level=logging.INFO)
        logging.exception(e)
main()

