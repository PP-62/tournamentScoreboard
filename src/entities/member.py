class Member():
    counter = 0
    def __init__(self):
        self.id = counter
        self.__name = "no Name"
        self.points = {}
        counter+=1

    def add_point(self, event, position):
        self.points[event.id] = event.points[position]

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name



    