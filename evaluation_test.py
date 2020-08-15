board_1= [ "X", 1, 2, 
   		   3, "O", 5, 
		   "X", 7, 8]

board_2=["X","X","X",
		  3, 4, 5,
		  6, "O", 8]

board_3=["O","X","O",
		  3,"O",5,
		  6, 7,"O"]

board_4=["O",1,"X",
		"O", 4, "X",
		"O",7, "X"]

board_5=[ 0, "X", "O", 
		 3, 4, 5, 
		 6, "X", 8]


human = "O"
robot= "X"

#winning board combinations
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


#evaluates the score of the game
def evaluation(board):
	if (winning(board, human)):
		return -10
	elif (winning(board, robot)):
		return +10
	# elif(len(empty_spots)==0):
	else:
		return 0



print(f'Evaluation board_1: {evaluation(board_1)}')
# print(f'Evaluation board_2: {evaluation(board_2)}')
# print(f'Evaluation board_3: {evaluation(board_3)}')
# print(f'Evaluation board_4: {evaluation(board_4)}')
# print(f'Evaluation board_5: {evaluation(board_5)}')


#function to check end state of the game 
def game_over(board_5):
	return winning(board_5, robot) or winning(board_5, human)


scores=[]	#an array of scores
moves=[]	#an array of moves

def minimax(board, depth, maximizing_player, moves):
	#pick out the empty spots left
	empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board_5))

	#checking base case 
	if depth==0 or game_over(board_5):
		func_eval= evaluation(board_5)
		# moves.append(func_eval)
		print(board_5 , func_eval)

		return func_eval


	for spot in empty_spots:
		if maximizing_player:
			func_eval= -100000
			#place robot in that spot 
			board_5[spot]=robot
			#find maximum evaluation
			func_eval= max(func_eval, minimax(empty_spots, depth-1, False, moves))
			#remove the placed robot
			board_5[spot]= spot
			# moves.append(func_eval)


		else:
			func_eval= +100000
			#place the human input 
			board_5[spot]=human
			#find the minimum evaluation
			func_eval=min(func_eval, minimax(empty_spots, depth-1, True, moves))
			#remove the empty spot
			board_5[spot]= spot
			# moves.append(func_eval)

			
		moves.append(func_eval)


	return func_eval


############################################################################
#Testing
print(f'Testing if the moves array was empty to begin with {moves}')
empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board_5))
print(f'Print the length of the empty spot {len(empty_spots)}')


spot_eval_5= minimax(board_5, len(empty_spots), True, moves)

# print(f'spot_eval_5 is {spot_eval_5}')
print(f'This is the moves array {moves}')
print(f'The length of the moves array {len(moves)}')

##############################################################################





"""
def print_board(board):
	board_string = ''
	for i in range(5):
		for j in range(5):
			if(i%2!=0 and j%2==0):
				print("|", end=" "),
			elif(i%2==0 and j%2!=0):
				print("__", end=" "),
			else:
				print("  ", end=" "),
		print("\n")


print_board(board_5)


############
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
"""