# ticTacToe
Creating ticTacToe game with different programming languages

## Languages Used 
- Python


---
# **Python**
## Classes: 

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
> +isCross():bool

### Board
> -spot:spot[]
>
> +getSpot():spot[]

### Spot
> -coordinate:int[]
> -empty:bool
> -cross:bool
>
> +isEmpty():bool
> +isCross():bool
> +setCross():void
> +setEmpty(isempty:bool):void

### Game 
> -boardState:board
> 
> +isDraw():bool
