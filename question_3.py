#! /usr/bin/python3

'''

Question 3:
Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.

Name : Rasel Miah
Batch: Django-1

'''

def tower_hanoi(n,start,helper,end):

	if n>=1:
		tower_hanoi(n-1,start,end,helper)
		print("Move from {} --> {}".format(start,end))
		tower_hanoi(n-1,helper,start,end)




if __name__ == '__main__':
	
	disk=int(input("Enter the number of disk : "))
	start=input("Enter start point : ")
	end=input("Enter end poin : ")
	helper=input("Enter helper : ")

	print("\n")

	tower_hanoi(disk,start,helper,end)



	

