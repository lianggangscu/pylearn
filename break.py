#!/usr/bin/env python
#Filename:break.py

while True:
	s = raw_input("enter a string:")
	if s == "quit":
		break
	print("%s \'s length is %d" %(s,len(s)))

print("Done!")
