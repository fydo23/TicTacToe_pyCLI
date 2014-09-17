#!/usr/bin/env python
from cli.app import CommandLineApp

input = raw_input
PLAYERS = ["X","O"]

class TicTacToeApp(CommandLineApp):

	name = "TicTacToe"

	move_counter = 0;
	current_player = 0
	user_player = ""
	game_over = False
	board = ['1','2','3',
			 '4','5','6',
			 '7','8','9']

	def setup(self):
		super(TicTacToeApp,self).setup()
		# define self.params.player via input param 
		self.add_param("-n", "--no-player", help="Plays the game as two computers.", 
			default=0, action="store_true")
		
	# This is called after run() completes setup()
	def main(self):
		"""
		Play a simple game of Tic Tac Toe. 
		"""
		while not (self.params.no_player or self.user_player):
			self.set_user_player()
		while not self.game_over:
			self.play()
		print "fin."

	def set_user_player(self):
		player = input("Will you play as X's (go first) or O's: ").upper()
		if player not in PLAYERS:
			print "invalid player."
			return
		self.user_player = player
		print "You are playing as player "+ player + "."

	def get_current_player(self):
		return PLAYERS[self.current_player]

	def play(self):
		if self.get_current_player() == self.user_player:
			move = self.get_user_move()
		else:
			move = self.get_computer_move()
		#plave the position.
		self.board[move-1] = self.get_current_player()
		self.move_counter+=1
		if self.test_winners():
			self.game_over = True
			print "Player " + self.get_current_player() + " WINS!"
			self.print_board()
			return
		if self.move_counter >= 9:
			self.game_over = True
			print "The game is a DRAW!"
			self.print_board()
			return
		self.current_player = (self.current_player + 1) % 2;

	def get_user_move(self):
		"""
		Prompt yser and retun the requested position.
		"""
		self.print_board()
		move = None
		print "moveCounter:"+str(self.move_counter)
		while not move:
			try: 
				input_move = int(input("Where would you like to place your '" + self.get_current_player() + "'? "))
				if 0 < input_move <= 9 and self.board[input_move-1] not in PLAYERS:
					move = input_move
				else:
					raise ValueError()
			except ValueError:
				print "invalid input"
		return move

	def get_computer_move(self):
		print "computer is thinking..."
		for x in range(1,10):
			if self.board[x-1] not in PLAYERS:
				print "computer placed " + self.get_current_player() + " in position " + str(x)
				return x

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

	def print_board(self):
		board = self.board
		print " "+ board[0] + " | " + board[1] + " | " + board[2] 
		print "---+---+---"
		print " "+ board[3] + " | " + board[4] + " | " + board[5]
		print "---+---+---"
		print " "+ board[6] + " | " + board[7] + " | " + board[8] 



if __name__ == "__main__":
	TicTacToeApp().run()

