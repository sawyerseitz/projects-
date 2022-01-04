import random

#IT4401 final project by: Sawyer Seitz
# the hangman printouts are from the following website: https://www.asciiart.eu/animals/mammals/hanging-

# this function is used to draw the hangman according to the number of tries left
def Hangman(guess,playing):
    print("\n")
    
#shows user the number of tries left
    print("You have ",guess," tries left")
#all of these will return an integer value, when the user loses the game and has zero guesses this function will return 0 and the game will end
    print("\n")
    #head of hangman
    if(guess == 5):
        print("*********************************************************")
        print("  _________")
        print(" |/     |")
        print(" |     (_)")
        print(" |  ")
        print(" |")
        print(" |")
        print(" | ")
        print("_|_")
        print("********************************************************")
        print("\n")
        return playing
#body of the hangman
    elif(guess == 4):
        print("*********************************************************")
        print("  _________")
        print(" |/     |")
        print(" |     (_)")
        print(" |      |")
        print(" |  ")
        print(" |")
        print(" |")
        print("_|_ ")
        print("********************************************************")
        print("\n")
        return playing
#left arm of the hangman
    elif(guess == 3):
        print("*********************************************************")
        print("  _________")
        print(" |/     |")
        print(" |     (_)")
        print(" |      |\\")
        print(" | ")
        print(" |")
        print(" |")
        print("_|_ ")
        print("********************************************************")
        print("\n")
        return playing
#right arm of the hangman
    elif(guess == 2):
        print("*********************************************************")
        print("  _________")
        print(" |/     |")
        print(" |     (_)")
        print(" |    / |\\")
        print(" |      ")
        print(" | ")
        print(" |")
        print("_|_ ")
        return playing
        #left leg of the hangman
        
    elif(guess == 1):
        print("*********************************************************")
        print("  _________")
        print(" |/     |")
        print(" |     (_)")
        print(" |    / |\\")
        print(" |     /")
        print(" |")
        print(" |")
        print("_|_ ")
        return playing
#this is the end of the hangman
    elif(guess == 0):
        print("*********************************************************")
        print("  _________")
        print(" |/     |")
        print(" |     (_)")
        print(" |    / |\\")
        print(" |     /\\")
        print(" |")
        print(" |")
        print("_|_ ")
        return playing - 1
    # function with list of random words for the user to guess, it returns a random word from the list
def GetRandomWord():
    words = ["titan","combination","gracious","javascript","carbine","elucidate","alabama","alaska","arizona","arkansas","california",
    "colorado","connecticut","delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana","maine","maryland","massachusetts","michigan","minnesota"
    "mississippi","missouri","montana","nebraska","nevada","ohio","oklahoma","oregon","pennsylvania","tennessee","texas","utah","vermont","virginia","washington","wisconsin","wyoming",
    "christmas","santa","fragile","information","technology","dinosaur","penguin","discover","complexity","enamoured","enumeration","envelope","fantastic","centenial","point","reflection","lexicon","solar","zenith"]
    randomWord = random.choice(words)
    return randomWord
#this function is used to start a game of hangman
def gameStarted():
    #initialize the variables
    word = GetRandomWord()
    playing  = 1
    guess = 6
    temp = []
    win = 0
   #create a list of underscores the same length as the word
    for i in range(len(word)):
        temp.append('')
        
    print("\n")
    print("*********************************************************")
    print("The word you have to guess is: ",len(word),"letters long  (type your guess as a lower case character!)")
    print("\n")
    while(playing == 1):
        letter = input("guess here: ")
        
        if(len(letter) > 1):
            print("\n")
            print("*********************************************************")
            print("You have to guess only one character!")
            print("********************************************************")
            print("\n")
            continue
        if(letter in word):
            if(letter in temp):
                print("*********************************************************")
                print("You have already guessed this letter!")
                print("********************************************************")
                continue
            #temp[word.index(letter)] = letter
            for i in range(len(word)):
                if word[i] == letter:
                    temp[i] = letter               #find letter to insert in temp if correct guess
            print("\n")
            print("You guessed the letter correctly!")
            print("\n")
            if('' not in temp):
                print("*********************************************************")
                print("You won the game!")
                print("********************************************************")
                print("*********************************************************")
                print("The word was: ",word)
                print("********************************************************")
                print("\n")
                playing = 0
                win = 1      # setting win to 1 to end the game if the user wins
                break
            print("*********************************************************")
            print("The word now looks like this: ",temp)
            print("********************************************************")
            print("*********************************************************")
            print("You have ",guess," tries left")
            print("********************************************************")
            print("\n")
        else:
            guess = guess - 1   # decrement the number of tries left (if the user guesses wrong)
            print("\n")
            print("*********************************************************")
            print("You guessed the letter incorrectly!")
            print("\n")
            print("current letters guessed correctly: ",temp)
            print("\n")
            playing = Hangman(guess,playing)   #call the hangman function to progess the game and the varibles
    if(win == 1):
        print("would you like to play again? (y/n)")
        playAgain = input()
        if(playAgain == 'y'):
            gameStarted()
        elif(playAgain == 'n'):
            print("*********************************************************")
            print("Thanks for playing!")
            print("********************************************************")
            print("\n")
            return
    else:
        #tell the user that they used their last guess and give the option to play again
        if(guess == 0):
            print("\n")
            print("*********************************************************")
            print("You lost the game!")
            print("The word was: ",word)
            print("********************************************************")
            print("\n")
        again = input("Do you want to play again? (y/n)")  # check if user would like to play again and  call the function within itself to start a new game
        if(again == "y"):
            gameStarted()
        else:
            print("\n")
            print("*********************************************************")
            print("Goodbye!")
            print("********************************************************")
            print("\n")
            exit()
        #main function
def main():
    print("*********************************************************")
    print("Hi there! Welcome my hangman game!")
    print("********************************************************")
    print("\n")
    game = input("press 1. to play the game\npress 2. to exit\n")
    if(game == "1"):
        print("\n")
        print("*********************************************************")
        print("Let's start the game!")
        print("********************************************************")
        print("\n")
        print("*********************************************************")
        print("The rules of the game are simple")
        print("********************************************************")
        print("\n")
        print("*********************************************************")
        print("You have to guess the word in less than 6 tries")
        print("********************************************************")
        #intially call the gameStarted function
        gameStarted()
        # error handling
    elif(game != "2"or"1"):
        print("\n")
        print("*********************************************************")
        print("You have to enter 1 or 2!")
        print("********************************************************")
        main()
    else: 
        print("goodbye!")
        exit()
        
main()

