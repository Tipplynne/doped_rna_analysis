#!/usr/bin/python
#A script to illustrate variable scope in python

total_height = 0 						#global namespace

def triangle():
	def inc_total_height():
		global total_height
		total_height = total_height + height
	for i in range(height):
		print("*" * i)
	inc_total_height()
	print

def square():
	def inc_total_height():
		global total_height
		total_height = total_height + height
	for i in range(height):
		print("*" * height)
	inc_total_height()
	print

height = 3
triangle()
height = 4
square()
height = 5
triangle() 
