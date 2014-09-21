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
		return board.set_position(move-1, self._player)


class Computer(Player):

	def __init__(self, player):
		self._player = player

	def do_move(self,board):
		"""
		Currently this implemenation simply takes the firts available spot.
		"""
		print "computer is thinking..."
		#can I win?
		for x in range(1,10):
			if board[x-1] not in PLAYERS:
				_board = list(board)
				_board[x-1] = self._player
				if ((_board[0] == _board[1] == _board[2]) or 
					(_board[3] == _board[4] == _board[5]) or
					(_board[6] == _board[7] == _board[8]) or 
					(_board[0] == _board[3] == _board[6]) or
					(_board[1] == _board[4] == _board[7]) or
					(_board[2] == _board[5] == _board[8]) or
					(_board[0] == _board[4] == _board[8]) or
					(_board[2] == _board[4] == _board[6])):
						board.set_position(x-1,self._player)
						return

		#can I block?
		for x in range(1,10):
			if board[x-1] not in PLAYERS:
				_board = list(board)
				_board[x-1] = self.get_opponent_player()
				if ((_board[0] == _board[1] == _board[2]) or 
					(_board[3] == _board[4] == _board[5]) or
					(_board[6] == _board[7] == _board[8]) or 
					(_board[0] == _board[3] == _board[6]) or
					(_board[1] == _board[4] == _board[7]) or
					(_board[2] == _board[5] == _board[8]) or
					(_board[0] == _board[4] == _board[8]) or
					(_board[2] == _board[4] == _board[6])):
						board.set_position(x-1,self._player)
						return
		
		#can I take the center?
		if board[4] not in PLAYERS:
			board.set_position(4,self._player)
			return
		
		#take square with most possible wins?
		pos_wins = (None, 0)
		for x in range(1,10):
			if board[x-1] not in PLAYERS:
				wins_at_x = board.get_possible_win_count(x, self._player)
				if wins_at_x > pos_wins[1]:
					pos_wins = (x,wins_at_x)
		if pos_wins[0]:
			board.set_position(pos_wins[0]-1,self._player)
			return

		for x in range(1,10):
			if board[x-1] not in PLAYERS:
				board.set_position(x-1,self._player)
				return

