class Package:
    pacId = ""
    wgtInKg = 0
    def __init__(self, pId, w):
        self.pacId = pId
        self.wgtInKg = w

class Drone:
#    dId = "" 
 #   maxLoad = 0
  #  __status = ""

    def __init__(self, dId, maxLoad, status):
        self.dId = dId
        self.maxLoad = maxLoad
        status = status.lower()
        self.__status = status

    def getStatus(self):
        return self.__status

    def setStatus(self,newS):
        newS = newS.lower()
        if(newS == 'idle' or newS =='delivering' or newS == 'charging'):
            self.__status = newS
        else:
            print("Not a valid status")
    def assignPack(self,packObj):
        if(self.__status == 'idle' and packObj.wgtInKg<=self.maxLoad):
            self.currPack = packObj
            self.__status = 'delivering'
            self.timer  =  2
            print(f"Package sucessfully assigned to drone {self.dId}, package id: {packObj.pacId}")
            return True
        else:
            print(f"PAckage {packObj.pacId} cant be assigned because drone {self.dId} not available")
            return False
        
    def updateStatus(self):
        if self.__status == 'delivering':
            if self.timer>0:
                self.timer -=1
            if self.timer==0:
                self.__status = 'charging'
                self.timer = 2
                print(f"Drone {self.dId } delivery finishes and charging now!!")

        elif self.__status == 'charging' :
            if self.timer>0:
                self.timer -=1
            if self.timer ==0:
                self.__status = 'idle'
                print(f"Drone {self.dId} idle currently. ") 
class FleetManager:
    def __init__(self):
        self.drones = {
        }
        self.pendPack = []

    def addDrone(self, droneObj) :
        self.drones[droneObj.dId] = droneObj
    def addPack(self, packObj):
        self.pendPack.append(packObj)
    def dispatchJobs(self):
        unassigned = []
        
        for pkg in self.pendPack:
            assigned = False
            for drone in self.drones.values():
                if drone.getStatus() == 'idle' and pkg.wgtInKg <= drone.maxLoad:
                    if drone.assignPack(pkg):
                        assigned  = True
                        break
                if not assigned:
                    unassigned.append(pkg)
            self.pendPack = unassigned
            for drone in self.drones.values():
                drone.updateStatus()
    def simulationTick(self):

        for drone in self.drones.values():
            drone.updateStatus()
        self.dispatchJobs()

fm = FleetManager()
fm.addDrone(Drone("Drone 001",10,'idle'))
fm.addDrone(Drone("Drone 002",4,'idle'))
fm.addDrone(Drone("Drone 003",5,'idle'))
fm.addPack(Package("Arms Supplies", 3))
fm.addPack(Package("Grenades",5))
fm.addPack(Package("Missiles",10))
fm.dispatchJobs()

for t in range (1,6):
    print("Tick: ") 
    fm.simulationTick()