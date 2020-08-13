
board= [ 0, 1, 2, 
		 3, 4, 5, 
		 6, 7, 8]

human = "O"
robot= "X"

# these define if the player is winning 
def winning(board, player):
		#horizontal tests
	if((board[0] == player and board[1]==player and board[2]==player) or
		(board[3]==player and board[4]==player and board[5]==player) or
		(board[6]==player and board[7]==player and board[8]==player) or
		#diagonal tests
		(board[0]==player and board[4]==player and board[8]==player) or
		(board[2]==player and board[4]==player and board[6]==player) or
		#vertical tests
		(board[0]==player and board[3]==player and board[6]==player) or
		(board[1]==player and board[4]==player and board[7]==player) or
		(board[2]==player and board[5]==player and board[8]==player)
		):
		return True
	else:
		return False

# Evaluation function of board that returns positive for robot but negative for robot 
def evaluation(board):
	if (winning(board, human)):
		return -10
	elif (winning(board, robot)):
		return +10
	else:
		# made draw a 5 to make the position score array to work
		return 0


# Create a function to display the board 
# the board will modify according to the move the player makes 
# this function will simpy display that 
def display_board(board):
	print(f" {board[0]} | {board[1]} | {board[2]} ")
	print("___________")
	print(f" {board[3]} | {board[4]} | {board[5]} ")
	print("___________")
	print(f" {board[6]} | {board[7]} | {board[8]} ")


# function to check if there are any moves left on the table 
def is_moves_left(board):
	for spot in board:
		if(spot != "O" and spot != "X"):
			return True
	# if no moves left 
	return False

###########################################################################

def find_empty_spots(board):
	empty_spots = []
	for spot in board:
		if(spot != "X" and spot != "O"):
			empty_spots.append(spot)
	return empty_spots

# testing the empty spots function
print(f"Empty spots from new function  {find_empty_spots(board)}")

# the minimax function returns the max evaluation for the specific 
# postion specified 
def minimax(board, is_max_player):
	# variable holds changing empty spots on the board based on game tree 
	# empty_spots=list(filter(lambda spot: (spot != "O" and spot != "X"), board))
	empty_spots = find_empty_spots(board)
	# print(f"Empty spots in gameplay {empty_spots}")

	# a list to hold the moves 
	moves= []

	# base case 
	#if depth == 0:
	if not is_moves_left(board):
		board_eval = evaluation(board)

		# append board evaluation to position scores 
		# position_scores.append(board_eval)
		return board_eval


	# simulating the robot move 
	if is_max_player:
		max_eval = -10000
		# no go through each child of that position 
		for spot in empty_spots:
			
			# testing 
			#print(f"this is what board returns in minimax {display_board(board)}")

			# the board is modified to include the move
			board[spot] = robot
			
			# score of position evaluated revursively 
			pos_eval = minimax(board, False)

			# after evaluation is found, remove the move 
			board[spot] = spot

			# append the move to moves array after adding 
			moves.append(spot)

			# retain maximum evaluation from branch of game tree
			max_eval = max(max_eval, pos_eval)

		return max_eval

	# simulating the human move 
	else:
		min_eval = +10000
		
		# now go through each child of the tree based on the move
		for spot in empty_spots:

			# board is modified to include the move
			board[spot] = human 

			# score of postion evaluated recursively
			pos_eval = minimax(board, True)

			# remove the move
			board[spot] = spot

			# append the move to moves array after adding 
			moves.append(spot)

			#retain minimum evaluation from the branch of the game tree
			min_eval = min(min_eval, pos_eval)

		return min_eval



#####################################################################

# the list scores should save the score of the positions left 
# by default we assume- the index corresponds to the position

# populate it with large values so that the occupied spots are not picked 
position_scores = [-10000, -10000, -10000, 
					-10000, -10000, -10000, 
					-10000, -10000, -10000]

# this finds the best move in the list of scores and returns the best move, 
# the best move is the index of the score - within position scores 
def find_best_move(position_scores):
	max_score = position_scores[0]
	best_move = 0
	for score in position_scores:
		if max_score < score:
			max_score = score
			best_move = position_scores.index(score)
	
	return best_move


#################################################################
#### GAMEPLAY ####
##################

def initialize_game(board):
	print("Hello human!")
	print("I hope you're having a great day.")
	print("Get Ready for DEFEAT.")
	print("Get ready to make your move.")

# initialize the game 
initialize_game(board)

# Now for the main program loop - the gameplay portion of the game

# Let's check what empty spots returns 
# empty spots returns all the spots that are not occupied by a move 

def game_run(board):
	while(True):
		# this is so that the last empty spot is accounted for 
		# and the user is not allowed anymore inputs  
		# empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
		if not is_moves_left:
			game_eval=evaluation(board)
			if game_eval > 0: 
				print(f'The winner is the robot')
				break # this is for there for the game play to end 
			elif game_eval < 0:
				print(f'The winner is the human')
				break
			else: 
				print("It's a damn tie")
				break
			break


		#this works for the human input - takes a valid input and breaks the loop 
		# the while loop is not broken until the right input is put
		while(True):
			try:	
				print(f"Make your move from spots {find_empty_spots(board)}")
				display_board(board)
				human_input=int(input("Please enter an integer: "))
				#this should only take in empty spots
				if(human_input>=0 and human_input<=8 and board[human_input]!=robot):
					break
			except ValueError:
				print("Input must be an integer value, it's right there in the instructions.")	
			else:
				print("That box is not empty - try again")

		# Now to take that human input and add it to the board 
		board[human_input] = human 

		# display the board again 
		# display_board(board)

		# Now for the robot to choose the best move based on the minimax
		# algorithm 

		# update the list of empty spots 
		available_moves=list(filter(lambda spot: (spot!="O" and spot!="X"), board))

		# this is where minimax comes in 
		# now run the program and find the best move out of empty spots
		for spot in available_moves:
			# place the move
			board[spot] = robot
			# run minimax for robot turn to find the best evaluation for move
			position_scores[spot] = minimax(board, True)
			# remove the move and 
			board[spot] = spot

		# after finding the evaluation for all the empty spots- 
		# find the best move from all the evalauted moves and make the move 
		robot_move = find_best_move(position_scores)
		board[robot_move] = robot

		print("The bot has chosen it's move ")
		display_board(board)





game_run(board)


