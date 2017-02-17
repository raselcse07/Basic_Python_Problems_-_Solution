#! /usr/bin/python3

'''

Question 13:

Write a program that accepts a sequence of 
whitespace separated words as input and prints 
the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world

Name : Rasel Miah
Batch: Django-1

'''

def remove_duplicate(_list):

	sequence_duplicate=[]
	sequence=[]

	for i in _list:

		sequence_duplicate.append(i)

	for i in sequence_duplicate:

		if i not in sequence:
			sequence.append(i)


	sequence=sorted(sequence)

	return " ".join(sequence)

if __name__ == '__main__':
	
	user_input=map(str,input().split())

	print(remove_duplicate(user_input))
