## making a singly linked list api


## Making the linked list node

class ListNode:
    '''A node in a singly linked list '''

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_head(self,data):
        ''' Insert at the beginning'''
        self.head = ListNode(data,self.head)

    
    def insert_last(self,data):
        '''Insert at the last of the list'''
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data)

    def __repr__(self):
        '''Returns the string representation of linked list'''
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '{'+  ", ".join(nodes) +'}'


l = SinglyLinkedList()
l.insert_head(2)
l.insert_last(3)
l.insert_head(5)
l.insert_head(4)
l.insert_last(6)

print(l)


