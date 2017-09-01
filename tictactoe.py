human = " X "
#human = MAX
bot = " O "
#bot = MIN
empty = " . "

class Board:
	def __init__(self):
		self.grid = [[empty,empty,empty],[empty,empty,empty],[empty,empty,empty]]

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
				if grid[col][row] == empty:
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
			grid[move["index"][0]][move["index"][1]] = empty
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
		firstLine = self.formatLine(self.grid[2])
		secondLine = self.formatLine(self.grid[1])
		thirdLine = self.formatLine(self.grid[0])
		hRule = self.getHorizRule(firstLine)

		#ridStr = "-----" + "\n" + str(self.grid[2]) + "\n" + str(self.grid[1]) + "\n" + str(self.grid[0]) + "\n" + "-----"
		gridStr = "\n" + firstLine + hRule + secondLine + hRule + thirdLine
		return gridStr

	def formatLine(self,line):
		return "\t" + str(line[0]) + "|" + str(line[1]) + "|" + str(line[2]) + "\n"

	def getHorizRule(self,line):
		rule = ""
		for i in range(len(line)-2):
			rule += "-"
		return "\t" + rule + "\n";


board = Board()

currPlayer = human

gameOver = False
while gameOver == False:
	if board.checkGrid(human, board.grid) or len(board.getSpots(board.grid)) == 0 or board.checkGrid(bot, board.grid):
		gameOver = True
		break
	if currPlayer == human:
		print(board)
		moveRow = input("x: ")
		moveCol = input("y: ")
		board.grid[int(moveCol)][int(moveRow)] = currPlayer
		currPlayer = bot
	else:
		move = board.getMove(currPlayer)
		board.grid[move[0]][move[1]] = currPlayer
		currPlayer = human
print("\n\tGame Over!!!")
print(board)