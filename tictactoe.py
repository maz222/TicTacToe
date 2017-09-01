human = "X"
#human = MAX
bot = "O"
#bot = MIN

class Board:
	def __init__(self):
		self.grid = [[0,0,0],[0,0,0],[0,0,0]]

	def checkHorizontal(self, player, col, grid):
		if grid[col][0] != player:
			return False
		return grid[col][0] == grid[col][1] and grid[col][1] == grid[col][2]

	def checkVertical(self, player, row, grid):
		if grid[0][row] != player:
			return False
		return grid[0][row] == grid[1][row] and grid[1][row] == grid[2][row]

	def checkDiagonal(self, player, grid):
		if grid[1][1] != player:
			return False
		return ((grid[1][1] == grid[0][0] and grid[1][1] == grid[2][2]) or 
					(grid[1][1] == grid[2][0] and grid[1][1] == grid[0][2]))

	def checkGrid(self, player, grid):
		return (self.checkHorizontal(player,0,grid) or self.checkHorizontal(player,1,grid) or self.checkHorizontal(player,2,grid) or
					self.checkVertical(player,0,grid) or self.checkVertical(player,1,grid) or self.checkVertical(player,2,grid) or
						self.checkDiagonal(player,grid))

	def getMove(self,player):
		return self.minimax(player, self.grid)["index"]

	def getSpots(self,grid):
		moves = []
		for col in range(3):
			for row in range(3):
				if grid[col][row] == 0:
					moves.append([col,row])
		return moves

	def minimax(self,player,grid):
		spots = self.getSpots(grid)
		if self.checkGrid(human,grid):
			return {"score":-10}
		elif self.checkGrid(bot,grid):
			return {"score":10}
		if len(spots) == 0:
			return {"score":0}

		moves = []
		for i in range(len(spots)):
			#log spot
			move = {"index":spots[i]}
			#do move
			grid[move["index"][0]][move["index"][1]] = player
			if player == bot:
				result = self.minimax(human,grid)["score"]
				move["score"] = result
			else:
				result = self.minimax(bot,grid)["score"]
				move["score"] = result
			#reset
			grid[move["index"][0]][move["index"][1]] = 0
			moves.append(move)

		bestMove = None
		if player == bot:
			bestScore = -1000
			for i in range(len(moves)):
				if moves[i]["score"] > bestScore:
					bestScore = moves[i]["score"]
					bestMove = i
		else:
			bestScore = 1000
			for i in range(len(moves)):
				if moves[i]["score"] < bestScore:
					bestScore = moves[i]["score"]
					bestMove = i

		return moves[bestMove]


	def __str__(self):
		gridStr = "-----" + "\n" + str(self.grid[2]) + "\n" + str(self.grid[1]) + "\n" + str(self.grid[0]) + "\n" + "-----"
		return gridStr


board = Board()

currPlayer = human

gameOver = False
while gameOver == False:
	if board.checkGrid(human, board.grid) or len(board.getSpots(board.grid)) == 0 or board.checkGrid(bot, board.grid):
		gameOver = True
	if currPlayer == human:
		print(board)
		moveCol = input("column: ")
		moveRow = input("row: ")
		board.grid[int(moveCol)][int(moveRow)] = currPlayer
		currPlayer = bot
	else:
		move = board.getMove(currPlayer)
		board.grid[move[0]][move[1]] = currPlayer
		currPlayer = human
print("Game Over!!!")
print(board)