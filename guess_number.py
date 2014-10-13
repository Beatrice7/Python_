#"Guess the number" mini-project
import simplegui
import math
import random

secret_number = 100
scope = 100
count = 0

def new_game():
    global secret_number, count
    print "New game. Range is from 0 to %d" % scope
    secret_number = random.randrange(0, scope)
    count = int(math.ceil(math.log(scope, 2)))
    print "Number of remaining guesses is %d\n" % count
    
def range100():
    global scope
    scope = 100
    new_game()
   
def range1000():
    global scope
    scope = 1000
    new_game()
  
def input_guess(guess):
    guess = int(guess)
    global count
    count -= 1
    print "Guess was", guess
    print "Number of remaining guesses is", count
    if secret_number > guess:
        if count == 0:
            print "You ran out of guesses.  The number was %d\n" % secret_number
            new_game()
        else:
            print "Higher!\n"
    elif secret_number < guess:
        if count == 0:
            print "You ran out of guesses.  The number was %d\n" % secret_number
            new_game()
        else:
            print "Lower!\n"
    else:
        print "Correct!\n"
        new_game()
   
        
# create frame
frame = simplegui.create_frame('Guess The Number', 200, 200)
frame.add_button('Range [0, 100)', range100, 200)
frame.add_button('Range [0, 1000)', range1000, 200)
frame.add_input('Guess a number', input_guess, 100)

# call new_game 
new_game()


