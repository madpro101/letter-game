import os 
import sys 
import random
# make a list of words
words = [
    "sadza",
    "beef", 
    "coconut",
    "timber", 
    "capricon", 
    "artistic", 
    "samsung", 
    "nokia", 
    "blackberry", 
    "gtel", 
    "sony", 
    "amazon"
]
# function to clear the screen
def clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')
        
# tidng up my code 
# draw function 
def draw(good_guesses, bad_guesses, secret_word):
    # First thing we do is to clear the screen
    clear()
    
    print('')
    print("Strikes: {}/7".format(len(bad_guesses)))

    for letter in bad_guesses:
        print(letter, end = ' ')
    print("\n\n")
        
    # draw guessed letters, spaces and strikes
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end="")
        else:
            print("_ ", end="")
            # end = "" lets print, print things multiple times in the same line. 
            
              
# function to get user input of the guess  
def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("guess a letter ").lower()
        if len(guess) != 1 :
            print("You can only guess one letter at a time")
                
        elif guess in bad_guesses or guess in good_guesses:
                print("Oops you have already guessed that letter")
            
        elif not guess.isalpha(): 
                print("You can only guess letters ")
                # isalpha checks to see if all characters in guess are letters
        else: 
            return guess

def play(done):
    clear()
    secret_word = random.choice(words)
    good_guesses = []
    bad_guesses = []
    
    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)
        
        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False 
            if found: 
                print("You win")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("Im sorry my guy you lost")
                print("The secret word was {}".format(secret_word))
                done = True
                
        if done:
            play_again = input("Play again? Y/n").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                syt.exit()
def welcome():
    start = input("Press enter to start or Q to quit").lower()
    if start =='q':
        print("Bye thanks for playing my game")      
        
print("Welcome to sketchy letter an award winning letter game ")
done = False

while True:
    clear()
    welcome()
    play(done)