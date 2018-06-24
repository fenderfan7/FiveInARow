from random import randint

def initialise_board(rows, columns):
	return [[0 for i in range(columns)] for i in range(rows)]
	
def print_board(board):
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


def human_turn(player_nr, board):
	while 1:
		print('It\'s Player' + str(player_nr) + '\'s turn! Setting mark at: row column')
		inputString = input()
		pos = [int(s) for s in inputString.split() if s.isdigit()]
		if len(pos) == 2:
			if pos[0] < len(board) and pos[1] < len(board[0]) and board[pos[0]][pos[1]] == 0:
				break
		print('ERROR: Try Again!')
	board[pos[0]][pos[1]] = player_nr
	return pos, board
	
def random_turn(player_nr, board):
	while 1:
		pos = [randint(0, len(board)-1), randint(0, len(board[0]))-1]
		if board[pos[0]][pos[1]] == 0:
			break
	board[pos[0]][pos[1]] = player_nr
	return pos, board


def check_has_won(board, player_nr, last_move_row, last_move_col):
	won = False
	counter = 0
	min_row = last_move_row-4 if last_move_row-4 >= 0 else 0
	max_row = last_move_row+4 if last_move_row+4 < len(board) else len(board)-1
	min_col = last_move_col-4 if last_move_col-4 >= 0 else 0
	max_col = last_move_col+4 if last_move_col+4 < len(board[0]) else len(board[0])-1
	
	min_row_offset = min_row-last_move_row
	min_col_offset = min_col-last_move_col
	min_offset = min_row_offset if min_row_offset >= min_col_offset else min_col_offset
	max_rowOffset = max_row-last_move_row
	max_colOffset = max_col-last_move_col
	max_offset = max_rowOffset if max_rowOffset <=  max_colOffset else max_colOffset
	
	min_offsetUp = -max_rowOffset if -max_rowOffset >= min_col_offset else min_col_offset #negative Result
	max_offsetUp = -min_row_offset if -min_row_offset <= max_colOffset else max_colOffset #positive Result
	
	#Check horizontally
	for row in range(min_row, max_row+1):
		if(board[row][last_move_col] == player_nr):
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	#Check vertically
	counter = 0
	for col in range(min_col, max_col+1):
		if(board[last_move_row][col] == player_nr):
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	#Check diagonally up
	counter = 0
	for offset in range(min_offsetUp, max_offsetUp+1):
		if(board[last_move_row - offset][last_move_col + offset] == player_nr):
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	#Check diagonally down
	counter = 0
	for offset in range(min_offset, max_offset+1):
		if(board[last_move_row + offset][last_move_col + offset] == player_nr):
			#print('curOffset' + str(offset))
			counter+=1
			if counter >= 5:
				return True
		else:
			counter = 0
	return False

def check_board_full(board):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == 0:
				return False
	return True
	
	



# board = initialise_board(20,20)
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

