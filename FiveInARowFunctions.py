from random import randint

def initialiseBoard(rows, columns):
	return [[0 for i in range(columns)] for i in range(rows)]
	
def printBoard(board):
	rows = len(board)
	cols = len(board[0])
	line = '   '
	for i in range(cols):
		# if i == 10:
			# line += ' '
		if i < 10:
			line += str(i) + '  '
		else:
			line += str(i) + ' '
	print(line)
	line = ''
	for row in range(rows):
		# if row == 10:
			# print('')
		if row < 10:
			line += str(row) + '  '
		else:
			line += str(row) + ' '
		for col in range(cols):
			# if col == 10:
				# line += ' '
			if board[row][col] == 0:
				line += '°  '
			elif board[row][col] == 1:
				line += 'X  '
			elif board[row][col] == 2:
				line += 'O  '
			else:
				line += 'ERROR'
		print(line)
		line = ''


def humanTurn(playerNr, board):
	while 1:
		print('It\'s Player' + str(playerNr) + '\'s turn! Setting mark at: row column')
		inputString = input()
		pos = [int(s) for s in inputString.split() if s.isdigit()]
		if len(pos) == 2:
			if pos[0] < len(board) and pos[1] < len(board[0]) and board[pos[0]][pos[1]] == 0:
				break
		print('ERROR: Try Again!')
	board[pos[0]][pos[1]] = playerNr
	return pos, board
	
def randomTurn(playerNr, board):
	while 1:
		pos = [randint(0, len(board)-1), randint(0, len(board[0]))-1]
		if board[pos[0]][pos[1]] == 0:
			break
	board[pos[0]][pos[1]] = playerNr
	return pos, board


def checkHasWon(board, playerNr, lastMoveRow, lastMoveCol):
	won = False
	counter = 0
	minRow = lastMoveRow-4 if lastMoveRow-4 >= 0 else 0
	maxRow = lastMoveRow+4 if lastMoveRow+4 < len(board) else len(board)-1
	minCol = lastMoveCol-4 if lastMoveCol-4 >= 0 else 0
	maxCol = lastMoveCol+4 if lastMoveCol+4 < len(board[0]) else len(board[0])-1
	
	minRowOffset = minRow-lastMoveRow
	minColOffset = minCol-lastMoveCol
	minOffset = minRowOffset if minRowOffset >= minColOffset else minColOffset
	maxRowOffset = maxRow-lastMoveRow
	maxColOffset = maxCol-lastMoveCol
	maxOffset = maxRowOffset if maxRowOffset <=  maxColOffset else maxColOffset
	
	minOffsetUp = -maxRowOffset if -maxRowOffset >= minColOffset else minColOffset #negative Result
	maxOffsetUp = -minRowOffset if -minRowOffset <= maxColOffset else maxColOffset #positive Result
	
	#Check horizontally
	for row in range(minRow, maxRow+1):
		if(board[row][lastMoveCol] == playerNr):
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	#Check vertically
	counter = 0
	for col in range(minCol, maxCol+1):
		if(board[lastMoveRow][col] == playerNr):
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	#Check diagonally up
	counter = 0
	for offset in range(minOffsetUp, maxOffsetUp+1):
		if(board[lastMoveRow - offset][lastMoveCol + offset] == playerNr):
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	#Check diagonally down
	counter = 0
	for offset in range(minOffset, maxOffset+1):
		if(board[lastMoveRow + offset][lastMoveCol + offset] == playerNr):
			#print('curOffset' + str(offset))
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	return False

def checkBoardFull(board):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == 0:
				return False
	return True
	
	



# board = initialiseBoard(20,20)
# board[2][4] = 2
# board[6][4] = 1
# board[7][3] = 1
# board[8][2] = 1
# board[9][1] = 0
# board[10][0] = 1
# board[2][4] = 2
# board[19][19] = 1
# board[18][18] = 1
# board[17][17] = 1
# board[16][16] = 1
# board[15][15] = 1

