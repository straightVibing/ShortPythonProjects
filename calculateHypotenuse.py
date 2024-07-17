# Calculate hyptenuse func

def calculateHypotenuse(side1,side2):
    side1 = float(side1)
    side2 = float(side2)
    hypot = ((side1**2)+(side2**2))**0.5
    return hypot

firstTriangleSide1 = input('Enter side 1: ')
firstTriangleSide2 = input('Enter side 2: ')

hypot1 = calculateHypotenuse(firstTriangleSide1,firstTriangleSide2)
#call function to do calc

print('The hypotenuse of the first triangle is: ',hypot1)

secondTriangleSide1 = input('Enter the first side: ')
secondTriangleSide2 = input('Enter the second side: ')
hypot2 = calculateHypotenuse(secondTriangleSide1,secondTriangleSide2)
# call function to do calc


print('The hypotenuse of the second triangle is: ',hypot2)
