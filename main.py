
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

#the main program loop
while(True):
	
	while(True):
		try:
			human_input=int(input("Please enter your move corresponding to the box number: "))
			break
		except ValueError:
			print("Please enter a postitive integer value: ")
		

	#returns a list of empty positions in the array 
	empty_spots=[]
	def empty_spots_func(board):
		for i in board:
			if(i!="X" and i!="O"):
				empty_spots.append(i)


	#evaluates the score of the game
	def evaluation(board):
		if (winning(board, human)):
			score=+10
		elif (winning(board, robot)):
			score=-10
		elif(len(empty_spots)==0):
			score=0

	#this will store the evaluation of the moves of each empty spot
	moves=[]
	#this will decide the best possible move- 
	def minimax(current_position, depth, maximizing_player): 	
		#this updates the empty spots available on the board
		empty_spots_func(board)

		pass

