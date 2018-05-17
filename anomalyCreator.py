#anomalyCreator
from gameObjects import Anomaly
from items import Perm
import pickle

def generateAnomalyFile():
    anomalyList = []
    itemList = []

    #blackHoleItem
    blackHole = Perm("Black Hole",-1000000000000000000,"HP")
    flavorText = "Your Ship has flown too close to a blackHole, your destruction is emminent and your crew has gone insane. Fare thee well traveler"
    blackHoleAnomaly = Anomaly(blackHole,flavorText,art = "")

    #wormhole
    wormHoleEffect = Perm("Worm Hole",-10,"SHD")
    flavorText = "You have drifted past an unstable wormhole. A space-time distortion field at the mouth of the wormhole has weakened your shield generators, reducing your shields by 10 points. "
    wormHoleAnomaly = Anomaly(wormHoleEffect, flavorText, art= "")

    #subspace current
    subspaceEffect = Perm("Subspace",-2,"SPD")
    flavorText = "Your ship was hit head on by a Subspace Current, you escape but your engines were overloaded, reducing your speed by 2 points. "
    subspaceCurrentAnomaly = Anomaly(subspaceEffect,flavorText, art = "")

    #asteroid belt
    asteroidEffect = Perm("Asteroid",-5,"ARM")
    flavorText = "Your ship has ventured too close to a massive asteroid belt. Stray rocks from the belt hammer your ship, reducing your armor by 5 points."
    asteroidAnomaly = Anomaly(asteroidEffect, flavorText, art = "")

    anomalyList = [wormHoleAnomaly,subspaceCurrentAnomaly,asteroidAnomaly]
    anomalyFile = open("anomaly.anome","wb")

    pickle.dump(anomalyList,anomalyFile)
    pickle.dump(blackHoleAnomaly,anomalyFile)
    anomalyFile.close()


    picklein = open("anomaly.anome","rb")
    try:
        anomalies = pickle.load(picklein)
    except EOFError:
        print("Anomaly File Empty")
        time.sleep(10)
    #print(anomalies[0])
    picklein.close()

generateAnomalyFile()
