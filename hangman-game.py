###########################################
#The classic HANGMAN game.
#Hangman is a game where the user/player has to guess a word correctly within limited guesses/chances.
#Suppose, the word is ELEPHANT.
#To the player, it will appear as a sequence of underscores(_).
# E.g, _ _ _ _ _ _ _ _
#the word is of length 8 and you have 5 guesses/chances left!

#If the player guesses E or e, then the dashes will get filled, such as,
# E.g, E _ E _ _ _ _ _

#If the player makes a wrong guess, such as a 'M', that doesn't exist in the word 'ELEPHANT', the player gets a visual representation of hangman looking figure appearing stroke by stroke.
#Also, number of guesses left is shown!
#Therefore, if player can guess the correct word before the chances/guessees run out,
# HE WON THE GAME!

#otherwise, if he can't guess within the limited chances/guesses,
# GAME OVER!
##########################################

import random
#this method displays the hangman based on number of guesses left
def showHangman(n):
    if n == 5:
        s = "YOU HAVE GOT 5 CHANCES LEFT!"
    elif n == 4:
        s = ''' ______
|      |
|
|
|
|
|
|
-----

YOU HAVE GOT 4 CHANCES LEFT!'''
    elif n == 3:
        s = ''' ______
|      |
|      O
|
|
|
|
|
|
-----

YOU HAVE GOT 3 CHANCES LEFT!'''
    elif n == 2:
        s = ''' ______
|      |
|      O
|     /|\\
|
|
|
|
|
|
-----

YOU HAVE GOT 2 CHANCES LEFT!'''
    elif n == 1:
        s = ''' ______
|      |
|      O
|     /|\\
|      |
|
|
|
|
-----

YOU HAVE GOT 1 CHANCE LEFT!'''
    elif n == 0:
        s = ''' ______
|      |
|      O
|     /|\\
|      |
|     / \\
|    /   \\
|
|
|
|
-----

!!GAME OVER!!'''
    else:
        pass

    return s   

def find(s,ch):
    for i,c in enumerate(s):
        if c == ch:
            yield i
 
#main body of the program
def main():
    words =["eagle","elephant","rabbit","tiger","crocodile","panther","koala","sloth","rhinoceros","hippopotamus","vulture","snake","horse","dolphin","jackal","orangutan","chimpanzee","panda","peacock","llama","whale","shark","sheep","iguana","penguin"]
    s = random.choice(words)
    already_guessed = ""
    answer = []
    for _ in range(len(s)):
        answer.append("_ ")
    print(*answer)
    chances = 5
    print("chances left =",chances)

    while(True):
            if chances == 0:
                print("THE COMPLETE WORD IS",s)
                break
            guessed = input("\nit's your turn to guess a letter: ").lower()
            
            if ord(guessed) >= 97 and ord(guessed) <= 122:
                if guessed in s:
                    if guessed in already_guessed:
                        print("YOU ALREADY GUESSED THIS LETTER!")
                    else:
                        already_guessed += guessed
                        indices = list(find(s,guessed)) #<---- here add the indices code
                        for _ in indices:
                            answer[_] = guessed
                        print(*answer)
                        if answer == list(s):
                            print("\nCONGRATS! YOU WON THE GAME!")
                            print("THE COMPLETE WORD IS",s)
                            break
                else:
                    chances -= 1
                    print("\nWRONG GUESS")
                    print(showHangman(chances))
                    print(*answer)
            else:
                print("\nNUH UH! YOU HAVE TO GUESS A LETTER")
                print(*answer)
                chances -= 1
                print(showHangman(chances))
                
            #print("l=",l)

if __name__ == '__main__':
    main()
