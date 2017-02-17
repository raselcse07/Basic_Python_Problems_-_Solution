#! /usr/bin/python3

'''

Question 9:
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and 
rabbits in a farm. How many rabbits and how many chickens do we have?

Name : Rasel Miah 
Batch: Django-1

'''


#Solution

'''
Head Equation, C+R =35..........(1)
Legs Equcation 2C+4R=94..........(2)

(1)x2-(2)--> 2C+2R-2C-4R=70-94=>2R=24=>12

So, Number of Rabbits = 12
And Number of Chicken =35-12=23

We will solve this problem with Python.For this we will 
write (1) & (2) as below and solve this Matrix using python 
"numpy" module.

|1 1|	|C|	  |35|
|	|	| | = |	 |
|2 4|	|R|	  |94|



'''

import numpy as np

def calculate_chicken_and_rabbit(heads,legs):


	A=np.array([[1,1],[2,4]])
	B=np.array([heads,legs])

	Z=np.linalg.solve(A,B)
	Chicken=int(Z[0])
	Rabbits=int(Z[1])

	print("Chicken : ",Chicken)
	print("Rabbits : ",Rabbits)


if __name__ == '__main__':

	calculate_chicken_and_rabbit(35,94)



