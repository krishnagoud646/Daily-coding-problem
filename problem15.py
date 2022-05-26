"""This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space."""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next

def find_intersection(list1, list2):

    ptr = list2

    while ptr:
        ptrl1 = list1
        while ptrl1:
            if ptrl1 == ptr:  # found intersection
                return ptrl1.data
            ptrl1 = ptrl1.next
        ptr = ptr.next


def find_intersection_2(list1, list2):# O(M+K)
    #  store ptr2 values to a dictionary
    # return when match found
    dict_visited = {}  # dict of visited nodes

    ptr2 = list1

    while ptr2:
        dict_visited[id(ptr2)] = None  # just add the key no need to store a value
        ptr2 = ptr2.next

    ptr2 = list2
    while ptr2:
        if id(ptr2) in dict_visited:
            return ('intersection point at: {}'.format(ptr2.data))
        ptr2 = ptr2.next

    return 'No Intersection'




if __name__ == '__main__':
    common_tail = Node(8, next=Node(10))
    l1 = Node(1, next=Node(2,next=Node(3, next=Node(7, next=common_tail))))


    l2 = Node(99, next=Node(1, next=common_tail))
    

    print(find_intersection_2(l1,l2))
