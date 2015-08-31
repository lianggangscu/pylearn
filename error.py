#!/usr/bin/env python
#Filename:error.py

import sys

try:
	s = raw_input("pls input a sentence:")
except EOFError:
	print('\n why did you do EOF on me?')
	sys.exit()
except:
	print("other errors")

print("Done")

