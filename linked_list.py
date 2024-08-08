class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size = 0
        self.linked_list = []   

    def is_empty(self):
        if self._tail_node is None:
           return True

    def append(self, item):
        new_node_item = Node(item)
        if LinkedList.is_empty(self):
           self._head_node = new_node_item
           self._tail_node = new_node_item
        else:
           self._tail_node.next = new_node_item
           new_node_item.prev = self._tail_node
           self._tail_node = new_node_item
        print(f"В конец списка добавлен элемент {item}")
        self._size += 1
        self.linked_list.append(item)

    
    def display(self, reverse=False):
        linked_list = []
        if reverse:
            item = self._tail_node
            while item:
                linked_list.append(item.data)
                item = item.prev
        else:
            item = self._head_node
            while item:
                linked_list.append(item.data)
                item = item.next
        return print(linked_list)
  
    def prepend(self,item):
        new_node_item = Node(item)
        if LinkedList.is_empty(self):
           self._head_node = new_node_item
           self._tail_node = new_node_item
        else:
            new_node_item.next = self._head_node
            self._head_node.prev = new_node_item
            self._head_node = new_node_item
        print(f"В начало списка добавлен элемент {item}")
        self._size += 1
        prepend_list = []
        prepend_list.append(item)
        for i in self.linked_list:
            prepend_list.append(i)
        self.linked_list = prepend_list

    def insent(self,item,index):
        new_node_item = Node(item)
        if index == 0:
           self.prepend(item)
           return print(f"Элемент {item} вставле на позицию {index}.")
        elif index == self._size:
           self.append(item)
           return print(f"Элемент {item} вставле на позицию {index}.")
        else:
            current = self._head_node
            for i in range(index-1):
                current = current.next
            new_node_item.prev = current.prev
            new_node_item.next = current
            current.prev.next = new_node_item
            current.prev = new_node_item
            self._size +=1
            return print(f"Элемент {item} вставле на позицию {index}.")
   
    def delete(self, item):
        current = self._head_node
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head_node = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail_node = current.prev
                self._size -= 1
                print(f"{item} удален из списка.")
                return
            current = current.next
        print(f"{item} не найден в списке.")

    def __getitem__(self, i):
        item = self._head_node
        for j in range(i):
            item = item.next
        return print(f"Значение элемента с индексом {i} является {item.data}")

# append(item) для добавления элемента в конец списка
item = LinkedList()
item.append(11)
item.append("Roma")
item.append(True)
item.prepend(True)
item.prepend("Roma")
item.prepend(11)
item.display(False)

# display(reverse=False) для вывода списка от начала до конца,
# если reverse=False, или от конца до начала, если True.

item.insent("Alexandr",4)
item.insent("Roman",4)
item.display()
item.delete("Roman")
item.display()
#__getitem__(i) для получения элемента списка на позиции i.
item.__getitem__(1)