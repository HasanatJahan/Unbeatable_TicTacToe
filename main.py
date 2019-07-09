
board= [ 0, 1, 2, 
		 3, 4, 5, 
		 6, 7, 8]

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
	if (winning(board, human)):
		return -10
	elif (winning(board, robot)):
		return +10
	else:
		return 0

################################################################################


def minimax(spot, empty_spots, depth, maximizing_player):
	empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
	
	if depth==0 or len(empty_spots)==0:
		eval= evaluation(board)
		# print(f'The evaluation function returns: {evaluation(board)}')
		# return evaluation(board)
		return eval

	if maximizing_player:
		maxEval= -1000000		
		#for the child of that position
		for spot in empty_spots:
			board[spot]=robot
			eval = minimax(spot, empty_spots, depth-1, False)

			board[spot]=spot
			maxEval= max(maxEval, eval)

		return maxEval

	else:
		minEval= +1000000
		# empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
		# print(f'testing empty spots from minimizing_player{empty_spots}')

		#for each child of that position
		for spot in empty_spots:
			board[spot]=human
			eval= minimax(spot, empty_spots, depth-1, True)

			board[spot]=spot
			minEval=min(minEval, eval)

		return minEval


#####################################################################################

#the main program loop
while(True):
	#this is so that the last empty spot is accounted for 
	#and the user is not allowed anymore inputs  
	empty_spots=list(filter(lambda spot: (spot!="O" and spot!="X"), board))
	if(len(empty_spots))==0:
		eval=evaluation(board)
		print(f'The winner is {eval}')
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

##############################################################################
### THe evaluations are being accounted for?/done? wrong 
###
##############################################################################