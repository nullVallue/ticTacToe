class Spot:
    def __init__(self, x:int, y:int):
        self.coordinate = [x, y]
        self.empty = True
        self.cross = False 

    def isEmpty(self) -> bool:
        return self.empty

    def isCross(self) -> bool:
        return self.empty

    def setCross(self, iscross:bool):
        self.cross = iscross 

    def setEmpty(self, isempty:bool):
        self.empty = isempty

    def printSpot(self):
        if self.empty:
            print(" ", end="")
            return
        elif self.cross:
            print("x", end="")
            return
        else:
            print("o", end="")
            return
