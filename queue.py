# 7_2

class Node:
    def __init__(self , data = []) -> None:
        self.data = data
        self.next = None

class Queue:
    
    def __init__(self):
        self._first_node  = None
        self._last_node =  None
        self._size = 0  
        self.queue = []

    def enqueue(self , item):
        new_node_item = Node(item)
        if self._first_node is None:
            self._first_node = new_node_item
        else:
            self._last_node.next = new_node_item
        self._last_node = new_node_item
        self._size +=1
        print(f"В очередь добавлено элемент {item}")
        self.queue.append(item)

    def dequeue(self):
        if self._first_node is None:
            print("Элементов в очереди нету")
        else:
            delete_item = self._first_node
        self._first_node = self._first_node.next

        self._size -=1
        print(f"Элемент {delete_item.data} удален из очереди")
        self.queue = self.queue[1:]
        return delete_item.data
    
    def front(self):
        if self._first_node is None:
            print("Остудствуют элементы в очереди")
        else: 
            return print(f"Первый элемент в очереди {self._first_node.data}")

    def is_empty(self):
        if self._first_node is None: 
            print("Очередь пуста")
        else:
            print("Очередь не пуста")

    def size(self):
        return(print(f"Количество очередей: {self._size}"))

    def display(self):
        list = []
        for i in range(1, len(self.queue)+1):
            list.append(i)
        serial_number = iter(list)
        for i in self.queue:
            print(f"Номер в очереди {next(serial_number)}  : {i}")

list = Queue()
# Реализация  enqueue(item) для добавления элемента в конец очереди
list.enqueue(11)
list.enqueue("Roma")
list.enqueue(True)
#  dequeue() для удаления и возврата элемента из начала очереди.
list.dequeue()
list.dequeue()
list.dequeue()
# front() для возврата элемента из начала очереди без его удаления.
list.enqueue(11)
list.enqueue("Roma")
list.enqueue(True)
list.dequeue()
list.front()

# is_empty() для проверки, пуста ли очередь.
list.is_empty()

# size() для возврата количества элементов в очереди.
list.size()

# display() для вывода очереди от начала до конца
list.display()
