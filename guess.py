#!/usr/bin/env python
#Filename:guess.py

number = 23

guess=int(raw_input("please input a number:"))

if guess==number:
	print("Congratulation,you guess the number")
	print("But you do not win any prize!")
elif guess< number:
	print("your guess if a little smaller!")
else:
	print("your guess if a little bigger")

print("Done")
	
