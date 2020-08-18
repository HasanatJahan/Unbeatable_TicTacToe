# the game board

board= [ 0, 1, 2, 
		 3, 4, 5, 
		 6, 7, 8]

# the players in the game 
human = "O"
robot= "X"

# these define if the player is winning 
def winning(board, player):
	""" Determines if there is a winning combination in game board 
		Args: 
			board: list representing the game board with positions 
			player: represents which player holds winning position
		Returns:
			Boolean whether there is a win or not for player
	"""
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
	""" Evaluates the game board to determine game state 
		Args: 
			board: list representing the game board with positions 
		Returns:
			Integer representing game state
	"""
	if (winning(board, human)):
		return -10
	elif (winning(board, robot)):
		return +10
	else:
		return 0


# Create a function to display the board 
# the board will modify according to the move the player makes 
# this function will simpy display that 
def display_board(board):
	""" Displays the list game board as a tictactoe board on the console
		Args: 
			board: list representing the game board with positions 
		Returns:
			Prints the game board as a string on the console
	"""
	print(f" {board[0]} | {board[1]} | {board[2]} ")
	print("___________")
	print(f" {board[3]} | {board[4]} | {board[5]} ")
	print("___________")
	print(f" {board[6]} | {board[7]} | {board[8]} ")


# function to check if there are any moves left on the table 
def is_moves_left(board):
	""" Determines if there are moves left on the baord
		Args: 
			board: list representing the game board with positions 
		Returns:
			Boolean whether there are any empty spots or not
	"""
	for spot in board:
		if(spot != "O" and spot != "X"):
			return True
	# if no moves left 
	return False


# function to find empty spots on the board 
def find_empty_spots(board):
	""" Finds the empty spots on the board 
		Args: 
			board: list representing the game board with positions 
		Returns:
			Returns a list of empty spots on the board
	"""
	empty_spots = []
	for spot in board:
		if(spot != "X" and spot != "O"):
			empty_spots.append(spot)
	return empty_spots



# function that keeps track whether the game is over or not 
def game_over(board):
	""" Determines if the game state is game over 
		Args: 
			board: list representing the game board with positions 
		Returns:
			Boolean whether the game is over or not
	"""
	game_won = (evaluation(board) == 10 or evaluation(board) == -10)
	if game_won or not is_moves_left(board):
		return True
	return False



def minimax(board, is_max_player):
	""" Finds the best evaluation of game tree for robot for spot in gameplay
		Args: 
			board: list representing the game board with positions 
			is_max_player : boolean whether it is the robot or not
		Returns:
			Integer value for maximum evaluation for robot in game tree
	"""
	# variable holds changing empty spots on the board based on game tree 
	empty_spots = find_empty_spots(board)

	# base case 
	if game_over(board): 
		board_eval = evaluation(board)
		return board_eval


	# simulating the robot move 
	if is_max_player:
		max_eval = -10000
		# no go through each child of that position 
		for spot in empty_spots:
			
			# the board is modified to include the move
			board[spot] = robot
			
			# score of position evaluated revursively 
			pos_eval = minimax(board, False)

			# after evaluation is found, remove the move 
			board[spot] = spot

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

			#retain minimum evaluation from the branch of the game tree
			min_eval = min(min_eval, pos_eval)

		return min_eval



# the list scores should save the score of the positions left 
# by default we assume- the index corresponds to the position
# populate it with large values so that the occupied spots are not picked 
position_scores = [ -10000, -10000, -10000, 
					-10000, -10000, -10000, 
					-10000, -10000, -10000]


# this finds the best move in the list of scores and returns the best move, 
# the best move is the index of the score - within position scores 
def find_best_move(position_scores):
	""" Finds the index of the higest score in position scores
		Args: 
			position_scores: list representing the scores for positions to play in board
		Returns:
			Integer index presenting position in board 
	"""
	max_score = position_scores[0]
	best_move = 0
	for score in position_scores:
		if max_score < score:
			max_score = score
			best_move = position_scores.index(score)
	
	return best_move





##################
#### GAMEPLAY ####
##################

def initialize_game(board):	
	""" Initializes the game for player
		Args: 
			board: list representing the game board with positions 
		Returns:
			Prints to screen to prompt the user to begin playing
	"""
	print("Hello human!")
	print("I hope you're having a great day.")
	print("Get Ready for DEFEAT.")
	display_board(board)
	print("Get ready to make your move.")

# initialize the game 
initialize_game(board)

# Now for the main program loop - the gameplay portion of the game
def game_run(board):
	""" Game play portion
		Args: 
			board: list representing the game board with positions 
		Returns:
			Interactive gameplay 
	"""
	while(True):
		# this is so that the last empty spot is accounted for 
		# and the user is not allowed anymore inputs  
		# empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
		# invoking the game over function 
		if game_over(board): 
			game_eval=evaluation(board)
			if game_eval > 0: 
				print(f'THE WINNER IS THE ROBOT!')
				break # this is for there for the game play to end 
			elif game_eval < 0:
				print(f'The winner is the you - it must be a bug please be nice to my bot :(')
				break
			else: 
				print("It's a draw! But considering a draw with a bot...")
				break
			break


		# this works for the human input - takes a valid input and breaks the loop 
		# the while loop is not broken until the right input is put
		while(True):
			try:	
				print(f"Make your move from spots {find_empty_spots(board)}")

				human_input=int(input("Please enter an number: "))
				
				# this should only take in empty spots with no robot or human input
				if(human_input >= 0 and human_input <= 8 and board[human_input] != robot and board[human_input] != human):
					break
			except ValueError:
				print("Input must be an number value, it's right there in the instructions.")	
			else:
				print("That box is not empty - try again")

		# Now to take that human input and add it to the board 
		board[human_input] = human 

		# Now for the robot to choose the best move based on the minimax
		# algorithm 

		# update the list of empty spots 
		# empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
		empty_spots = find_empty_spots(board)

		## now we have to reset position scores  - new change 
		position_scores = [ -10000, -10000, -10000, 
							-10000, -10000, -10000, 
							-10000, -10000, -10000]



		# this is where minimax comes in 
		# now run the program and find the best move out of empty spots
		for spot in empty_spots:
			# place the move
			board[spot] = robot
			# run minimax starting with the human's turn 
			position_scores[spot] = minimax(board, False)
			# remove the move  
			board[spot] = spot


		# after finding the evaluation for all the empty spots- 
		# find the best move from all the evalauted moves and make the move 
		robot_move = find_best_move(position_scores)


		## now we have to reset position scores  - new change 
		position_scores = [ -10000, -10000, -10000, 
							-10000, -10000, -10000, 
							-10000, -10000, -10000]
		
		# make the robot move
		# adding a statement so that it does not override the plates move here
		# if there is already nothing occupied there
		if board[robot_move] != robot and board[robot_move] != human:
			board[robot_move] = robot
			print(f"The bot has chosen it's move at spot {robot_move}")
		
		# finally display board before asking for input again
		display_board(board)

# Run the game 
game_run(board)


