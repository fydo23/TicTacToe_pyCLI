#!/usr/bin/env python
from cli.app import CommandLineApp
from game.objects import Engine

class TicTacToeApp(CommandLineApp):

	name = "TicTacToe"

	def setup(self):
		super(TicTacToeApp,self).setup()
		self.add_param("-n", "--no-player", help="Plays the game as two computers.", 
			default=0, action="store_true")
		
	# This is called after run() completes setup()
	def main(self):
		Engine(no_player=self.params.no_player).play()


if __name__ == "__main__":
	TicTacToeApp().run()

