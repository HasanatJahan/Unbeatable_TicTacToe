
board= ["O", 1, "X", 
		"X", 4, "X", 
		6, "O", "O"]

human = "O"
robot= "X"


#winning board combinations
def winning(board, player):
		#horizontal test
	if((board[0] == player and board[1]==player and board[2]==player) or
		(board[3]==player and board[4]==player and board[5]==player) or
		(board[6]==player and board[7]==player and board[8]==player) or
		#diagonals test
		(board[0]==player and board[4]==player and board[8]==player) or
		(board[2]==player and board[4]==player and board[6]==player) or
		#verticals test
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
		return +10
	elif (winning(board, robot)):
		return -10
	elif(len(empty_spots)==0):
		return 0
	else:
		return 2


#this is to find the empty spots on the board 
def empty_spots_func(board):
	for i in board:
		if(i!="X" and i!="O"):
			empty_spots.append(i)


def minimax(spot, empty_spots, depth, maximizing_player):
	if depth==0:
		eval= evaluation(board)
		print("The evaluation function returns: ")
		print(evaluation(board))
		return eval

	if maximizing_player:
		maxEval= -1000000
		#for each move in all possible moves
		for spot in empty_spots:
		
			#make the move
			board[spot]=robot

			eval = minimax(spot, empty_spots, depth-1, False)
			maxEval= max(maxEval, eval)
		return maxEval

	else:
		minEval= +1000000
		#for each move in all possible moves
		for spot in empty_spots:

			#make the move 
			board[spot]=human

			eval= minimax(spot, empty_spots, depth-1, True)
			minEval=min(minEval, eval)
		return minEval



#the main program loop
while(True):

	while(True):
		try:	
			human_input=int(input("Please enter an integer from 0 to 8: "))
			if(human_input>=0 and human_input<=8):
				break
		except ValueError:
			print("Input must be an integer value.")	


	#returns a list of empty positions in the array 
	empty_spots=[]
	empty_spots_func(board)

	moves= []
	for spot in empty_spots:
		spot_eval= minimax(spot, empty_spots, len(empty_spots), True)
		moves.append(spot_eval)
		print("The spot eval is: ")
		print(spot_eval)



