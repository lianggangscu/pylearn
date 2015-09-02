#!/usr/bin/env python
#Filename:school.py

''' demostrate how to use 
    the attribution of inherient'''

class Schoolmember:
	population = 0 # define the class variable
	'''define the base class'''

	def __init__(self,name,age):
		'''construct function'''
		
		self.name = name
		self.age = age
		Schoolmember.population +=1

	def __del__(self):
		print("See u %s" %self.name)

	def tell(self):
		print("name:%s" %self.name)
		print("age:%d" %self.age)

class Teacher(Schoolmember):
	'''the teacher inherent class'''
	
	def __init__(self,name,age,salary):
		Schoolmember.__init__(self,name,age)
		self.salary = salary

	def tell(self):
		Schoolmember.tell(self)
		print("salary:%d"%self.salary)

class Student(Schoolmember):
	'''define the student inherent class'''
	
	def __init__(self,name,age,grade):
		Schoolmember.__init__(self,name,age)
		self.grade = grade


	def tell(self):
		Schoolmember.tell(self)
		print("grade:%d"%self.grade)



t = Teacher("gang",39,1000)
s = Student("yaolin",8,100)

t.tell()
s.tell()
