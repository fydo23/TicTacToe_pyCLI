from game.players import Computer, User

class Board:

	board = ['1','2','3',
			 '4','5','6',
			 '7','8','9']

	def __getitem__(self,index):
		return self.board[index]

	def set_position(self,pos,player):
		self.board[pos] = player
		return self

	def test_winners(self):
		board = self.board
		"""
		Test if any rows, columns or diagonals are winners by using the following index layout:
		0,1,2
		3,4,5
		6,7,8
		"""
		if ((board[0] == board[1] == board[2]) or 
			(board[3] == board[4] == board[5]) or
			(board[6] == board[7] == board[8]) or 
			(board[0] == board[3] == board[6]) or
			(board[1] == board[4] == board[7]) or
			(board[2] == board[5] == board[8]) or
			(board[0] == board[4] == board[8]) or
			(board[2] == board[4] == board[6])):
			return True
		return False

	def get_possible_win_count(self, position, player):
		good_spaces = [1,2,3,4,5,6,7,8,player]
		all_winners = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
		winners = []
		for pos_winner in all_winners:
			good_winner = True
			for x in range(1,4):
				if self.board[pos_winner[x-1]-1] not in good_spaces:
					good_winner = False
			if good_winner:
				winners.append(pos_winner)
		return len(winners)

	def print_board(self):
		board = self.board
		print " "+ board[0] + " | " + board[1] + " | " + board[2] 
		print "---+---+---"
		print " "+ board[3] + " | " + board[4] + " | " + board[5]
		print "---+---+---"
		print " "+ board[6] + " | " + board[7] + " | " + board[8] 


class Engine:

	players = [None,None]
	board = None

	game_over = False
	move_counter = 0
	current_player_index = 0

	def __init__(self, no_player=False):
		"""
		Play a simple game of Tic Tac Toe. 
		"""
		if no_player:
			self.players[0] = Computer("X")
		else:
			self.players[0] = User()
		self.players[1] = Computer(self.players[0].get_opponent_player())

		self.board = Board()
		if self.players[0]._player == "O":
			self.current_player_index = 1

	def get_current_player(self):
		return self.players[self.current_player_index]

	def play(self):
		while not self.game_over:
			self.get_move()

	def get_move(self):
		# print "Player "+self.get_current_player()+"'s turn. "
		self.board.print_board()
		self.get_current_player().do_move(self.board)
		self.move_counter+=1
		if self.board.test_winners():
			self.board.print_board()
			self.game_over = True
			print "Player " + self.get_current_player()._player + " WINS!"
			return
		if self.move_counter >= 9:
			self.board.print_board()
			self.game_over = True
			print "The game is a DRAW!"
			return
		self.current_player_index = (self.current_player_index + 1) % 2;

