# ticTacToe
Creating ticTacToe game with different programming languages

## Languages Used 
- Python
- Java


---
# **Python**
## Classes: 

### main file
```
+main()
+promptSelectSpot(player:Player):int
+play()
```

### Player
```
-name:str
-score:int
-cross:bool
-mark:str

init(name:str, cross:bool)

+getName():str
+getScore():int
+addScore():void
+resetScore():void
+getMark():str
+isCrossPlayer():bool
```

### Board
```
-spot:spot[]

init()

+getSpot():spot[]
+printBoard()
```

### Spot
```
-coordinate:int[]
-empty:bool
-cross:bool

init(x:int, y:int)

+isEmpty():bool
+isCross():bool
+setCross(iscross:bool):void
+setEmpty(isempty:bool):void
+printSpot():void
```

### Game 
```
-boardState:board
-players:Player[]
-winner:str
 
init(player1:Player, player2:Player) 
 
+getBoardState():Board 
+getPlayer(index:int):Player
+updateBoard(position:int, player:Player):bool
+updateBoardIgnore():void
+checkThreeSpots(s1:int, s2:int, s3:int, cross):bool
+checkWin(cross):bool
+isFull():bool
+setWinner(index):void
+getWinner():str
+setDraw():void
```

---
# **Java**
## Classes: 

### main file

### Player
```
-name:str
-score:int
-cross:bool
-mark:str

init(name:str, cross:bool)

+getName():str
+getScore():int
+addScore():void
+resetScore():void
+getMark():str
+isCrossPlayer():bool
```

### Board
```
-spot:spot[]

init()

+getSpot():spot[]
+printBoard()
```

### Spot
```
-coordinate:int[]
-empty:bool
-cross:bool

init(x:int, y:int)

+isEmpty():bool
+isCross():bool
+setCross(iscross:bool):void
+setEmpty(isempty:bool):void
+printSpot():void
```

### Game 
```
-boardState:board
-players:Player[]
-winner:str
 
init(player1:Player, player2:Player) 
 
+getBoardState():Board 
+getPlayer(index:int):Player
+updateBoard(position:int, player:Player):bool
+updateBoardIgnore():void
+checkThreeSpots(s1:int, s2:int, s3:int, cross):bool
+checkWin(cross):bool
+isFull():bool
+setWinner(index):void
+getWinner():str
+setDraw():void
```
