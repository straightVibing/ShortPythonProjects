#   Program chooses 2 random integers between 0 and 10
#   Pose an question for the user
#   Compare the user's answer to the correct answer
#   Give feedback: correct or incorrcet

#Version 2: Adding a loop and a score counter

import random

score = 0

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


        if question == answer:
            print("Yes that's right")
            score = score + 2
        else:
            print("Sorry that's not correct. The right answer was:",answer)
            score = score - 1


        
        print("Your current score is:",score)
