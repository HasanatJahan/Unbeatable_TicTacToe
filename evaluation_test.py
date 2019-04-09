

board_1=[
		"O", "O", "O",
		"X", 5, 6, 
		"X", "X", 8
		]

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
	#trying to get another value
	# else:
		# return 2

print(evaluation(board_1))