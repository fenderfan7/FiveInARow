import FiveInARowFunctions as f
import tensorflow as tf
import tflearn
import numpy as np
import math

learning_rate = 0.01
training_iterations = 50000
# Change board dimensions here, Warning: Can only load model, if board dimensions stay the same!
board_side_length = 5
board_history_length = 5 #must be smaller than 6

def get_data():
	data = []
	labels = []
	for iteration in range(training_iterations):
		playing = True
		player = 1
		board = f.initialise_board(board_side_length, board_side_length)
		last_boards = []
		while playing:
			pos, board = f.random_turn(player, board)
			if f.check_has_won(board, player, pos[0], pos[1]) == True:
				break
			player = (player % 2) + 1
			if f.check_board_full(board):
				playing = False
			last_boards.append(board)
			if len(last_boards) > board_history_length:
				del last_boards[0]
		data.append(last_boards)
		if player == 1:
			for _ in range(len(last_boards)):
				labels.append([1,0]) #win for player1
		else:
			for _ in range(len(last_boards)):
				labels.append([0,1]) #win for player1
			
		print('Get data iteration: ' + str(iteration))
	return data, labels
def get_model():
	tflearn.init_graph(num_cores = 4)
	net = tflearn.input_data(shape=[None, board_side_length, board_side_length, 1])
	#Hidden Layer, change dimensions/number of nodes here
	net = tflearn.conv_2d(net, 8, 5,activation = 'relu', padding = 'valid')
	net = tflearn.conv_2d(net, 8, 5,activation = 'relu', padding = 'same')
	net = tflearn.conv_2d(net, 8, 5,activation = 'relu', padding = 'same')
	net = tflearn.conv_2d(net, 8, 5,activation = 'relu', padding = 'same')
	
	net = tflearn.fully_connected(net, 2, activation='softmax')
	net = tflearn.regression(net, optimizer='adam', metric = 'accuracy', loss='categorical_crossentropy')
	model = tflearn.DNN(net)
	return model
	
	
def train_model():
	print('Getting data...')
	input_data, labels = get_data()	
	X = np.reshape(input_data, [training_iterations*board_history_length, board_side_length, board_side_length, 1])
	Y = np.reshape(labels, [training_iterations*board_history_length,2])	
	model = get_model()
	model.fit(X, Y, n_epoch = 3, show_metric=True)
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
				pred = model.predict(np.reshape(board_copy, [1, board_side_length, board_side_length, 1]))
				predictions.append(pred[0][0])
			else:
				predictions.append(0)
			i += 1
	#print(str(predictions))
	flat_pos = predictions.index(max(predictions))
	pos = [math.floor(flat_pos/len(board)), flat_pos%(len(board))]
	board[pos[0]][pos[1]] = player_nr
	return pos, board

def test_model(model):
	data, labels = get_data()
	test_pos = 0
	for i in range(len(data)):
		print('Testing iteration: ' + str(i))
		pred = model.predict(np.reshape(data[i][0], [1, board_side_length, board_side_length, 1]))
		val = int(np.round(pred[0][0])) 
		if val == labels[i][0]:
			test_pos +=1
	print('test accuracy: ' + str(test_pos/len(data)))
		
model = train_model()
test_model(model)
model.save("model2.tfl")
print('model saved')
#*******Uncomment below to load the last saved model, Warning: Dimensions must be still the same*******
# model = get_model()
# model.load("model2.tfl")

num_played = 0
num_won = 0

for games in range(100):
	playing = True
	player = 1
	board = f.initialise_board(board_side_length, board_side_length)
	# board[2][4] = 2
	# board[6][4] = 1
	# board[7][3] = 1
	# board[8][2] = 1
	# board[9][1] = 0
	# board[10][0] = 1
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
		
	#f.print_board(board)
	if playing:
		print('*****Player' + str(player) + ' has won*****')
		if player ==1:
			num_won += 1
	else:
		num_won+=0.5
		print('*****It\'s a draw*****')
	num_played += 1
	print(str(pos))
print(str(num_won/num_played))