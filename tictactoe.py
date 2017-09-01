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
		spots = self.getSpots(self.grid)
		if player == human: 
			bestScore = [-10]
		else:
			bestScore = [10]
		bestMove = 0
		for i in range(len(spots)):
			self.grid[spots[i][0]][spots[i][1]] = player
			if player == human:
				score = self.minimax(bot,self.grid,1)
				if score[0] > bestScore[0]:
					bestScore = score
					bestMove = i
				elif score[0] == bestScore[0] and score[1] < bestScore[1]:
					bestScore = score
					bestMove = i
			else:
				score = self.minimax(human,self.grid,1)
				if score < bestScore:
					bestScore = score
					bestMove = i
				elif score[0] == bestScore[0] and score[1] < bestScore[1]:
					bestScore = score
					bestMove = i
			self.grid[spots[i][0]][spots[i][1]] = 0
		return spots[bestMove]

	def getSpots(self,grid):
		moves = []
		for col in range(3):
			for row in range(3):
				if grid[col][row] == 0:
					moves.append([col,row])
		return moves

	def minimax(self,player,grid,depth):
		if self.checkGrid(player,grid):
			if player == human:
				return [10, depth]
			else: 
				return [-10, depth]
		else:			
			avilableSpots = self.getSpots(grid)
			scores = []
			for spot in avilableSpots:
				#do move
				grid[spot[0]][spot[1]] = player
				if player == human:
					score = self.minimax(bot,grid,depth+1)
					scores.append(score)
				else:
					score = self.minimax(human,grid,depth+1)
					scores.append(score)
				#reset grid
				grid[spot[0]][spot[1]] = 0
			if player == human:
				bestScore = [-10, depth]
				for i in range(len(scores)):
					if scores[i][0] > bestScore[0]:
						bestScore = scores[i]
					elif scores[i][0] == bestScore[0] and scores[i][1] < bestScore[1]:
						bestScore = scores[i]
				return bestScore
			else:
				bestScore = [10, depth]
				for i in range(len(scores)):
					if scores[i][0] < bestScore[0]:
						bestScore = scores[i]
					elif scores[i][0] == bestScore[0] and scores[i][1] < bestScore[1]:
						bestScore = scores[i]
				return bestScore
		return [0, depth]

	def __str__(self):
		gridStr = "-----" + "\n" + str(self.grid[2]) + "\n" + str(self.grid[1]) + "\n" + str(self.grid[0]) + "\n" + "-----"
		return gridStr


board = Board()

currPlayer = human

gameOver = False
while gameOver == False:
	if currPlayer == human:
		print(board)
		moveCol = input("column: ")
		moveRow = input("row: ")
		board.grid[int(moveCol)][int(moveRow)] = currPlayer
		currPlayer = bot
	else:
		move = board.getMove(human)
		board.grid[move[0]][move[1]] = currPlayer
		currPlayer = human
	#if board.checkGrid(bot, board.grid) or board.checkGrid(human, board.grid):
		#gameOver = True




