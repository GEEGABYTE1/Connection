import random 


class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link 

class Queue:
    def __init__(self, limit=None):
        self.limit = limit 
        self.size = 0 
        self.head_node = None
        self.tail_node = None 

    def has_space(self):
        if self.limit == None:
            return True 
        else:
            if self.size < self.limit:
                return True 
    
    def is_empty(self):
        return self.size == 0 

    def peek(self):
        if not self.is_empty():
            print(self.head_node.get_value())
        else:
            print('The Queue is empty! ')
    
    def peek_bottom(self):
        if not self.is_empty():
            print(self.tail_node.get_value())
        else:
            print('The Queue is empty! ')

    def enqueue(self, new_value):
        if self.has_space() == True:
            new_node = Node(new_value)

            if self.size == 0:
                self.head_node = new_node
                self.tail_node = new_node 
                print(self.head_node.get_value())
            else:
                self.tail_node.set_link(new_node)
                self.tail_node = new_node 
                print(self.tail_node.get_value())
            
            self.size += 1
        else:
            print("The Queue is Full! ")
    
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head_node

            if self.size == 1:
                self.head_node = None 
                self.tail_node = None 
                print(self.head_node.get_value())
            else:
                self.head_node = item_to_remove.get_link()
                print(self.head_node.get_value())
            
            self.size -= 1
            return item_to_remove 
        
        else:
            print('The Queue is empty! ')


class Test:
    
    def test(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(random.randint(1, 10))
        




testing = Test()

print(testing.test())