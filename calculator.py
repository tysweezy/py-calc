#Calculator in Python
#calculator.py
#Author: Tyler Souza

import sys
import math

#Greets user
print 'Hello and welcome'

def add():
	print 'Ok. Add...'
	ex1 = int(raw_input('Enter a value: '))
	ex2 = int(raw_input('Enter another value: '))
	return ex1 + ex2
	
def subtract():
	print 'Ok. Subtract..'
	ex1 = int(raw_input('Enter a value: '))
	ex2 = int(raw_input('Enter another value:'))
	return ex1 - ex2
	
def multiply():
	print 'Ok. Multiply...'
	ex1 = int(raw_input('Enter a value: '))
	ex2 = int(raw_input('Enter another value: '))
	return ex1 * ex2
	
def divide():
	print 'Ok. Divide...'
	ex1 = float(raw_input('Enter a value: '))
	ex2 = float(raw_input('Enter another value: '))
	return ex1 / ex2
	
	

print 'OPERATORS: '
print 'Press "1" to add'
print 'Press "2" to subtract'
print 'Press "3" to multiply'
print 'Press "4" to divide'
print 'Press "0" to exit'

#determines the operator key
while True:
	op = int(raw_input('Select the correct key that represents the operator: '))
	if op == 1:
		print add()
		
	elif op == 2:
		print subtract()
	
	elif op == 3:
		print multipy()
		
	elif op == 4:
		print divide()
		
	elif op == 0:
		print 'quiting...'
		sys.exit()
		
	else:
		print 'Please choose an operator'

		


