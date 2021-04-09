import random

class Hangman:

    def __init__(self):
        self.word = ""
        self.dashed_word = ""
        self.word_list = []
        self.choice = ""
        self.guessed_letters = []
        self.guesses = 8
        self.wins = 0
        self.losses = 0
        self.game_over = False

    def initialize_game(self):
        """Initializes a game of hangman"""
        self.get_word_list()
        self.get_word()
        self.word_to_dash()
        # self.how_many_guesses()

    def reset(self):
        self.word = ""
        self.dashed_word = ""
        self.word_list = []
        self.choice = ""
        self.guessed_letters = []
        self.guesses = 8
        self.game_over = False

    def get_word_list(self):
        """Gets all of the words from the word bank and appends them to a list"""
        with open("wordbank.txt") as file:
            for word in file:
                word = word.strip()
                self.word_list.append(word)

    def get_word(self):
        """Gets a random word from the word bank"""
        self.word += random.choice(self.word_list)

    def word_to_dash(self):
        """Makes a dashed string with equivalent length to the word"""
        self.dashed_word += "-" * len(self.word)

    # def how_many_guesses(self):
    #     self.guesses = int(input("How many guesses would you like? "))

    def print_guessed_letters(self):
        print(f"\nYou have already guessed: {', '.join(str(letter) for letter in self.guessed_letters)}")
        print(self.display_hangman())

    def get_choice(self):
        choice = input("Input a letter you think is in the word: ")
        self.choice = choice.lower()
        print()

    def check_choice(self):
        """Checks if the guessed letter is in the word"""
        if self.choice in self.word:
            return True
        else:
            return False

    def add_to_guessed(self):
        self.guessed_letters.append(self.choice)

    def update_dashed(self):
        """If the guessed letter is in the word, remove dashes in appropriate places"""
        index_list = []
        for index, letter in enumerate(self.word):
            if letter == self.choice:
                index_list.append(index)
        temp = list(self.dashed_word)
        for index in index_list:
            temp[index] = self.choice
        self.dashed_word = "".join(temp)

    def check_win(self):
        """If there are any dashes in the word then it has not been guessed yet"""
        if "-" in self.dashed_word:
            return False
        else:
            return True

    def add_word(self):
        """Add a new word to word bank, only for winners"""
        print("Winners get the chance to add a new word to the word bank\n")
        new = input("Would you like to add a new word? y/n ")
        if new == "y":
            new_word = input("Please enter the word: ")
            self.add_word_to_file(new_word)
            print(f"The word {new_word} has been added to the word bank")

    def add_word_to_file(self, word):
        """Winners get to add a new word to the data bank"""
        file = open("wordbank.txt", "a")
        file.write("\n")
        file.write(word)
        file.close()

    def play_again(self):
        """Asks the user if he wants to play again"""
        play = input("Would you like to play again? y/n ")
        if play.lower() == "y":
            return True
        elif play.lower() == "n":
            return False
        else:
            print("\nI'll take that as a no")

    def display_hangman(self):
        states = [
            """
            ----------
            |        |
            |        O
            |       \|/
            |        |
            |       / \\
            |
            -
            """,
            """
            ----------
            |        |
            |        O
            |       \|/
            |        |
            |         \\
            |
            -
            """,
            """
            ----------
            |        |
            |        O
            |       \|/
            |        |
            |
            |
            -
            """,    
            """
            ----------
            |        |
            |        O
            |        |/
            |        |
            |
            |
            -
            """,      
            """
            ----------
            |        |
            |        O
            |        |
            |        |
            |
            |
            -
            """,
            """
            ----------
            |        |
            |        O
            |        |
            |        
            |
            |
            -
            """,
            """
            ----------
            |        |
            |        O
            |
            |
            |
            |
            -
            """,
            """
            ----------
            |        |
            |
            |
            |
            |
            |
            -
            """,
            """
            ----------
            |
            |
            |
            |
            |
            |
            -
            """
        ]
        return states[self.guesses]

    def __len__(self):
        """Returns the length of the word"""
        return len(self.word)

    def __str__(self):
        """Returns the word"""
        return self.word

def print_welcome():
    """Welcome message"""
    print()
    print("Welcome to hangman!")
    print()

def main():
    """The Hangman game"""

    # Make sure guess is a single letter, not multiple or a non string
    # Make prettier

    print_welcome()

    game = Hangman()

    while not game.game_over:    
        # Initializing the game, a random word is chosen and a dashed version is made
        game.initialize_game()

        while game.guesses > 0:
            print("\nYour word to guess is:")
            print("\n", game.dashed_word, "\n") 
            # If user guesses the entire word correctly, instant win
            game.get_choice()
            if game.choice == game.word:
                game.game_over = True
                break
            # User guesses same letter he has already guessed
            if game.choice in game.guessed_letters:
                print(f"\nYou have already guessed {game.choice}, please try another letter")
            # User guesses new letter that he has not guessed before
            # If the letter is in the word, the dashes are removed for that letter
            elif game.check_choice():
                game.update_dashed()
                # Check if this guess has revealed the entire word
                if game.check_win():
                    game.game_over = True
                    break
                print(f"\nGood job! {game.choice} is in the word")
            else:
                print(f"\nSorry, {game.choice} is not in the word")
                # The user only loses a guess if he guesses a wrong letter (does not lose additional guesses for re-guessing the same letters)
                game.guesses -= 1
            if game.guesses != 1:
                print(f"\nYou have {game.guesses} guesses left")
            else:
                print(f"\nYou have {game.guesses} guess left")
            game.add_to_guessed()
            game.print_guessed_letters()

        if game.game_over:
            game.wins += 1
            print(f"\nCongratulations! You guessed the word {game.word}!\n")
            # Winners get the chance to add a new word to the word bank
            game.add_word()
        else:
            game.losses += 1
            print(f"\n-- Game over -- \n\nYour word was {game.word}")
        # User gets to see his game history - wins and losses
        print(f"\nYou have won {game.wins} game(s), and lost {game.losses} game(s)")
        print()
        game.reset()
        if not game.play_again():
            print("\nThanks for playing!\n")
            break


if __name__ == "__main__":
    main()