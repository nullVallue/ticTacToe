class Spot:
    def __init__(self, x:int, y:int):
        self.coordinate = [x, y]
        self.empty = True
        self.cross = False 

    def isEmpty(self) -> bool:
        return self.empty

    def isCross(self) -> bool:
        return self.empty

    def setCross(self) -> bool:
        if self.isEmpty():
            self.cross = True
            return True
        else:
            return False
