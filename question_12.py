#! /usr/bin/python3

'''
Question 12:

Write a program that accepts a comma separated sequence of 
words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world

Name : Rasel Miah
Batch: Django-1

'''

def alphabetically_sequence(_list):

	new_sequence=[]

	for i in _list:
		new_sequence.append(i)

	new_sequence=sorted(new_sequence)

	return ",".join(new_sequence)


if __name__ == '__main__':
	
	user_input=map(str,input().split(","))

	print(alphabetically_sequence(user_input))

