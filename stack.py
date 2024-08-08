class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

class Stack:

    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def push(self, data):
        new_node = Node(data= data, next= self._head)
        self._head = new_node
        self._size +=1

    def pop(self):
        top_node = self._head
        self._head = self._head.next
        self._size = 1
        top_node.next = Node
        return top_node

    def peek(self):
        return self._head

    def is_empty(self):
        return self._head is not None
    
    def size(self):
        return self._size
    
    def display(self):
        current_node = self._head
        while current_node is not None:
            if current_node is self._head:
                print(f"{current_node} <-- head")
            else:
                print(current_node)
            current_node = current_node.next

stack = Stack()

stack.push(11)
stack.push(22)
stack.push(33)
stack.display()
stack.pop()
stack.pop()
stack.display()
stack.peek()
stack.display()
print(f"Длинна : {stack.size()}")
