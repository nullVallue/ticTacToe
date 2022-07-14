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
