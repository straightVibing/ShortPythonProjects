#   Program chooses 2 random integers between 0 and 10
#   Pose an question for the user
#   Compare the user's answer to the correct answer
#   Give feedback: correct or incorrcet

import random

firstNumber = random.randrange(0,11)
secondNumber = random.randrange(0,11)

question = input("What is: " + str(firstNumber) + " + " + str(secondNumber) + "? ")

question = int(question)

answer = firstNumber + secondNumber

if question == answer:
    print("Yes that's right")
else:
    print("Sorry that's not correct. The right answer was:",answer)


