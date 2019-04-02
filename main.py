
board= ["O", 1, "X", 
		"X", 4, "X", 
		6, "O", "O"]

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




#this is to find the empty spots on the board 
# I THINK IT WOULD BE BETTER TO USE A FILTER HERE BECAUSE 
# WE HAVE TO INITIALIZE EMPTY_SPOTS ARRAY EVERYWHERE AND THATS NOT GOOD 
def empty_spots_func(board):
	# empty_spots=[]
	for i in board:
		if(i!="X" and i!="O"):
			empty_spots.append(i)




def minimax(spot, empty_spots, depth, maximizing_player):
	if depth<=0:
		eval= evaluation(board)
		# print(f'The evaluation function returns: {evaluation(board)}')
		return eval

	if maximizing_player:
		maxEval= -1000000
		#for each move in all possible moves
		for spot in empty_spots:
		
			#make the move
			board[spot]=robot

			#evaluate the outcome of the move
			eval = minimax(spot, empty_spots, depth-1, False)

			#then remove the move and replace it with the number
			board[spot]=spot
			
			maxEval= max(maxEval, eval)

		# print(f'The maximum evaluation {maxEval}')
		return maxEval

	else:
		minEval= +1000000
		#for each move in all possible moves
		for spot in empty_spots:

			#make the move 
			board[spot]=human

			#evaluate the outcome of the move
			eval= minimax(spot, empty_spots, depth-1, True)

			#then remove the spot
			board[spot]=spot

			#figure out the minimal evaluation
			minEval=min(minEval, eval)

		# print(f'The minimal evaluation is {minEval}')
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

	#now actually place the human input in the postion
	board[human_input]= human

	#CHECK IF ANYONE WON - IF YES DECLARE WINNER AND REFRESH BOARDS
	#ACTUALLY FIRST CHECK WHICH WOULD BE THE BEST PLACE TO PUT IF SOMEONE HAS WON

	#returns a list of empty positions in the array 
	empty_spots=[]
	empty_spots_func(board)
	print(empty_spots)

	moves= []
	for spot in empty_spots:
		spot_eval= minimax(spot, empty_spots, len(empty_spots), True)
		print(f'The spot eval is {spot_eval}')
		moves.append(spot_eval)
	# print(f'The spot eval is {test_spot_eval}')

	#go through the moves array and pick out the best
	best_move= empty_spots[0]
	for move in moves:
		best_move= max(best_move, move)
	print(best_move)

	#place the robots move 
	board[best_move]= robot
	print(board)