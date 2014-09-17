#!/usr/bin/env python
from cli.app import CommandLineApp

input = raw_input
PLAYERS = ["X","O"]

class TicTacToeApp(CommandLineApp):

	name = "TicTacToe"

	current_player = 0
	game_over = False
	board = ['1','2','3',
			 '4','5','6',
			 '7','8','9']

	def main(self):
		"""
		Play a simple game of Tic Tac Toe
		"""
		while not self.params.player:
			self.set_user_player()
		while not self.game_over:
			self.play()
		print "The game has ended. :'("

	def print_board(self):
		board = self.board
		print " "+ board[0] + " | " + board[1] + " | " + board[2] 
		print "---+---+---"
		print " "+ board[3] + " | " + board[4] + " | " + board[5]
		print "---+---+---"
		print " "+ board[6] + " | " + board[7] + " | " + board[8] 

	def set_user_player(self):
		player = input("Will you play as X's (go first) or O's: ").upper()
		if player not in ['X','O']:
			print "invalid player."
			return
		self.params.player = player
		print "You are playing as player "+ player + "."

	def get_current_player(self):
		return PLAYERS[self.current_player]

	def play(self):
		if self.get_current_player() == self.params.player:
			move = self.get_user_move()
		else:
			move = self.get_computer_move()
		#plave the position.
		self.board[move-1] = self.get_current_player()
		if self.test_winners():
			self.game_over = True;
		self.current_player = (self.current_player + 1) % 2;

	def get_user_move(self):
		"""
		Prompt yser and retun the requested position.
		"""
		self.print_board()
		move = None
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
		for x in range(1,9):
			if self.board[x-1] not in PLAYERS:
				print "computer placed " + self.get_current_player() + " in position " + str(x)
				return x

	def test_winners(self):
		board  = self.board
		if ((board[0] == board[1] == board[2]) or 
			(board[3] == board[4] == board[5]) or
			(board[6] == board[7] == board[8]) or 
			(board[0] == board[3] == board[2]) or
			(board[1] == board[4] == board[5]) or
			(board[2] == board[5] == board[8]) or
			(board[0] == board[4] == board[8]) or
			(board[2] == board[4] == board[6])):
			self.game_over = True;
			print "Player " + self.get_current_player() + " WINS!"
			self.print_board()

	def setup(self):
		super(TicTacToeApp,self).setup()
		self.add_param("-p", "--player", help="Choose X or O. X goes first", 
			default=None, action="store_true")
		


if __name__ == "__main__":
	TicTacToeApp().run()

