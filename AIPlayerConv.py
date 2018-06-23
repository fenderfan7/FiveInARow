import FiveInARowFunctions as f
import tensorflow as tf
import tflearn
import numpy as np
import math

learning_rate = 0.01
training_iterations = 50000
board_side_length = 20

def getData():
	data = []
	labels = []
	for iteration in range(training_iterations):
		playing = True
		player = 1
		board = f.initialiseBoard(board_side_length, board_side_length)
		while playing:
			pos, board = f.randomTurn(player, board)
			if f.checkHasWon(board, player, pos[0], pos[1]) == True:
				break
			player = (player % 2) + 1
			if f.checkBoardFull(board):
				playing = False
		data.append(board)
		if player == 1:
			labels.append(1) #win for player1
			
		else:
			labels.append(0) #no win for player1
		print('iteration: ' + str(iteration))		
	return [data, labels]
def get_model():
	tflearn.init_graph(num_cores = 4, gpu_memory_fraction = 0.5)
	net = tflearn.input_data(shape=[None, board_side_length*board_side_length, 1, 1])
	net = tflearn.conv_2d(net, 32, 8,activation = 'relu')
	net = tflearn.dropout(net, 0.8)
	net = tflearn.fully_connected(net, 1, activation='relu')
	net = tflearn.regression(net, optimizer='sgd', loss='mean_square')
	model = tflearn.DNN(net)
	return model
	
	
def train_model():
	print('Getting data...')
	input_data, labels = getData()	
	X = np.reshape(input_data, [training_iterations, board_side_length*board_side_length, 1, 1])
	Y = np.reshape(labels, [training_iterations,1])	
	model = get_model()
	model.fit(X, Y, n_epoch = 3)
	return model

def copy_board(board):
	board_copy = []
	for row in range(len(board)):
		for col in range(len(board[0])):
			board_copy.append(board[row][col])
	return board_copy

def ai_turn(playerNr, model, board):
	i=0
	predictions = []
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == 0:
				board_copy = copy_board(board)
				board_copy[i] = 1
				pred = model.predict(np.reshape(board_copy, [1, len(board_copy), 1, 1]))
				predictions.append(pred[0][0])
			else:
				predictions.append(0)
			i += 1
	print(str(predictions))
	flat_pos = predictions.index(max(predictions))
	pos = [math.floor(flat_pos/len(board)), flat_pos%(len(board))]
	board[pos[0]][pos[1]] = playerNr
	return pos, board


model = train_model()
model.save("modelConv.tfl")
print('model saved')
# model = get_model()
# model.load("modelConv.tfl")

num_played = 0
num_won = 0
for games in range(30):
	playing = True
	player = 1
	board = f.initialiseBoard(board_side_length, board_side_length)
	while playing:
		f.printBoard(board)
		if player == 1:
			pos, board = ai_turn(player, model, board)
		else:
			pos, board = f.randomTurn(player, board)
		if f.checkHasWon(board, player, pos[0], pos[1]) == True:
			break
		player = (player % 2) + 1
		if f.checkBoardFull(board):
			playing = False
		
	f.printBoard(board)
	if playing:
		print('*****Player' + str(player) + ' has won*****')
		if player ==1:
			num_won += 1
	else:
		print('*****It\'s a draw*****')
	num_played += 1
	print(str(pos))
print(str(num_won/num_played))
