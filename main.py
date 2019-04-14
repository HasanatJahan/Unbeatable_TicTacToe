
board= [ "X", 1, 2, 
		 3, "O", 5, 
		 "X", 7, 8]

human = "O"
robot= "X"


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


def evaluation(board):
	if (winning(board, robot)):
		return +10
	elif (winning(board, human)):
		return -10
	else:
		return 0


def minimax(spot, empty_spots, depth, maximizing_player):
	if depth==0 or len(empty_spots)==0:
		# print(f'The evaluation function returns: {evaluation(board)}')
		return evaluation(board)

	if maximizing_player:
		maxEval= -1000000
		empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
		# print(f'testing empty spots from maximizing_player{empty_spots}')
		
		#for the child of that position
		for spot in empty_spots:
			board[spot]=robot
			eval = minimax(spot, empty_spots, depth-1, False)

			#then remove the move and replace it with the number
			board[spot]=spot
			maxEval= max(maxEval, eval)
			# print(f'The maxEval is {maxEval}')
		# print(f'The maxEval is {maxEval}')
		return maxEval

	else:
		minEval= +1000000
		# board[spot]=human
		empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
		# print(f'testing empty spots from minimizing_player{empty_spots}')

		#for each child of that position
		for spot in empty_spots:
			board[spot]=human
			eval= minimax(spot, empty_spots, depth-1, True)

			#then remove the spot
			board[spot]=spot
			minEval=min(minEval, eval)
		# print(f'The minEval is {minEval}')
		return minEval



#the main program loop
while(True):

	while(True):
		try:	
			human_input=int(input("Please enter an integer from 0 to 8: "))
			#this should only take in empty spots
			if(human_input>=0 and human_input<=8):
				break
		except ValueError:
			print("Input must be an integer value.")	

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
	print(best_move)

