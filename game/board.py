ALL_WINNERS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

class Board:

	_board = ['1','2','3',
			 '4','5','6',
			 '7','8','9']

	def __init__(self,board=None):
		if not board: return
		self._board = list(board._board)

	def __setitem__(self,index,item):
		self._board[index] = item
		
	def __getitem__(self,index):
		return self._board[index]

	def get_open_tiles(self):
		return [int(x)-1 for x in self._board if x in ['1','2','3','4','5','6','7','8','9']]

	def test_winners(self):
		for triplet in ALL_WINNERS:
			if self._board[triplet[0]] == self._board[triplet[1]] == self._board[triplet[2]]:
				return True
		return False

	def get_best_move(self, player):
		#best_move = (pos, pos_wins, win)
		fill_count = 0
		best_move = (None, 0, False)

		for x in self.get_open_tiles():
			testBoard = Board(self)
			testBoard[x] = player
			if testBoard.test_winners():
				best_move = (x, 1, True)
				return best_move

		for x in self.get_open_tiles():
			info = self.get_position_info(x, player)		
			wins_at_x = info[0]
			filled_spaces = info[1]
			if wins_at_x > best_move[1] or not best_move[0]:
				fill_count = filled_spaces
				best_move = (x,wins_at_x, False)
			elif wins_at_x == best_move[1] and filled_spaces > fill_count:
				fill_count = filled_spaces
				best_move = (x, wins_at_x, False)
		return best_move

	def get_position_info(self, position, player):
		"""
		This function returns a tuple (x, y) where x is the number of unblocked winning combinations 
		that are still available for the current player, and y is the number of tiles
		filled by the player in those winning combinations.
		"""
		good_values = ['1','2','3','4','5','6','7','8','9', player]
		winners_for_pos = [triplet for triplet in ALL_WINNERS if position in triplet]
		unblocked_winning_combos = 0
		tiles_filled_by_player = 0
		for triplet in winners_for_pos:
			good_winner = True
			for pos in triplet:
				# print "position:"+str(position)+" player:"+player +" triplet"+str(triplet)+ " self._board[triple["+str(pos)+"]]:"+str(self._board[pos])
				if self._board[pos] not in good_values:
					good_winner = False
			if good_winner:
				unblocked_winning_combos+=1
				for pos in triplet:
					if self._board[pos] == player:
						tiles_filled_by_player+=1
		return (unblocked_winning_combos, tiles_filled_by_player)

	def print_board(self):
		board = self._board
		print " "+ board[0] + " | " + board[1] + " | " + board[2] 
		print "---+---+---"
		print " "+ board[3] + " | " + board[4] + " | " + board[5]
		print "---+---+---"
		print " "+ board[6] + " | " + board[7] + " | " + board[8] 

