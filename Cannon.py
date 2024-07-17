#Cannon function just for fun
import math

g = 9.81 #gravitatin constant units ms^-2

print('Welcome! Are you ready to rain down fury upon those against you? Excellent!!!')#cheeky intro
print('')

angleDegrees = input('What is the angle of your cannon in degrees?:')#recieves answer as a string

angleDegrees = float(angleDegrees)#string to floating point number conversion

print('')#adds a line inbetween

velocity = input('What is the velocity of your projectile in ms^-1?:')#receives answer as a string

velocity = float(velocity)#string to floating point number conversion

angleRadians = math.radians(angleDegrees) #degrees to radians conversion using built in function

verticalVelocity = velocity*math.sin(angleRadians)# calculates vertical component on the velocity

TOF = 2*verticalVelocity/g # Time Of Flight

horizontalVelocity = velocity*math.cos(angleRadians)#calculates horizontal compenent of the velocity

horizontalDisplacement = TOF*horizontalVelocity #calculates horizontal displacement

verticalDisplacement = (verticalVelocity**2)/(2*g)#Calculates vertical displacement
print('The projectile will travel:',horizontalDisplacement,'metres and reach a height of',verticalDisplacement,'metres')

