#!/usr/bin/python3

'''
Question-14:

Using the find_successor method, write a non-recursive inorder traversal for a binary search tree.

'''

class Node:

	def __init__(self,data):

		self.data=data
		self.left=None
		self.right=None



def binaryTree(root):

	current=root
	stack=[]
	done=0

	while not done:

		if current is not None:

			stack.append(current)
			current=current.left

		else:

			if len(stack)>0:

				current=stack.pop()
				print(current.data)

				current=current.right
			
			else:

				done=1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


if __name__ == '__main__':
	
	binaryTree(root)





