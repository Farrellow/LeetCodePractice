# -*- coding: utf-8 -*-

class UndergroundSystem:

    def __init__(self):
        self._check_in_dict = dict()
        self._notes_dict = dict()


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._check_in_dict[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station_name, start_t = self._check_in_dict[id]
        if start_station_name not in self._notes_dict:
            self._notes_dict[start_station_name] = dict()
        if stationName not in self._notes_dict[start_station_name]:
            self._notes_dict[start_station_name][stationName] = list()
        self._notes_dict[start_station_name][stationName].append(t - start_t)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        notes_list = self._notes_dict[startStation][endStation]
        return sum(notes_list) / len(notes_list)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

