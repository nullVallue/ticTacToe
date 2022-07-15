# ticTacToe
Creating ticTacToe game with different programming languages

## Languages Used 
- Python


---
# **Python**
## Classes: 

### main file

### Player
> -name:str
> -score:int
> -cross:bool
> -mark:str
> 
> +getName():str
> +getScore():int
> +addScore():void
> +resetScore():void
> +getMark():str
> +isCrossPlayer():bool

### Board
> -spot:spot[]
>
> +getSpot():spot[]
> +printBoard()

### Spot
> -coordinate:int[]
> -empty:bool
> -cross:bool
>
> +isEmpty():bool
> +isCross():bool
> +setCross(iscross:bool):void
> +setEmpty(isempty:bool):void
> +printSpot():void

### Game 
> -boardState:board
> -players:Player[]
> -winner:str
> 
> +getPlayer(index:int):Player
> +updateBoard():bool
> +updateBoardIgnore():void
> +checkThreeSpots(s1:int, s2:int, s3:int, cross):bool
> +checkWin(cross):bool
> +isFull():bool
> +setWinner(index):void
