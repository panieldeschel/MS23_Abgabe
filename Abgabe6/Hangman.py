# Play Hangman inside the console

import os
import WordGuesser
import keyboard

wordGuesser = WordGuesser.WordGueser()      # Hier habe ich einen Tippfehler eingebaut! WordGueser

# loop the game until the word is completed
while Tru:                                  # Hier habe ich noch einen Tippfehler eingebaut! Tru
    # reset canvas and write UI
    os.system('cls')                            # only works on Windows  
    print('''
        Hangman, ohne jemanden zu Hängen - Viel Spaß!
        Zum Raten bitte einen Buchstaben eintippen:

        %s
    ''' % wordGuesser.getProgressString())

    # if word is incomplete wait for the next guess
    if not wordGuesser.isFinished():
        keyPressed = keyboard.read_key()        # stops code until key is pressed
        wordGuesser.letterGuessed(keyPressed)
    # else end the game
    else:
        break

print("Du hast es erraten, nicht schlecht!")