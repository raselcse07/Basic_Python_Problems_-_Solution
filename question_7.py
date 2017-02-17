#! /usr/bin/python3

'''
Question 7:

Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.

Name : Rasel Miah
Batch: Django-1

'''


def binary_search(item,_list):

	index=None
	start=0
	end=len(_list)-1

	while start <= end:

		midpoint=(start+end)//2

		if item == _list[midpoint]:

			index=midpoint
			end=midpoint-1

		elif item > _list[midpoint]:
			start=midpoint+1
		
		else:

			end=midpoint-1

	return index


my_list=[10,10,20,20,30,40,50,60,70,80,200,250,100,380,400,90]
sorted_list=sorted(my_list)


if __name__ == '__main__':
	
	n=int(input())

	print(binary_search(n,sorted_list))

