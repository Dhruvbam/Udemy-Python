import random

# List of words to choose from
word_list = ['python', 'java', 'kotlin', 'javascript', 'swift', 'html', 'css']

# Function to choose a random word from the list
def get_word():
    word = random.choice(word_list)
    return word.upper()

# Function to play the game
def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Let\'s play Hangman!')
    print(display_hangman(tries))
    print(word_completion)
    print('\n')

    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter', guess)
                print('\n')
            elif guess not in word:
                print(guess, 'is not in the word.')
                print('\n')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Good job,', guess, 'is in the word!')
                print('\n')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed the word', guess)
                print('\n')
            elif guess != word:
                print(guess, 'is not the word.')
                print('\n')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess.')
            print('\n')
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print('Congratulations, you guessed the word! You win!')
    else:
        print('Sorry, you ran out of tries. The word was ' + word + '. Maybe next time!')

# Function to display the hangman based on the number of tries
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, and one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, and both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso, and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial
    ]