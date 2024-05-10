
import random

def choose_word():
    words = ["apple", "banana", "orange", "grape","kiwi"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_hangman(attempts):
    stages = [  
        '''
           --------
           |      |
           |      
           |      
           |     
           |
        ''',
        '''
           --------
           |      |
           |      O
           |      
           |     
           |
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |     
           |
        ''',
        '''
           --------
           |      |
           |      O
           |     /|
           |      
           |
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      
           |
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        '''
    ]
    return stages[attempts]

def hangman():
    max_attempts = 6
    guessed_letters = []
    word = choose_word()
    attempts = 0
    
    print("Welcome to Hangman!")
    print("Here's a hint: The word is a fruit.")
    print("Try to guess the word.")
    print(display_word(word, guessed_letters))

    while True:
        print("\nGuessed letters:", ", ".join(guessed_letters))
        print("Attempts left:", max_attempts - attempts)
        print(display_hangman(attempts))
        guess = input("Enter a letter (or 'quit' to end the game): ").lower()

        if guess == 'quit':
            print("Thanks for playing! The word was:", word)
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts += 1
            print("Incorrect!")

        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word!")
            break
        elif attempts == max_attempts:
            print("You ran out of attempts. The word was:", word)
            break

hangman()
