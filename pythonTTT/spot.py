class Spot:
    def __init__(self, x:int, y:int):
        self.coordinate = [x, y]
        self.empty = True
        self.cross = False 

    def isEmpty(self) -> bool:
        return self.empty

    def isCross(self) -> bool:
        return self.empty

    def setCross(self):
        self.cross = True

    def setEmpty(self, isempty:bool):
        self.empty = isempty
