# September IDP - Brick Breaker

My very first IDP involved making a version of Brick Breaker. The goal of this game is to break all of the on screen bricks without letting the ball fall off. I initially programmed this in Python because I had prior knowledge of this language before this class and wanted to demonstrate what I already knew. 

The six things were used extensively throughout this project. Arrays were required to keep track of each brick, and conditionals were used for collision detection.

This project requires a recent version of Python 3 with the TKInter library installed if necessary. 

## Game controls - Arrow Keys

# Original Reflection: September 2021
# September IDP: Brick Breaker
For my first IDP I wanted to make a relatively simple game in Python. I chose Python as I wanted to start off with a language that I was semi-familiar with already. 

Disclaimer: I did not do this project inside Replit, instead opting to locally use VSCode and Python 3. If there are issues, copy the code into a .py file and run it natively if you can. If not, see me. 

**INSTRUCTIONS TO PLAY:**
Use arrow keys to control the paddle (left and right)
Your objective is to get the ball to break all of the bricks without it falling off of the screen

Experience while programming:
This was relatively straightforward. Some things that I had to take account into were:
	
  - Physics of the ball
	
  - Collisions with the window border, 
  paddle, 
	
  - Get the paddle to respond to my keystrokes
	
  - Drawing and assigning values to the bricks to be able to detect collision and its appearance/location on the map
	
  - Score system
	
  - Creation of game canvas (used a feature in Python called Tkinter)

  - Calling a game over

Issues I ran into that I had to fix:
	
  - Window size was too big for the default Replit layout. Resize the different columns until you find one that works. 
- Occasionally, the game would lag due to the high amount of variables. Especially noticeable when it's being ran through the cloud. Seems fine locally.

What I've learned:
How to create simple games in Python and the different aspects of creating one
