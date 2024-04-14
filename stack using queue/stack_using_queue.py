'''stack using queue'''

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

class MyStack:
    '''stack using queue'''
    def __init__(self):
        '''init'''
        self.q = Queue()
        self.copy = Queue()  

    def push(self, x: int) -> None:
        '''Pushes element x to the top of the stack.'''
        while self.q.head:
            self.copy.push(self.q.head.value)
            self.q.pull()

        self.q.push(x)

        while self.copy.head:
            self.q.push(self.copy.head.value)
            self.copy.pull()

    def pop(self) -> int:
        '''Removes the element on the top of the stack and returns it.'''
        value = self.q.head.value
        self.q.pull()
        return value

    def top(self) -> int:
        '''Returns the element on the top of the stack.'''
        return self.q.head.value

    def empty(self) -> bool:
        '''Returns true if the stack is empty, false otherwise.'''
        return not self.q.head


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())
# param_3 = obj.top()
# param_4 = obj.empty()