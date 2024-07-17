#   Program chooses 2 random integers between 0 and 10
#   Pose an question for the user
#   Compare the user's answer to the correct answer
#   Give feedback: correct or incorrcet

#Version 2: Adding a loop and a score counter

import random   # random module

from FileReadWrite import * #import ability to read/write our score
DATA_FILE_PATH = "AddingGameScore.txt"

#Initial creation of score counter
if not fileExists(DATA_FILE_PATH):
    # The file was not found, this is the first time we are running the program
    print("Hello! You must be new here") # first time intro
    score = 0
    writeFile(DATA_FILE_PATH,str(score))
else:
    score = readFile(DATA_FILE_PATH)
    score = int(score)
    print("Welcome back Player! Your current score is: ",score)


while True:

    firstNumber = random.randrange(0,11)
    secondNumber = random.randrange(0,11)

    question = input("What is: " + str(firstNumber) + " + " + str(secondNumber) + "? Press Enter to quit: ")

    if question == "":
        print("Goodbye! See you next time")
        break
    else:
        
        question = int(question)

        answer = firstNumber + secondNumber


        if question == answer:
            print("Yes that's right")
            score = score + 2
        else:
            print("Sorry that's not correct. The right answer was:",answer)
            score = score - 1


        
        print("Your current score is:",score)
textToWrite = str(score)
writeFile(DATA_FILE_PATH,textToWrite)
        
