#!/usr/bin/env python
#Filename:scanf.py


s = raw_input('pls input a sentence:')

screen_len=80
s_len = len(s)
box_len = s_len +6
left_margin = (screen_len-box_len)//2

print()
print(" "*left_margin+"+"+"_"*box_len+"+")
print(" "*left_margin+"|" +" "*box_len+"|")
print(" "*left_margin+"|"+" "*3+s+" "*3+"|")
print(" "*left_margin+"|"+" "*box_len+"|")

print(" "*left_margin+"+"+"_"*box_len+"+")
