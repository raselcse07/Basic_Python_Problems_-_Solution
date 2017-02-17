#! /usr/bin/python3

'''
Question 11:

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.

Example

Suppose the following inputs are given to the program:
3,5

Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Name : Rasel Miah
Batch: Django-1

'''

def solution(user_input):

	for i in user_input:

		row=user_input[0]
		col=user_input[1]

	arr=[[x for x in range(col)] for y in range(row)]

	for i in range(row):
		for j in range(col):
			arr[i][j]=i*j

	return arr


if __name__ == '__main__':
 	
 	user_input=list(map(int,input().split(",")))

 	print(solution(user_input)) 