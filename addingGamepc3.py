#   Program chooses 2 random integers between 0 and 10
#   Pose an question for the user
#   Compare the user's answer to the correct answer
#   Give feedback: correct or incorrcet

#Version 2: Adding a loop and a score counter

"""Score tracking

from FileReadWrite import *

DATA_FILE_PATH = "AddingGameScore.txt"

if not fileExists(DATA_FILE_PATH):
    # The file was not found, this is the first time we are running the program
    print("First time - creating the data file.") # for testing
    score = "0"
    writeFile(DATA_FILE_PATH, score)

else:

    # The file was found. We have run this program before
    score = readFile(DATA_FILE_PATH)
    print("Found the file, data read was: ",count) # for testing
    score = int(count)
    score = score + 1
    textToWrite = str(score)
    writeFile(DATA_FILE_PATH,textToWrite)"""

from FileReadWrite import *
DATA_FILE_PATH = "AddingGameScore.txt"

import random

if not fileExists(DATA_FILE_PATH):
    # The file was not found, this is the first time we are running the program
    print("Hello! You must be new here") # first time intro
    score = "0"
    writeFile(DATA_FILE_PATH, score)
else:
    score = readFile(DATA_FILE_PATH)
    score = int(score)
    print("Welcome back Player! Your current score is: ",score)


while True:

    firstNumber = random.randrange(0,11)
    secondNumber = random.randrange(0,11)

    question = input("What is: " + str(firstNumber) + " + " + str(secondNumber) + "? Press Enter to quit: ")

    if question == "":
        print("Goodbye!")
        break
    else:
        
        question = int(question)

        answer = firstNumber + secondNumber

        score = readFile(DATA_FILE_PATH)
        score = int(score)

        if question == answer:
            print("Yes that's right")
            score = score + 2
        else:
            print("Sorry that's not correct. The right answer was:",answer)
            score = score - 1


        textToWrite = str(score)
        writeFile(DATA_FILE_PATH,textToWrite)
        print("Your current score is:",score)
