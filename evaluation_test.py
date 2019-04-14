board= [ "X", 1, 2, 
		 3, "O", 5, 
		 "X", 7, 8]

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
	if (winning(board, robot)):
		return +10
	elif (winning(board, human)):
		return -10
	elif(len(empty_spots)==0):
		return 0

def minimax(spot, empty_spots, depth, maximizing_player):
	if depth==0:
		eval= evaluation(board)
		print(f'The evaluation function returns: {evaluation(board)}')
		return eval

	if maximizing_player:
		maxEval= -1000000
		
		#place it here and then check all the children
		board[spot]=robot

		#for each move in all possible moves
		for spot in empty_spots:

			#make the move
			# board[spot]=robot

			#evaluate the outcome of the move
			eval = minimax(spot, empty_spots, depth-1, False)

			#then remove the move and replace it with the number
			# board[spot]=spot
			
			maxEval= max(maxEval, eval)

		# print(f'The maximum evaluation {maxEval}')

		#remove the move
		board[spot]=spot

		return maxEval

	else:
		minEval= +1000000

		#place the human spot
		board[spot]=human

		#for each move in all possible moves
		for spot in empty_spots:

			#make the move 
			# board[spot]=human

			#evaluate the outcome of the move
			eval= minimax(spot, empty_spots, depth-1, True)

			#then remove the spot
			board[spot]=spot

			#figure out the minimal evaluation
			minEval=min(minEval, eval)

		# print(f'The minimal evaluation is {minEval}')
		#remove the human
		board[spot]=spot

		return minEval




empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))

for spot in empty_spots:
	spot_eval= minimax(spot, empty_spots, len(empty_spots), True)
	print(f'The spot eval is {spot_eval}')


print(evaluation(board_1))