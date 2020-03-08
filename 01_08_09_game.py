'''
authors: AJ Riley
editors: Moshood Olawale
'''
#!/usr/bin/env python3

import random

player_name = input("Hello, What is your username? ")

print("Hello! " + player_name + ". You are welcome to \"The Minder Game Corner\"" )
question = input("Would you like to play a game? [Yes (y)/No (n)]: ")

if question.lower() == "n": #in case of capital letters is entered
    print("oh..okay")
    exit()
elif question.lower() == "y":
    

    #game starts
    '''
    advanced  contribution
    allow player to set the range of guess, chances which can be used to calculate their accuracy
    reminder  if non-negative is allowed from the print meassage 
    '''
    print("Enters the range of numbers your would like the computer to guess and the number of trial(s) to play the game")
    try:
        start = int(input("Start: "))
        end = int(input("End: "))
        chances = int(input("Chances: "))

        if (start > end):
            start, end = (end, start)
    except:
        print("Only enter integer numbers")
        exit()

    number = random.randint(start, end)
    trial = 0
    win = False # setting a win flag to false

    print("\n I'm thinking of a number between {} & {} .....\n".format(start, end))

    while not win and trial < chances:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
        guess = int(input("Have a guess: "))
        trial = trial + 1
        remainder = chances - trial

        if guess == number:
            win = True    # set win to true when the user guesses correctly.
        elif guess < number:
            print("****************\n Nope! Your guess is lower than the number. \n","Trial left:", remainder,"\n")
        elif guess > number:
            print("****************\n Nope! Your guess is higher than the number. \n","Trial left:", remainder,"\n")
        elif remainder > 0:
            print("\n Try again!")
    
    # if win is true then output message
    if win == True:
        print("Congrats, you guessed correctly. The number was indeed {}".format(number))
        print("it had taken you {} trial".format(trial))
    else:
        print("*** Game Over! *** The number was {}".format(number))

    #game IQ report score - chances, trials, number range 


else:
    print("You need to enter yes (y) or no (n)")

