TicTacToe_pyCLI
===============

This is a simple CLI based app that intelligently plays Tic-Tac-Toe with the user, or vs itself. It uses a min-max scoring system to guage it's next move and deviates it's strategy if it realizes it's loosing after a single-move lookahead tactic. 


Most basic installations of python include `pip`, which is to be used for installing this project's dependencies. To install the packages, run `$ pip install -r requirements.txt` from the project's source folder. It is suggested that you also use [virtualenv](http://virtualenv.readthedocs.org/en/latest/) in conjunction with this project so as to not clutter your machine with this project's dependent packages.


HOW TO PLAY
===========

To run the game, change into the folder containing this file and run `$ Python playTTT.py`

This game also runs as computer vs. computer simulation if you run `$ Python playTTT.py -n`, but be warned, it's always the same!

AUTHORS
============
Fyodor Wolf  
Chris Farrell  
William Wilson
