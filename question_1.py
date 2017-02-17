#! /usr/bin/python3

'''
Question-1:Write a recursive function to reverse a list.

Name : Rasel Miah
Batch:Django-1

'''

def reverse_list(_list):

	if len(_list) != 1:

		return [_list[-1]]+reverse_list(_list[:-1])
	
	return _list
	

if __name__ == '__main__':
	
	my_list=["Item1","Item2","Item3"]

	print(reverse_list(my_list)) 