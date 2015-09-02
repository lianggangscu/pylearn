#!/usr/bin/env python
#Filename:static.py

class Person:
	'''represents a person'''
	population=0 # class variable

	def __init__(self,name):
		self.name = name
		print("name:%s"%self.name)
		Person.population +=1
		
		if Person.population==1:
			print("Congratulation you are the first person")

	def __del__(self):
		'''destory class'''
		print("See u %s"%self.name)
		Person.population -=1

		if Person.population == 0:
			print("I am the last person")
		else:
			print("There are still %d person" %Person.population)

	def sayhi(self):
		print("hello %s"%self.name)

	def howmany(self):
		if Person.population == 1:
			print("you are the only person")
		else:
			print("there are %d person"%Person.population)

p = Person('gang')
s = Person('yaolin')
s.sayhi()
s.howmany()
