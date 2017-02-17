#! /usr/bin/python3

'''
Question 10:

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.

Example

Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24

Name : Rasel Miah
Batch: Django-1

'''

from math import sqrt


def calculation(user_input):

	C=50
	H=30

	Result=[]

	for i in user_input:

		Result.append(str(round(sqrt((2*C*i)/H))))

	return ",".join(Result)


if __name__ == '__main__':

	D=map(float,input().split(","))
	print(calculation(D))