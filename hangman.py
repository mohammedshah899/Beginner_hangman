import random
from words import words

# Selects at random from the words list
hidden_word = random.choice(words)
print(f"Hidden Word: {hidden_word} ")
lives = 5
final_word = ""
used_words = ""

# Creates a string of '-', equal in length to the hidden_word
def corrected_guess(word):
    corrected_word = ""
    for x in range(0, len(word)):
        corrected_word = corrected_word + '-'
    
    return corrected_word


# Converts the str into a list
correct_guess = list(corrected_guess(hidden_word))

while lives > 0:
    user_input = input("\nGuess the letter: ")

    # Container for all the used alphabets
    used_words = used_words + " " + user_input

    # Check if the user_input is present in the Hidden_word.
    # Iterate from the first element to the last
    # Check to see if the user_input is present at a particular position in the Hidden_word
    # The '-' in correct_guess will be replaced by the right alphabet.
    if user_input in hidden_word:
        for x in range(0,len(hidden_word)):
            if hidden_word[x] == user_input:
                correct_guess[x] = hidden_word[x] 
        #  Converts the list into a string
        final_word = ''.join(correct_guess)    
        print(f"You have {lives} lives left and you have used these letters: {used_words.upper()}")
        print("Current word: " + final_word)
        # Checks to see if the final_word contains any '-', if it doesn't, breaks out of the loop
        if not(final_word.__contains__('-')):
            break
        
    else:
        print(f"Your letter, {user_input} is not in the word")
        lives -= 1
        print(f"You have {lives} lives left and you have used these letters: {used_words.upper()}")
        print(f"Current word: {final_word}\n")
            
# Compare the final_word and hidden_word
if final_word == hidden_word:
    print("\nCongratulations!!\n")
elif final_word != hidden_word and lives == 0:
    print("\nTry again!\n")



                
            




            
        
            
    
        


