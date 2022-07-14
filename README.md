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
> 
> +getName():str
> +getScore():int
> +addScore():void
> +resetScore():void

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
> +setCross():bool

### Game 
> -boardState:board
> 
> +isDraw():bool
