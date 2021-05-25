import string
from words import choose_word
from images import IMAGES
'''
Instructions:
* Function and Variable Name: snake_case -> is_prime
* Constant Variable: upper case -> PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guessed by the user
    letters_guessed: list which holds all the words guessed by the user
    returns: 
      return True (if user guesses the word correctly)
      return False (wrong selection)
    '''
    count=0
    for i in letters_guessed:
      if(i in secret_word):
        count+=1
    if(count == len(secret_word)):
      return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guessed by the user
    letters_guessed: list which holds all the words guessed by the user
    returns: 
      return string which contains all the correctly guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list which holds all the words guessed by the user
    returns: 
      a string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> 'bcdfghijklmnopqrstuvwxyz'
    '''
    global letters_left 
    for i in letters_guessed:
      if(i in letters_left):
        letters_left = letters_left.replace(i,"#")
    return letters_left

def ifValid(check_letter):
  if(check_letter.isalpha() == False or len(check_letter)>1):
        print("Please try again\n")
        return False
  return True

def hangman(secret_word):
    '''
    secret_word type -> (string) : to be guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character input give feedback to the user
      * right or wrong

    * Display the partial word as guessed by the user and use underscore in place of word unguessed yet    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives = 8;
    wrong_input_count =0

    while(remaining_lives > 0):
      available_letters = get_available_letters(letters_guessed)
      print("Available letters: {} ".format(available_letters))
      guess = input("Please guess a letter: ")
      letter = guess.lower()
      if(ifValid(letter) == False):
        continue      

      if letter in secret_word:
          letters_guessed.append(letter)
          print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
          if is_word_guessed(secret_word, letters_guessed) == True:
              print("\n * * Congratulations, you won! * * ", end='\n\n')
              exit()
      else:
          remaining_lives-=1
          if(remaining_lives == 0):
            print(IMAGES[wrong_input_count], "\n")
            print("Oops! That letter is not in my word: {} \nRemaining Lives: {}".format(get_guessed_word(secret_word, letters_guessed), remaining_lives))
            print(f"The word was: '{secret_word}'")
            exit();  
          print("Oops! That letter is not in my word: {} \nRemaining Lives: {}".format(get_guessed_word(secret_word, letters_guessed), remaining_lives))
          letters_guessed.append(letter)
          print(IMAGES[wrong_input_count], "\n")
          wrong_input_count+=1
    



# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
letters_left = " ".join(string.ascii_lowercase)
hangman(secret_word)
