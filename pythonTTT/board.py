from spot import Spot
class Board:
    def __init__(self):
        self.spot = [
                        Spot(0,0),
                        Spot(0,1),
                        Spot(0,2),
                        Spot(1,0),
                        Spot(1,1),
                        Spot(1,2),
                        Spot(2,0),
                        Spot(2,1),
                        Spot(2,2)
                    ]

    def getSpot(self, position):
        return self.spot[position]

    def printBoard(self):
        print("\n")
        print("-------")
        print("|", end="")
        self.spot[0].printSpot()
        print("|", end="")
        self.spot[1].printSpot()
        print("|", end="")
        self.spot[2].printSpot()
        print("|")
        print("|", end="")
        self.spot[3].printSpot()
        print("|", end="")
        self.spot[4].printSpot()
        print("|", end="")
        self.spot[5].printSpot()
        print("|")
        print("|", end="")
        self.spot[6].printSpot()
        print("|", end="")
        self.spot[7].printSpot()
        print("|", end="")
        self.spot[8].printSpot()
        print("|")
        print("-------")
        print("\n")
