#!/usr/bin/env python
#Filename:guess1.py

number = 23
running = True

while running:
	guess = int(raw_input("please input number:"))
	
	if number == guess:
		print("Congratulation,you do it!")
		print("but, you will not win any prize!")
		running = False
	elif guess < number:
		print("you guess is a little smaller")
	else:
		print("you guess is a little bigger!")

print("Done")
