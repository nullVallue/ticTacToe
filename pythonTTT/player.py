class Player:
    def __init__(self, name:str, cross:bool):
        self.name = name
        self.score = 0
        self.cross = cross
        if cross:
            self.mark = 'X'
        else:
            self.mark = 'O'

    def getName(self) -> str:
        return self.name

    def getScore(self) -> int:
        return self.score

    def addScore(self):
        self.score += 1

    def resetScore(self):
        self.score = 0

    def getMark(self) -> str:
        return self.mark

    def isCrossPlayer(self) -> bool:
        return self.cross
