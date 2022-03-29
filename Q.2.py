print ("Welcome to the game, Hangman!")
print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
print ("")

letters_guessed = []
while (True):
    available_letters = get_available_letters(letters_guessed)
    print ("Available letters: " + available_letters)
guess = input("Please guess a letter: ")
letter = guess.lower()
if letter in secret_word:
    letters_guessed.append(letter)
    print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
    print ("")
if is_word_guessed(secret_word, letters_guessed) == True:
    print (" * * Congratulations, you won! * * ")
    print ("")

else:
    print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word,letters_guessed))
    letters_guessed.append(letter)
    print ("")