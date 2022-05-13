'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

    def print_node(self):
        print(self.data)

    def print_inorder(self):
        if self.left:  # left exists
            self.left.print_inorder()

        print(self.data)

        if self.right:
            self.right.print_inorder()

    def insert(self, data):
        if (data <= self.data): # add to the left
            if self.left == None: # left empty
                self.left = Node(data)
            else: # left exists
                self.left.insert(data)
        else: # add to the right
            if self.right == None: # right empty
                self.right = Node(data)
            else: # right exists
                self.right.insert(data)


def helper(root, root_val):
   if root is None:
       return True
   elif root.val == root_val:
       return helper(root.left,root_val) and helper(root.right, root_val)
   return False

def check_unival(root):
    return helper(root, root.val)

def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if check_unival(root) else left + right

def bottom_up_helper(root, val):

    if root is None:
        return 0, True
    left_count, l_nodes_match = bottom_up_helper(root.left, root.val)
    right_count, r_nodes_match = bottom_up_helper(root.right, root.val) 

    if left_count == 0 and right_count ==0 and l_nodes_match is True and r_nodes_match is True:
        if root.val == val:  
            return 1,True  
        else: 
            return 1,False
    else:
        if (l_nodes_match and r_nodes_match) is True and root.val == val: 
            return 1 + left_count + right_count, True
        elif (l_nodes_match and r_nodes_match) is True and root.val != val:
            return 1 + left_count + right_count, False
        else:
            return left_count + right_count, False


def count_unival_bottom_up(root):
    count, _ = bottom_up_helper(root, root.val)
    return count


if __name__ == '__main__':
    root = Node(0, left= Node(1), right= Node(0, left=Node(1, left=Node(1), right=Node(1)), right=Node(0)))
    print(count_unival_bottom_up(root))
