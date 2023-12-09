import JSONUtils      
import random 
import re       

class WordGuesser:
    def __init__(self):
        # get a word and hide it
        self.word = self.initWord()                           # word to guess
        self.progress = self.initProgress(self.word)    # progress of guessing

    def initWord(self):
        # available words are listed in "./words.json"
        available_words = JSONUtils.readList('words.json')
        # pick a random available word
        return random.choice(available_words)

    def initProgress(self, word):
        # replace every letter with _ using RegExs
        hidden_word = re.sub(r'\w', '_', word)
        return hidden_word



    # Get Properties
    def getProgressString(self):
        return self.progress
 
    def isFinished(self):
        if self.progress == self.word:
            return True
        else:
            return False



    # Write Letter
    def letterGuessed(self, letter):
        # revert every _ that hides the guessed letter
        for num, character in enumerate(self.word):
            if character.lower() == letter:
                # replace the _ in the middle of the string that hides the correctly guessed letter
                # keep the old progress before and after that character
                self.progress = self.progress[:num] + self.word[num] + self.progress[num + 1:]


        