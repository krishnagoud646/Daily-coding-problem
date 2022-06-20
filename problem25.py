"""Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).

"""

class node:
	def __init__(self, value):
		self.left = None
		self.data = value
		self.right = None

# This function receives a node of the syntax tree
# and recursively evaluate it


def evaluateExpressionTree(root):

	if root.left is None and root.right is None:
		return int(root.data)

	# evaluate left tree
	left_sum = evaluateExpressionTree(root.left)

	# evaluate right tree
	right_sum = evaluateExpressionTree(root.right)

	# check which operation to apply
	if root.data == '+':
		return left_sum + right_sum

	else:
		return left_sum * right_sum

if __name__ == '__main__':

	# creating a sample tree
	root = node('*')
	root.left = node('+')
	root.left.left = node('3')
	root.left.right = node('2')
	root.right = node('+')
	root.right.left = node('4')
	root.right.right = node('5')
	print (evaluateExpressionTree(root))




