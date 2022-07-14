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
> -spot00:spot
> -spot01:spot
> -spot02:spot
> -spot10:spot
> -spot11:spot
> -spot12:spot
> -spot20:spot
> -spot21:spot
> -spot22:spot

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
