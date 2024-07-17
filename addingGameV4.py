#   Program chooses 2 random integers between 0 and 10
#   Pose an question for the user
#   Compare the user's answer to the correct answer
#   Give feedback: correct or incorrcet

#Version 4: Saving lots of data

import random   # random module

from FileReadWrite import * #import ability to read/write our score
DATA_FILE_PATH = "AddingGameData.txt"

#Initial creation of score counter
if not fileExists(DATA_FILE_PATH):
    # The file was not found, this is the first time we are running the program
    userName = input("You must be new here, please enter your name: ")
    score = 0
    nProblems = 0
    nCorrect = 0

    print("To quit the game, press ENTER and your info will be saved")
    print("Ok",userName,"let's get started ...")
    print()
    
else:
    savedDataString = readFile(DATA_FILE_PATH) # read the whole file into a list variable
    savedDataList = savedDataString.split(',') # turn that into a list
    userName = savedDataList[0]
    score = savedDataList[1]
    score = int(score)
    nProblems = savedDataList[2]
    nProblems = int(nProblems)
    nCorrect = int(savedDataList[3]) # can do both in a combined step

    print("Welcome back", userName, "nice to see you again!")
    print("Your current score is: ",score)
    print()



while True:

    firstNumber = random.randrange(0,11)
    secondNumber = random.randrange(0,11)
    answer = firstNumber + secondNumber

    question = input("What is: " + str(firstNumber) + " + " + str(secondNumber) + "? Press Enter to quit: ")

    if question == "":
        print("Goodbye! See you next time")
        break
    else:
        
        question = int(question)
        nProblems = nProblems + 1

        if question == answer:
            print("Yes that's right")
            score = score + 2
            nCorrect = nCorrect + 1
        else:
            print("Sorry that's not correct. The right answer was:",answer)
            score = score - 1

        print("Your current score is:",score)
        print()
print("Thanks for playing")
print()
print("You have tried", nProblems, "problems and you have correctly answered", nCorrect)

# Make a list of the userName, userScore, nProblems, nCorrect then
# create a string from that using join

dataList = [userName, str(score), str(nProblems), str(nCorrect)]
outputText = ','.join(dataList)

writeFile(DATA_FILE_PATH, outputText)
        
