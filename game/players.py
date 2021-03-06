from board import Board

PLAYERS = ["X", "O"]

class Player:

	_player = None

	def get_opponent_player(self):
		if not self._player:
			raise Exception("PLayer's _player is not defined.")
		if self._player == "X":
			return "O"
		return "X"


class User(Player):

	def __init__(self):
		input = raw_input
		player = None
		while player not in PLAYERS:
			player = input("Will you play as X's (go first) or O's: ").upper()
			if player not in PLAYERS:
				print "invalid player."
		self._player = player
		print "You are playing as player "+ self._player + "."

	def do_move(self, board):
		"""
		Prompt yser and retun the requested position.
		"""
		input = raw_input
		move = None
		# print "moveCounter:"+str(self.move_counter)
		while not move:
			try: 
				input_move = int(input("Where would you like to place your '" + self._player + "'? "))
				if 0 < input_move <= 9 and board[input_move-1] not in PLAYERS:
					move = input_move
				else:
					raise ValueError()
			except ValueError:
				print "invalid input"
		board[move-1] = self._player
		return


class Computer(Player):

	def __init__(self, player):
		self._player = player

	def do_move(self,board):
		"""
		Currently this implemenation simply takes the firts available spot.
		"""

		#stats = (pos, pos_wins, is_win)
		print "computer is thinking..."

		tempBoard = Board(board)

		# get my best move.
		my_best_move = tempBoard.get_best_move(self._player)
		if my_best_move[2]:
			print "I CAN WIN!!!"
			board[my_best_move[0]] = self._player
			return

		# mock my move.
		tempBoard[my_best_move[0]] = self._player 

		# get opponents best move
		op_best_move = tempBoard.get_best_move(self.get_opponent_player())
		if op_best_move[2]:
			print "Blocked you."
			board[op_best_move[0]] = self._player
			return

		# would my move, put my opponent at an advantage?
		if my_best_move[1] < op_best_move[1]:
			for x in board.get_open_tiles():

				# find a move that makes it better for me.
				testBoard = Board(board)
				testBoard[x] = self._player

				# get opponenents new best move
				new_op_move = testBoard.get_best_move(self.get_opponent_player())
				if not new_op_move[0]: continue
				
				# check if I can win afterwards.
				testBoard[new_op_move[0]] = self.get_opponent_player()
				my_new_move = testBoard.get_best_move(self._player)
				if not my_new_move[0]: continue

				if my_new_move[2] or (my_new_move[1] > new_op_move[1] and not new_op_move[2]):
					board[x] = self._player
					return
		
		board[my_best_move[0]] = self._player
		return



