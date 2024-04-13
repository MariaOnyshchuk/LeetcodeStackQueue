class Node:
    '''class node'''
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    '''class queue'''
    def __init__(self):
        '''init queue'''
        self.head = None

    def push(self, value):
        '''push node to queue'''
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current:
                if not current.next:
                    current.next = node
                    break
                current = current.next

    def pull(self):
        '''pull node from start'''
        if self.head:
            node = self.head
            self.head = self.head.next
            node.next = None
