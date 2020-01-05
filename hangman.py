import random
name=input('Enter your name?')
print("Hello, "+name+" Time to play Hangman!!")
# create a variable to set secret
word="secret"

# create a variable with empty value
guesses=''

# determine the number of turns
turns=10

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=' ')
        else:
            print("_",end=' ')
            failed+=1

    if failed==0:
        print("Congratulations ",name," You Won !!")
        break

    guess=input('Guess your character: ')
    guesses+=guess

    if guess not in word:
        turns-=1
        print("Your guess is wrong")

        print('you have ',turns,' more turns')
        if turns==0:
            print("Oops ",name,' You loose !!')







