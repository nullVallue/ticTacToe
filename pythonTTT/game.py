from board import Board
from player import Player
class Game:
    def __init__(self):
        self.boardState = Board() 

    # checks if position to be updated is legally allowed to be played updates and returns True if legal, returns False if illegal
    def updateBoard(self, position:int, player:Player) -> bool:
        updatePosition = self.boardState.getSpot(position)
        if updatePosition.isEmpty():
            if player.isCrossPlayer():
                updatePosition.setCross(True)
                updatePosition.setEmpty(False)
            else:
                updatePosition.setEmpty(False)

            return True
        else:
            return False

    # update board without checking if it is a legal move or not
    def updateBoardIgnore(self, position:int, player:Player):
        updatePosition = self.boardState.getSpot(position)
        if player.isCrossPlayer():
            updatePosition.setCross(True)
            updatePosition.setEmpty(False)
        else:
            updatePosition.setEmpty(False)
            updatePosition.setCross(False)

    #checks if the three given spots have the same symbol
    def checkThreeSpots(self, s1:int, s2:int, s3:int, cross) -> bool:
        if cross:
            check = self.boardState.getSpot(s1).isCross() and self.boardState.getSpot(s2).isCross() and self.boardState.getSpot(s3).isCross()
        else:
            check = not self.boardState.getSpot(s1).isCross() and not self.boardState.getSpot(s2).isCross() and not self.boardState.getSpot(s3).isCross()

        if not (self.boardState.getSpot(s1).isEmpty() and self.boardState.getSpot(s2).isEmpty() and self.boardState.getSpot(s3).isEmpty()):
            if check:
                return True
            else:
                return False
        else:
            return False
    
    def checkWin(self, cross) -> bool:
        # x x x
        # - - - scenario 1
        # - - -
        if self.checkThreeSpots(0, 1, 2, cross):
            return True

        # - - -
        # x x x scenario 2
        # - - -
        elif self.checkThreeSpots(3, 4, 5, cross):
            return True

        # - - -
        # - - - scenario 3
        # x x x
        elif self.checkThreeSpots(6, 7, 8, cross):
            return True

        # x - -
        # x - - scenario 4
        # x - -
        elif self.checkThreeSpots(0, 3, 6, cross):
            return True

        # - x -
        # - x - scenario 5
        # - x -
        elif self.checkThreeSpots(1, 4, 7, cross):
            return True

        # - - x
        # - - x scenario 6
        # - - x
        elif self.checkThreeSpots(2, 5, 8, cross):
            return True

        # x - -
        # - x - scenario 7
        # - - x
        elif self.checkThreeSpots(0, 4, 8, cross):
            return True

        # - - x
        # - x - scenario 8
        # x - -
        elif self.checkThreeSpots(2, 4, 6, cross):
            return True

        else:
            return False

    # returns true if board is full
    def isFull(self) -> bool:
        full = False
        for i in range(0,9):
            if not self.boardState.getSpot(i).isEmpty():
                full = True
                break
            else:
                full = False
        return full
