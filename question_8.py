#! /usr/bin/python3

'''

Question-8: With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.

Name : Rasel Miah
Batch: Django-1

'''

def remove_duplicate():

	given_list=[12,24,35,24,88,120,155,88,120,155]
	new_list=[]

	for i in given_list:

		if i not in new_list:
			new_list.append(i)

	return new_list

def reverse_list(_list):

	if len(_list) != 1:

		return [_list[-1]]+reverse_list(_list[:-1])
	
	return _list


if __name__ == '__main__':

	print("List After Removing Duplicate : {} ".format(remove_duplicate()))
	print("Original Order Reversed List  : {} ".format(reverse_list(remove_duplicate())))