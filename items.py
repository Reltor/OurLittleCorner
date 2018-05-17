#create item objects that will benefit the player so they are ready for the final boss
#give the items methods that would allow them to modify the players stats
    #pass the player as a parameter to the item method
    #have the method check what stat the item changes
    #modify the stat
    #return the player object to the game
#to use an item, the user inputs what catagory they want to select from
#the program prints the names of all the available item from the selected catagory
#the item is then applied

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##Items for final project:
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
##plasma shield: permanent 2 point boost to shields
##deflector shield: permanent 3 point boost to shileds
##kojima field: permanent 5 point boost to shields
##spiral shield: permanent 10 point boost to shields
##
##reinforced armor: permanent 2 point boost to armor
##titanium plating: permanent 3 point boost to armor
##adamantium lining: permanent 5 point boost to armor
##star metal coating: permanent 10 point boost to armor
##
##enhanced FTL drive: permanent 2 point boost to speed
##K-F drive: permanent 3 point boost to speed
##warp drive: permanent 5 point boost to speed
##quantum drive: permanent 10 point boost to speed
##
##enhanced lasers: permanent 2 point boost to energy
##PPC: permanent 3 point boost to energy
##turbo cannon: permanent 5 point boost to energy
##partical lance: permanent 10 point boost to energy
##
##high velocity rounds: permanent 2 point boost to physical
##rail guns: permanent 3 point boost to physical
##anti matter rounds: permament 5 point boost to physical
##FTL rounds: permanent 10 point boost to physical
##
##reinforced hull: permanent 2 point boost to HP
##endo-steel: permanent 3 point boost to HP
##impact absorbers: permanent 5 point boost to HP
##the power of friendship: permanent 10 point boost to HP

#--------------------
#Item drops
#--------------------

#each time an enemy is defeated, they will drop a random item from the items list
#the rarity of the item dropped will depend on the dificaulty of the enemy that dropped it
#using the item "map" the enemy dificaulty picks the row (rarity) of the item dropped, and a random number generator picks the column (type) of item dropped
#the item selected for the drop is then passed to the player's inventory




#The following is needed in the main program in order to generate and use items.


#these 2 lines should go before any items are referenced
import random
import pickle
'''
import items
itemList = items.createItems()


def useItem(player):
    print("0)HP  1)PHY  2)ARM  3)SPD  4)ENG  5)SHD")
    catagory = int(input("please select the number of the buff catagory you want: "))
    i = 0
    for x in itemList[catagory]:
        print(i,")",x.name)
        i += 1
    number = int(input("please select the number of the item you want to use: "))
    itemList[catagory][number].boostStat(player)
    player.showStats()
    return player
'''


class Perm(object):
    def __init__(self,name,boost,stat):
        self.name = name
        self.boost = boost
        self.stat = stat
    def boostStat(self,Player):
        if self.stat == "HP":
            if Player.HP + self.boost >= 0:
                Player.HP += self.boost
            else:
                Player.HP = 0
            return Player
        elif self.stat == "PHY":
            if Player.PHY + self.boost >= 0:
                Player.PHY += self.boost
            else:
                Player.PHY = 0
            return Player
        elif self.stat == "ARM":
            if Player.ARM + self.boost >= 0:
                Player.ARM += self.boost
            else:
                Player.ARM = 0
            return Player
        elif self.stat == "SPD":
            if Player.SPD + self.boost >= 0:
                Player.SPD += self.boost
            else:
                Player.SPD = 0
            return Player
        elif self.stat == "ENG":
            if Player.ENG + self.boost >= 0:
                Player.ENG += self.boost
            else:
                Player.ENG = 0
            return Player
        elif self.stat == "SHD":
            if Player.SHD + self.boost >= 0:
                Player.SHD += self.boost
            else:
                Player.SHD = 0
            return Player
        
'''
class Temp(Perm):
    def __init__(self,name,boost,stat,time):
        super().__init__(name,boost,stat)
        self.time = time
'''


def createItems():
    iList = []
    commonList = []
    unCommonList = []
    rareList = []
    superRareList = []
    hpList = []
    phyList = []
    armList = []
    spdList = []
    engList = []
    shdList = []
    #creats HP items list
    reinforced = Perm("Reinforced Hull",2,"HP")
    hpList.append(reinforced)
    endo = Perm("Endo-Steel",3,"HP")
    hpList.append(endo)
    impact = Perm("Impact Absorbers",5,"HP")
    hpList.append(impact)
    friendship = Perm("The Power of Friendship",10,"HP")
    hpList.append(friendship)
    #creats PHY items list
    hvr = Perm("High Velocity Rounds",2,"PHY")
    phyList.append(hvr)
    rail = Perm("Rail Guns",3,"PHY")
    phyList.append(rail)
    amr = Perm("Anti Matter Rounds",5,"PHY")
    phyList.append(amr)
    ftlr = Perm("FTL Rounds",10,"PHY")
    phyList.append(ftlr)
    #creats ARM items list
    reArmor = Perm("Reinforced Armor",2,"ARM")
    armList.append(reArmor)
    titanium = Perm("Titanium Plating",3,"ARM")
    armList.append(titanium)
    adamantium = Perm("Adamantium Lining",5,"ARM")
    armList.append(adamantium)
    star = Perm("Star Metal Coating",10,"ARM")
    armList.append(star)
    #create SPD items list
    ftld = Perm("Enhanced FTL Drive",2,"SPD")
    spdList.append(ftld)
    kf = Perm("K-F Drive",3,"SPD")
    spdList.append(kf)
    warp = Perm("Warp Drive",5,"SPD")
    spdList.append(warp)
    quantum = Perm("Quantum Drive",10,"SPD")
    spdList.append(quantum)
    #create ENG items list
    eLasers = Perm("Enhanced Lasers",2,"ENG")
    engList.append(eLasers)
    PPC = Perm("PPC",3,"ENG")
    engList.append(PPC)
    turbo = Perm("Turbo Cannon",5,"ENG")
    engList.append(turbo)
    partical = Perm("Particle Lance",10,"ENG")
    engList.append(partical)
    #creats SHD items list
    plasma = Perm("Plasma Shield",2,"SHD")
    shdList.append(plasma)
    deflect = Perm("Deflector Shield",3,"SHD")
    shdList.append(deflect)
    kojima = Perm("Kojima Field",5,"SHD")
    shdList.append(kojima)
    spiral = Perm("Spiral Shield",10,"SHD")
    shdList.append(spiral)
    #append all lists into an overall item list
    iList.append(hpList)
    iList.append(phyList)
    iList.append(armList)
    iList.append(spdList)
    iList.append(engList)
    iList.append(shdList)
    return iList

#--------------------
#Random item drops
#--------------------


#each time an enemy is defeated, they will drop a random item from the items list
#the rarity of the item dropped will depend on the dificaulty of the enemy that dropped it
#using the item "map" the enemy dificaulty picks the row (rarity) of the item dropped, and a random number generator picks the column (type) of item dropped
#the item selected for the drop is then passed to the player's inventory
def inventory(player):
    inInventory = True
    while inInventory:
        i = 0
        inventory = []
        pickle_in = open("inventory.inv","rb")
        try:
            inventory = pickle.load(pickle_in)
        except EOFError:
            inventory = []
        pickle_in.close()
        print("------------------")
        print("Select and item to use:")
        print("------------------")
        print("Or press B to exit")
        print("------------------")
        for x in inventory:
            print(i,") ",end="")
            itemString = x.name + ": " + "Boosts your " + x.stat + " stat by " + str(x.boost)
            print(itemString)
            i += 1
        choice = input("-->")
        valid = False
        while not valid:
            try:
                choice = int(choice)
                if choice not in range(len(inventory)):
                    choice = input("-->")
                else:
                    valid = True
            except ValueError:
                if choice != "b" and choice != "B":
                    choice = input("-->")
                else:
                    valid = True
        if choice == "b" or choice == "B":
            return player,"Player"
            inInventory = False
        else:
            choice = int(choice)
            player = inventory[choice].boostStat(player)
            del inventory[choice]
            player.getStats()
            pickle_out = open("inventory.inv","wb")
            pickle.dump(inventory,pickle_out)
            pickle_out.close
            return player,"Enemy"
            inInventory = False

def addItem(drop):
    inventory = []
    pickle_in = open("inventory.inv","rb")
    try:
        inventory = pickle.load(pickle_in)
    except EOFError:
        inventory = []
    pickle_in.close()
    inventory.append(drop)
    pickle_out = open("inventory.inv","wb")
    pickle.dump(inventory,pickle_out)
    pickle_out.close




def test():
    itemList = createItems()
    ranDrop = random.randint(0,5)
    pickedItem = itemList[ranDrop][0]
    print(pickedItem.name)
        
