'''stack by linkde list'''
class Node:
    '''class for nodes'''
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    '''stack'''
    def __init__(self):
        '''init stack'''
        self.top = None

    def push(self, value):
        '''push node to stack'''
        node = Node(value)
        if not self.top:
            self.top = node
        node.next = self.top
        self.top = node

    def pull(self):
        '''pull node'''
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None
