class Node:
    '''class node'''
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
        else:
            node.next = self.top
            self.top = node

    def pull(self):
        '''pull node'''
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None

class MyQueue:
    '''class queue by stack'''
    def __init__(self):
        '''init'''
        self.main = Stack()
        self.copy = Stack()        

    def push(self, x: int) -> None:
        '''push node to queue'''
        self.main.push(x)

    def pop(self) -> int:
        value = None
        while self.main.top:
            if not self.main.top.next:
                value = self.main.top.value
            else:
                self.copy.push(self.main.top.value)
            self.main.pull()
        current = self.copy.top
        while current:
            self.main.push(current.value)
            self.copy.pull()
            current = current.next

        return value

    def peek(self) -> int:
        value = None
        while self.main.top:
            if not self.main.top.next:
                value = self.main.top.value
            self.copy.push(self.main.top.value)
            self.main.pull()
        current = self.copy.top
        while current:
            self.main.push(current.value)
            self.copy.pull()
            current = current.next

        return value

    # def empty(self) -> bool:

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_1 = obj.peek()
# param_2 = obj.pop()
print(param_1)
# param_3 = obj.peek()
# param_4 = obj.empty()