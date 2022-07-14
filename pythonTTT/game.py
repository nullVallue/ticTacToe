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
    
    def checkWin(self, cross):
        winner = 0
        # x x x
        # - - - scenario 1
        # - - -
        if not (self.boardState.getSpot(0).isEmpty() and self.boardState.getSpot(1).isEmpty() and self.boardState.getSpot(2).isEmpty()):
            crossCheck = self.boardState.getSpot(0).isCross() and self.boardState.getSpot(1).isCross() and self.boardState.getSpot(2).isCross()
            circleCheck = not self.boardState.getSpot(0).isCross() and not self.boardState.getSpot(1).isCross() and not self.boardState.getSpot(2).isCross()
            if crossCheck:
                winner = 1 
            elif circleCheck:
                winner = 2
            else:
                winner = 0

        # - - -
        # x x x scenario 2
        # - - -
        elif not (self.boardState.getSpot(3).isEmpty() and self.boardState.getSpot(4).isEmpty() and self.boardState.getSpot(5).isEmpty()):
            crossCheck = self.boardState.getSpot(3).isCross() and self.boardState.getSpot(4).isCross() and self.boardState.getSpot(5).isCross()
            circleCheck = not self.boardState.getSpot(3).isCross() and not self.boardState.getSpot(4).isCross() and not self.boardState.getSpot(5).isCross()
            if crossCheck:
                winner = 1 
            elif circleCheck:
                winner = 2
            else:
                winner = 0

        # - - -
        # - - - scenario 3
        # x x x
        elif not (self.boardState.getSpot(6).isEmpty() and self.boardState.getSpot(7).isEmpty() and self.boardState.getSpot(8).isEmpty()):
            crossCheck = self.boardState.getSpot(6).isCross() and self.boardState.getSpot(7).isCross() and self.boardState.getSpot(8).isCross()
            circleCheck = not self.boardState.getSpot(6).isCross() and not self.boardState.getSpot(7).isCross() and not self.boardState.getSpot(8).isCross()
            if crossCheck:
                winner = 1 
            elif circleCheck:
                winner = 2
            else:
                winner = 0
