from .member import Member

class Team(Member):
    counter = 0
    def __init__(self):
        if counter>=4:   
            raise Exception
        self.id = counter
        self.name = "no Name (Team)"
        self.__members = []
        counter+=1

    def add_member(self,member: Member):
        self.__members.append(member)

    def get_members(self):
        return self.__members
    
    def delete_member(self, member: Member):
        self.__members.remove(member)
        