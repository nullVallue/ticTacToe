from player import Player
from board import Board
from spot import Spot
from game import Game

def main():
    loopMenu = True

    while loopMenu:
        print("=========")
        print("TicTacToe")
        print("=========")
        print("1) Play")
        print("0) Exit\n")

        invalidOption = True 
        menuOption = -1
        while invalidOption:
            try:
                menuOption = int(input(" >> ")) 
                invalidOption = False 
            except:
                invalidOption = True
            if not invalidOption:
                if menuOption < 0 and menuOption > 1:
                    invalidOption = True
                else:
                    invalidOption = False

            if invalidOption:
                print("\nPlease enter a valid option\n")

        if menuOption == 1:
            play()
            loopMenu = True
        else:
            print("\nExiting Program\n")
            loopMenu = False

def promptSelectSpot(player:Player) -> int:
    playerName = player.getName()

    invalidSpot = True
    selectedSpot = -1

    while invalidSpot:
        try:
            selectedSpot = int(input(playerName + " >> "))
            invalidSpot = False
        except:
            invalidSpot = True

        if not invalidSpot:
            if selectedSpot < 1 or selectedSpot > 9:
                invalidSpot = True
            else:
                invalidSpot = False

    return (selectedSpot - 1)


def play():
    print("\n=======")
    print("New Game")
    print("=======\n")

    print("Enter Player Name: ")
    player1Name = str(input("Player 1 : "))
    player2Name = str(input("Player 2 : "))

    player1 = Player(player1Name, False)
    player2 = Player(player2Name, True)

    game = Game(player1, player2)

    end = False
    i = 2
    winnerIndex = -1
    while not end:
        game.getBoardState().printBoard()
        if (i%2) == 0:
            turn = game.getPlayer(0)
        else:
            turn = game.getPlayer(1)
        
        legal = False
        while not legal:
            selectedSpot = promptSelectSpot(turn)

            legal = game.updateBoard(selectedSpot, turn)

            if not legal:
                print("\nMove is not legal!\n")

        if game.checkWin(game.getPlayer(0).isCrossPlayer()):
            end = True
            winnerIndex = 0
        elif game.checkWin(game.getPlayer(1).isCrossPlayer()):
            end = True
            winnerIndex = 1
        elif game.isFull():
            winnerIndex = -1
            end = True

        if end:
            game.getBoardState().printBoard()
            if winnerIndex == 0:
                game.setWinner(0)
            elif winnerIndex == 1:
                game.setWinner(1)
            else:
                game.setDraw()

        i += 1

    print("\n===============")
    print("Game has ended!")
    print("===============\n")
    if winnerIndex > -1:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("WINNER : " + game.getWinner())
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    else:
        print("\n||||||||||||||||||||||||||")
        print(game.getWinner() + "")
        print("||||||||||||||||||||||||||\n")

    return

main()
