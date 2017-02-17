#! /usr/bin/python3

'''
Question-2:

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.

Suppose the following input is supplied to the program:
8

Then, the output should be:
40320

Name : Rasel Miah
Batch:Django-1

'''

def compute_factorial(number):

	if number == 1:

		return 1

	return number * compute_factorial(number-1)


if __name__ == '__main__':
	

	n=int(input())

	print(compute_factorial(n))