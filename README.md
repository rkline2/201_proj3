# Scoring Go

## 1. Task
You will be programming up a simplified scoring system for the board game Go. Go is an abstract strategy
game where two players compete to surround as much of a board with their colored pieces as possible.
At the end of the game, each players score is the sum of how many pieces they still have on the board
with how much empty space their pieces surround.

Your program will need to:
  * Read in and store a completed Go game board from a file
  * Mark all of the empty spaces on the board with the symbol of the player's piece that controls them
  * Sum the total scores and display them to the user.

## 2. Details
The program starts by asking the user for the filename that contains the go board, and reads in the file.
The program will paint the board with player ownership and then tally the final score.

### Reading in and Creating the Board
For this assignment, you will be reading in a file representing the completed Go game.<br>
* The board may be any size
* The board will always be rectangular
* The board will consist of:
 a. plus sign (+) for an empty space
 b. the letter O, for a white piece
 c. the letter X, for a black piece
 
### Displaying the Board
The board should be displayed to the user once it is loaded in, then again
after it has been painted.<br>
 * The board's initial display should be how it was stored in the file
 * We recommend that you use a 2d list to store the contents of the file

## 3. Objective
Project 3 is designed to give you practice with two-dimensional lists, creating and calling functions, and recursion.
You’ll need to use practically everything you’ve learned so far, and will need to do some serious thinking about how all 
of the pieces you need to create should fit together.  
