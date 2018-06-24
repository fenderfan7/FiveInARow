import FiveInARowFunctions as f
import tensorflow as tf
import tflearn
import numpy as np
import math

learning_rate = 0.01
training_iterations = 50000
#Change board dimensions here, Warning: New board dimension needs a new model!
board_side_length = 20

def get_data():
	data = []
	labels = []
	for iteration in range(training_iterations):
		playing = True
		player = 1
		board = f.initialise_board(board_side_length, board_side_length)
		while playing:
			pos, board = f.random_turn(player, board)
			if f.check_has_won(board, player, pos[0], pos[1]) == True:
				break
			player = (player % 2) + 1
			if f.check_board_full(board):
				playing = False
		data.append(board)
		if player == 1:
			labels.append([1,0]) #win for player1
			
		else:
			labels.append([0,1]) #no win for player1
		print('iteration: ' + str(iteration))
	return [data, labels]
def get_model():
	tflearn.init_graph(num_cores = 4)
	net = tflearn.input_data(shape=[None, board_side_length*board_side_length])
	#Hidden Layer, change dimensions/number of nodes here
	net = tflearn.fully_connected(net, 256,activation = 'relu')
	net = tflearn.dropout(net, 0.8)
	net = tflearn.fully_connected(net, 128,activation = 'relu')
	net = tflearn.dropout(net, 0.8)
	net = tflearn.fully_connected(net, 64,activation = 'relu')
	net = tflearn.dropout(net, 0.8)
	net = tflearn.fully_connected(net, 32,activation = 'relu')
	net = tflearn.dropout(net, 0.8)
	net = tflearn.fully_connected(net, 2, activation='softmax')
	net = tflearn.regression(net, optimizer='adam', metric = 'accuracy', loss='categorical_crossentropy')
	model = tflearn.DNN(net)
	return model
	
	
def train_model():
	print('Getting data...')
	input_data, labels = get_data()	
	X = np.reshape(input_data, [training_iterations, board_side_length*board_side_length])
	Y = np.reshape(labels, [training_iterations,2])	
	model = get_model()
	model.fit(X, Y, n_epoch = 100, show_metric=True)
	return model

def copy_board(board):
	board_copy = []
	for row in range(len(board)):
		for col in range(len(board[0])):
			board_copy.append(board[row][col])
	return board_copy

def ai_turn(player_nr, model, board):
	i=0
	predictions = []
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == 0:
				board_copy = copy_board(board)
				board_copy[i] = 1
				pred = model.predict(np.reshape(board_copy, [1, len(board_copy)]))
				predictions.append(pred[0][0])
			else:
				predictions.append(0)
			i += 1
	#print(str(predictions))
	flat_pos = predictions.index(max(predictions))
	pos = [math.floor(flat_pos/len(board)), flat_pos%(len(board))]
	board[pos[0]][pos[1]] = player_nr
	return pos, board


model = train_model()
model.save("model2.tfl")
print('model saved')
#*******Uncomment below to load the last saved model, Warning: Dimensions must be still the same*******
# model = get_model()
# model.load("model1.tfl")

num_played = 0
num_won = 0
for games in range(10):
	playing = True
	player = 1
	board = f.initialise_board(board_side_length, board_side_length)
	while playing:
		#f.print_board(board)
		if player == 1:
			#Change Player1 here, options: ai_turn, human_turn, random_turn
			pos, board = ai_turn(player, model, board)
		else:
			#Change Player2 here, options: human_turn, random_turn
			pos, board = f.random_turn(player, board)
		if f.check_has_won(board, player, pos[0], pos[1]) == True:
			break
		player = (player % 2) + 1
		if f.check_board_full(board):
			playing = False
		
	f.print_board(board)
	if playing:
		print('*****Player' + str(player) + ' has won*****')
		if player ==1:
			num_won += 1
	else:
		print('*****It\'s a draw*****')
	num_played += 1
	print(str(pos))
print(str(num_won/num_played))