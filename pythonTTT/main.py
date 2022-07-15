from player import Player
from board import Board
from spot import Spot
from game import Game

def main():
    print("=========")
    print("TicTacToe")
    print("=========")
    print("0) Exit")
    print("1) Play\n")

    invalidOption = False
    menuOption = -1
    while invalidOption:
        try:
            menuOption = int(input(" >> ")) 
            invalidOption = False 
        except:
            invalidOption = True

        if menuOption < 0 and menuOption > 1:
            invalidOption = True
        else:
            invalidOption = False

        if invalidOption:
            print("\nPlease enter a valid option\n")
