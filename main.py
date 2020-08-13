
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


# check if the function call works 
display_board(board)

#################################################################

# the list scores should save the score of the positions left 
# by default we assume- the index corresponds to the position
position_scores = []

# Let's check what empty spots returns 
# empty spots returns all the spots that are not occupied by a move 
empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
print(f'Empty spots return value {empty_spots}')

# this finds the best move in the list of scores and returns the best move, 
# the best move is the index of the score
def find_best_move(position_scores):
	max_score = position_scores[0]
	best_move = 0
	for score in position_scores:
		if max_score < score:
			max_score = score
			best_move = position_scores.index(score)
	
	return best_move


################################################################

# function to check if there are any moves left on the table 
def is_moves_left(board):
	for spot in board:
		if(spot != "O" and spot != "X"):
			return True
	# if no moves left 
	return False




# the minimax function returns the max evaluation for the specific 
# postion specified 
def minimax(board, depth, is_max_player):
	# variable holds changing empty spots on the board based on game tree 
	empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
	
	# a list to hold the moves 
	moves= []

	# base case 
	#if depth == 0:
	if not is_moves_left(board):
		board_eval = evaluation(board)

		# append board evaluation to position scores 
		position_scores.append(board_eval)
		return board_eval


	# simulating the robot move 
	if is_max_player:
		max_eval = -10000
		# no go through each child of that position 
		for spot in empty_spots:
			# the board is modified to include the move
			board[spot] = robot
			
			# score of position evaluated revursively 
			pos_eval = minimax(board, depth-1, False)

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
			pos_eval = minimax(board, depth-1, True)

			# remove the move
			board[spot] = spot

			# append the move to moves array after adding 
			moves.append(spot)

			#retain minimum evaluation from the branch of the game tree
			min_eval = min(min_eval, pos_eval)

		return min_eval



#############
# TESTING
# now to test the minimax function on an actual move 
# creating a fake testing board 
test_board = [	0, 1, 2, 
				3, "O", 5, 
		 		6, 7, "X"]


#display_board(test_board)

print(f"The minimax evaluation returned {minimax(test_board, 3, True)}")

# TODO: weher did I specify which move it is evaluating it for, 
# the minimax should do this move specifically 

#################################################################



















################################################################################
# OLD CODE 
'''


#the main program loop
while(True):
	#this is so that the last empty spot is accounted for 
	#and the user is not allowed anymore inputs  
	empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
	if(len(empty_spots))==0:
		eval=evaluation(board)
		if eval > 0: 
			print(f'The winner is the robot')
		elif eval < 0:
			print(f'The winner is the human')
		else: 
			print("It's a damn tie")
		break

	#this works for the human input
	while(True):
		try:	
			human_input=int(input("Please enter an integer from 0 to 8: "))
			#this should only take in empty spots
			if(human_input>=0 and human_input<=8 and board[human_input]!="X"):
				break
		except ValueError:
			print("Input must be an integer value.")	
		else:
			print("That box is not empty- try again")
	#here you actually place the human input 
	board[human_input]= human

	#returns a list of empty positions in the array 
	empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
	print(empty_spots)

	moves= []
	for spot in empty_spots:
		spot_eval= minimax(spot, empty_spots, len(empty_spots), True)
		print(f'The spot eval for {spot} is {spot_eval}')
		moves.append(spot_eval)

	print(f'This is the moves array {moves}')
	#go through the moves array and pick out the best
	best_move= empty_spots[0]
	for move in moves:
		best_move= max(best_move, move)
	print(f'The best move is {best_move}')
	#this part works
	board[best_move]=robot

'''