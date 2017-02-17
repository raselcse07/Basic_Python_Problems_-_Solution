#! /usr/bin/python3

'''
Question-4 :

With a given integral number n, 
write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.

Suppose the following input is supplied to the program:

8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Name : Rasel Miah
Batch: Django-1

'''

def create_dict(n):

	my_dict={}

	for i in range(1,n+1):

		my_dict[i]=i*i

	return my_dict



if __name__ == '__main__':

	user_input=int(input())

	print(create_dict(user_input))

