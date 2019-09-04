# A python porgram for a hangman game between two players.

''' Player 1 is made to enter the secret word manually without Player 2 knowing it.
Player 1 also gives a clue for reference.'''
secret_word = input("Enter the secret word Player 1 : \n").upper()
clue = input("Give a clue for the word :\n")
# Every player only gets 7 chances.
count = 7
guess_word = "*"*len(secret_word)

# A function to update the dashes with the exisiting characters, giving the player a good playing field.
def update(word, letter ,star):
    updated_word = ""
    for i in range(len(word)):
        if letter == word[i]:
            updated_word += letter
        else:
            updated_word += star[i]
    return updated_word.upper()

# A while condition to loop within the 7 turns and to also check if the word has been reached.
while count > 0 and not guess_word == secret_word:
    print("You have %d chances left"%(count))
    print(guess_word)
    guess_char=input("Enter your character : ").upper()
    # An if condition so that the player doesn't exceed one character at a time rule.
    if len(guess_char)>1:
        print("Enter only a single character.")
    # The main condition where all the magic happens.
    elif guess_char in secret_word:
        print("The character is in the word.")
        guess_word = update(secret_word,guess_char,guess_word)
    else:
        print("The character is not in the word.")
        count -= 1

# To check if the player won or lost the game.
if count == 0:
    print("\nYou have lost the game. Better luck next time.\nThe word was : " + secret_word)

elif count > 0:
    print("\nCongrats. You won the game.\nThe word is " + secret_word)
