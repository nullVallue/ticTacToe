class Player:
    def __init__(self, name:str, mark:str):
       self.name = name
       self.score = 0
       self.mark = mark

    def getName(self) -> str:
        return self.name

    def getScore(self) -> int:
        return self.score

    def addScore(self):
        self.score += 1

    def resetScore(self):
        self.score = 0
