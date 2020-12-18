class FriendShips:
    def __init__(self):
        self.dict = {}

    def makeFriends(self, person1, person2):
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)
        return self.dict

    def getFriendsList(self, person):
        if person in self.dict.keys():
            return self.dict[person]
        else:
            raise Exception("This person not exist")

    def areFriends(self, person1, person2):
        if person2 in self.dict.keys() and person1 in self.dict[person2]:
            return person1 + " " + "is friend" + " " + person2
        else:
            return person1 + " " + "is not friend" + " " + person2

    def addFriend(self, person, friend):
        if type(person) == str and type(friend) == str:
            if person in self.dict.keys():
                self.dict[person].append(friend)
            else:
                self.dict[person] = [friend]
        else:
            raise TypeError("People have to be type string")
