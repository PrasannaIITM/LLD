class Player():
    def __init__(self, name, character):
        self.name = name
        self.character = character
    
    @staticmethod
    def builder():
        return PlayerBuilder()


class PlayerBuilder():
    
    def setName(self, name):
        self.__name = name
        return self

    def setCharacter(self, character):
        if character == "_":
            raise Exception(" '_' is not a valid character")
            
        self.__character = character
        return self

    def build(self):
        return Player(self.__name, self.__character)

