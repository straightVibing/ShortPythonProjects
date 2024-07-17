# Calculate total - repeated

def calculateSum(target):
    total = 0
    nextNumberToAddIn = 1
    while nextNumberToAddIn <= target:
        # add in the next value
        total = total + nextNumberToAddIn
        #increment
        nextNumberToAddIn = nextNumberToAddIn + 1
    return total

answer = 'y' # start off with the value 'y' to go through the the first time
while answer == 'y':
    usersTarget = input('Enter a target number: ')
    usersTarget = int(usersTarget)
    thisTotal = calculateSum(usersTarget) # call our function and get back the answer
    print('The sum of the numbers from 1 to',usersTarget,'is:', thisTotal)

    answer = input('Do you want to try again (y or n): ')

print('Ok bye')
