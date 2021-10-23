import random

# Functions of the game

def mistakes(counter):
    """ prints out the hangman according to the number of mistakes made
        up to a specific point in the game """
    if counter == 1:
        print('  ------\n |     |\n |\n |\n |\n |\n_|_')
    elif counter == 2:
        print('  ------\n |     |\n |     o\n |\n |\n |\n_|_')
    elif counter == 3:
        print('  ------\n |     |\n |     o\n |     |\n |     |\n |\n_|_')
    elif counter == 4:
        print('  ------\n |     |\n |     o\n |    /|\\\n |     |\n |\n_|_')
    elif counter == 5:
        print('  ------\n |     |\n |     o\n |    /|\\\n |     |\n |    / \\\n_|_')
    else:
        print('Counter should be between one and five!')

def print_progress(list):
    """ prints out the word with the guessed letters up to now """
    for i in range(len(list)):
        print(list[i], end = ' ')

def insert_letters(list ,indexes, letter):
    """ inserts the letter/s in the correct indices of the list
        that contains the rightly guessed letters """
    for i in indexes:
        list[i] = letter

def find_letters_in_word(word, letter):
    """ finds the indices at which a letter appears in a word,
        returns a list with those indices """
    t = list()
    index = -5
    for i in range(len(word)):
        if word.find(letter, i) != index and word.find(letter, i) != -1:
            index = word.find(letter, i)
            t.append(index)
    if bool(t) == False:
        return False
    return t

def completed(list1, list2):
    """ checks if the guessed word is the same as the word that should be guessed """
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

def prepare(list_of_words):
    """ prepares the variables to start the game again """
    global word
    word = random.choice(list_of_words)
    print('\n\nGuess the word with ', len(word), ' letters!')
    global word_list
    word_list = list(word)
    global guessed_letters
    guessed_letters = list(len(word) * '_')
    print_progress(guessed_letters)
    global count_mistakes
    count_mistakes = 0
    global all_guesses
    all_guesses = list()
    



# The start of the game     

print("Welcome to the Hangman Game!")
print("Type 'exit' to exit the game!")

fin = open('random_words.txt')
words = fin.read().split('\n')
word = random.choice(words) #the word the user should guess
print('\n\nGuess the word with ', len(word), ' letters!')
word_list = list(word)
guessed_letters = list(len(word) * '_')
print_progress(guessed_letters)
count_mistakes = 0
all_guesses = list()

while True:
    guess = input('\n\nGuess a letter: ').lower()
    if not guess.isalpha():
        print('The guess should be a letter! Guess again!')
        continue
    elif guess in all_guesses:
        print('You already guessed this letter.')
        continue
    elif guess == 'exit':
        break
    else:  
        indices = find_letters_in_word(word, guess)
        all_guesses.append(guess)
        if indices == False:    #if the letter wasn't found in the word
            count_mistakes += 1
            mistakes(count_mistakes)
            if count_mistakes >= 5:
                print('\nYou failed.')
                guess = input('Press Enter to play again or type "exit" to exit the program: ')
                if guess == 'exit':
                    break
                if guess == '':
                    prepare(words)
                    
        else:   # if the letter was found in the word
            insert_letters(guessed_letters ,indices, guess)
            if completed(guessed_letters, word_list) == True:
                print('You won!')
                print_progress(guessed_letters)
                guess = input('\n\nPress Enter to play again or type "exit" to exit the program: ')
                if guess == 'exit':
                    break
                if guess == '':
                    prepare(words)

            print_progress(guessed_letters)
            
    
        









