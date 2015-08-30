#!/usr/bin/env python
#Filename: global.py

def test():
	global x
	print("before change x is %d:"%x)
	x=2
	print("after change x is %d:"%x)

x=100
print("befor change")
print("x is %d"%x)
print("after chang")
print("x is %d"%x)
