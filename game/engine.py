from game.players import Computer, User
from board import Board

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