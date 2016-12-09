
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
now = datetime.datetime.now()

name = input()
age = int(input())

print ('current age of {} is {}'.format(name,age))
print('Current year is {}'.format(now.year))
dob = now.year - age
print('You will be 100 years old on {}'.format(dob+100))

