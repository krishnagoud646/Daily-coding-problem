import _ctypes

class node:
    def __init__(self, data, tail):
        self.both = tail  
        self.data = data

class XOR_list:
    head= None 
    tail= None 
    nodes_list = [] 

    def __init__(self):
        pass

    def add(self,element):

        if XOR_list.head is None and XOR_list.tail is None:  
            new_node = node(element, self.tail)
            XOR_list.nodes_list.append(new_node)

            XOR_list.head = self.get_pointer(new_node) 
            XOR_list.tail = self.get_pointer(new_node) 
            new_node.both = 0 
            print('added first node')

        else:
            temp = node(element, self.tail)  
            temp_ptr = self.get_pointer(temp)
            XOR_list.nodes_list.append(temp)
            
            last_node = self.dereference_pointer(self.tail)

            last_node.both = last_node.both ^ temp_ptr  
            XOR_list.tail = temp_ptr
            print('added {} to list'.format(element))

    def get(self, index):
        i = 0
        if i == index:
            return self.dereference_pointer(self.head).data
        if index== 19:
            temp = self.dereference_pointer(self.tail)
            return temp.data
        elif i < 0:
            return 'does not exist'
        else:

            current_ptr = self.head
            pre_ptr = 0 

            while(current_ptr != 0): 
                if i == index:

                    temp = self.dereference_pointer(current_ptr)
                    return temp.data

                link = self.dereference_pointer(current_ptr).both
                next_ptr = pre_ptr ^ link

                pre_ptr = current_ptr
                current_ptr = next_ptr
                i += 1

            return 'does not exist'

    def get_pointer(self, obj):
        return id(obj)

    def dereference_pointer(self, obj_id):
        """ Inverse of id() function. """
        return _ctypes.PyObj_FromPtr(obj_id)



if __name__ == '__main__':
    xor_list = XOR_list()
    xor_list.add('A')
    xor_list.add('B')
    xor_list.add('C')
    xor_list.add('D')

    print(xor_list.get(2))
