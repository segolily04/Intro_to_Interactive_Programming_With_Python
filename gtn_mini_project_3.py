# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

max_number = 0
secret_number = 0 
guesses = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global max_number, secret_number, guesses
    guesses = 0
    secret_number = 0
    max_number = 0
    print "Let's play! Pick a number range."

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_number, secret_number, guesses
    max_number = 100
    guesses = 7
    secret_number = random.randrange(1, 100, 1) 
    print "You have "+str(guesses) +" guesses. Pick a number between 0 and 100."

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_number, secret_number, guesses
    guesses = 10
    max_number = 1000
    secret_number = random.randrange(0, 1000, 1)
    print "You have "+str(guesses) +" guesses. Pick a number between 0 and 1000."
    
def input_guess(guess):
    global secret_number, guesses
    
    print "You picked " + guess
    
	player_guess = int(guess) 
	
    # main game logic goes here	
    if (secret_number < player_guess):
        print "Lower"
        print ""
    elif (secret_number > player_guess):
        print "Higher"
        print ""
    elif (secret_number == player_guess):
        print "Correct! You won!" 
        new_game()
        print ""
    else: 
        print ""
    
    #check if they have any more guesses left
    guesses = guesses - 1
    
    if (guesses == 0):
        print "Sorry, you lost. The correct number was " + str(secret_number) +"."
        new_game()
    else: 
        print "You have "+str(guesses) +" guesses left. Pick a number between 0 and 100."

# create frame
frame = simplegui.create_frame("Guess the Number Game", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Set range max to 100", range100)
frame.add_button("Set range max to 1000", range1000)
frame.add_input("Enter your guess.", input_guess, 200)  
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
