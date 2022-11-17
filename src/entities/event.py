class Event():
    counter = 0
    def __init__(self, name, description, team=False, places=5):
        self.id = counter
        self.__name = name
        self.team = team
        self.__points = [0 for _ in range(places)]
        self.description = description

        counter+=1

    def setpoints(self, points):
        self.__points = points