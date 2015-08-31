#!/usr/bin/env python
#Filename:file.py

s ='''long long ago
there lived  a beauty named snowwhite'''

f = file('lg.txt','w')
f.write(s)
f.close

f= file('lg.txt')

while True:
	line = f.readline()
	if len(line)==0:
		break
	
	print(line)

f.close()
