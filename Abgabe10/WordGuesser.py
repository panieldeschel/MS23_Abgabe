import JSONUtils      
import random 
import re       

def pickWord(path):
    available_words: Final = JSONUtils.readList(path)
    return random.choice(available_words)

def hideWord(word):
    return re.sub(r'\w', '_', word)

def guessingLetter(letter, hidden_word, full_word):
    new_hidden_word: Final = [
        full_word[num]
        if character.lower() == letter
        else hidden_word[num]
        for num, character in enumerate(full_word)
    ]

    return ''.join(new_hidden_word)