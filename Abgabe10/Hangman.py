# Play Hangman inside the console

import os
import WordGuesser
import keyboard

def gameLoop(progress, target):
    os.system('cls')                            # only works on Windows  
    print('''
        Hangman, ohne jemanden zu Hängen - Viel Spaß!
        Zum Raten bitte einen Buchstaben eintippen:

        %s
    ''' % progress)

    if progress == target:
        print("Du hast es erraten, nicht schlecht!")
    else:
        # stops code until key is pressed
        new_progress: Final = WordGuesser.guessingLetter(keyboard.read_key(), progress, target)
        gameLoop(new_progress, target)

# loop the game until the word is completed
wordToGuess = WordGuesser.pickWord('words.json') 
gameLoop(WordGuesser.hideWord(wordToGuess), wordToGuess)