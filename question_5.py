#!/usr/bin/python3

'''

Question-5:

Question 5:

Create an implementation of a queue that would have 
an average performance of O(1) for enqueue and dequeue operations.

Name : Rasel Miah
Batch: Django-1

'''

class Queue:

	def __init__(self):

		self.items=[]

	def isEmpty(self):

		return self.items == []

	def enqueue(self,n):

		return self.items.insert(0,n)

	def dequeue(self):

		return self.items.pop()

	def size(self):

		return len(self.items)


	
q=Queue()

print(q.isEmpty())
q.enqueue(4)
q.enqueue('String')
q.enqueue('ABC')
q.enqueue(10)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())