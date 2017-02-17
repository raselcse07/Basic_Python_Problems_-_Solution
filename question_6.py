#! /usr/bin/python3

'''

Question -6 :Write a program which accepts a sequence of 
comma-separated numbers from console and generate a list 
and a tuple which contains every number.

Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Name : Rasel Miah
Batch: Django-1

'''

def make_list_and_tuple():

	numbers=list(map(str,input().split(",")))

	print(numbers)
	print(tuple(numbers))

if __name__ == '__main__':
	
	make_list_and_tuple()