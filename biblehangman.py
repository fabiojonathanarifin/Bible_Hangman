import random 
from words import word_bank

# getting the word from word bank
def get_word():
    word = random.choice(word_bank)
    return word.upper()

#the game
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Bible Character Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("Total words: ", len(word))
    print("Tries left: ", tries)
    print("\n")

    #condition for the game
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        #guess per letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("good", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif guess == "":
            print("You didn't put anything.")
        #guess the whole word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "Wrong!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print ("Wrong!")
            tries -= 1
        print(display_hangman(tries))
        print(word_completion)
        count = 0
        for i in word_completion:
            if i == "_":
                count += 1
                
        print("Words left: ", count)
        print ("Tries left: ", tries)
        print("\n")
    if guessed and tries == 6 :
        print("Perfect! You smells like a Prophet.")
    elif guessed and tries < 6:
        print("You win! You smells like a Theologian.")
    else:
        print("Hehe, you lose. the word was " + word + "\nRead ur Bible\n")


def display_hangman(tries):
    stages = [
            # final state: head, torso, both arms, and both legs
                """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    -
                """,
            # head, torso, both arms, and one leg
                """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / 
                    -
                """,
            # head, torso, and both arms
                """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      
                    -
                """,
            # head, torso, and one arm
                """
                    --------
                    |       |
                    |       O
                    |      \\|
                    |       |
                    |      
                    -
                """,
            # head and torso
                """
                    --------
                    |       |
                    |       O
                    |       |
                    |       |
                    |      
                    -
                """,
            # head
                """
                    --------
                    |       |
                    |       O
                    |       
                    |       
                    |      
                    -
                """,
            # empty state
                """
                    --------
                    |       |
                    |       
                    |       
                    |       
                    |      
                    -
                """,
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()