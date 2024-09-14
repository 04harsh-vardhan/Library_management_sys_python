class Solution:   
    def maxFuelAndDistance(self,fuelLeft,currIndex,stations,currDistance):
        total_distance = currDistance
        r_fuel = -1
        r_distance= 0
        r_index = 0
        for index,station in enumerate(stations):
            if index >currIndex:
                if (station[1] - total_distance) -fuelLeft <0:
                    break
                else:
                    fuelLeft = fuelLeft-(station[1] - total_distance)
                    total_distance = station[1]
                    if r_fuel < station[1]:
                        r_fuel = station[1]
                        r_distance = station[0]
                        r_index = index
                    
        
        return r_fuel,r_distance,r_index
                
    
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        currDistance = 0
        count = 0
        fuelLeft = startFuel
        currIndex = -1
        while(currDistance < target):
            r_fuel,r_distance,r_index = self.maxFuelAndDistance(fuelLeft,currIndex,stations,currDistance)
            if r_fuel == -1:
                return -1
            fuelLeft = r_fuel + fuelLeft-(r_distance - currDistance)
            currDistance = r_distance
            currIndex = r_index
            count+=1
        return count