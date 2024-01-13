import random

def Hangman():
    guess = input("Pick a letter!")
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    print(chosen_word)

    letter_listed = list(chosen_word)
    num_guess = 0
    tries = 5
    words_length = len(letter_listed)
    display = []
    display_counter = 0
    for num in chosen_word:
        display_counter += 1
        display = list(display_counter * "_")
    
    print(display)
  #  display = list(display)
    while tries > 0 and words_length > 0:
        if guess in letter_listed:
            words_length -= 1        
                    
        for index, letter in enumerate(letter_listed):
            if letter == guess:
                display[index] = guess
                print("Right")
                num_guess += 1
            else:
                print("Wrong")
                tries -= 1 
                print(f"Nope, he is one stop closer to hanging!")
                print(f"You have {tries} remaining!")
                guess = input(" Next guess?")
    print(display)
    
    if "_" not in display:
        print("You did it!")
        print("Would you like to play again?")
     #   confirm = input("Next round!")
      #  if confirm == "yes":
            

print("Welcome to Hangman! Lets play?!")
Hangman()
        

