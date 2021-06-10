class Node:
    def __init__(self, value, link=None, prev_link=None):
        self.value = value 
        self.link = link  
        self.prev_link = prev_link 


    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link 

    def set_prev_link(self, new_link):
        self.prev_link = new_link 

    def get_prev_link(self):
        return self.prev_link 

class DoubleLinkedList:
    def __init__(self):
        self.head_node = None 
        self.tail_node = None 
        self.nodes = []
    
    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node 

        if current_head != None:
            current_head.set_prev_link(new_head)
            new_head.set_link(current_head)
        
        self.head_node = new_head 
        self.nodes.append(new_value[0])

        if self.tail_node == None:
            self.tail_node = new_head 


    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node 

        if current_tail != None:
            current_tail.set_link(new_tail)
            new_tail.set_prev_link(current_tail)
        
        self.tail_node = new_tail 
        self.nodes.append(new_value[0])

        if self.head_node == None:
            self.head_node = new_tail 
        

    
    def remove_head(self):
        removed_head = self.head_node 
        if removed_head == None:
            return None 
        else:
            self.head_node = removed_head.get_link()
            
            if self.head_node != None:
                self.head_node.set_prev_link(None)
            else:
                if removed_head == self.tail_node:
                    self.remove_tail()

        
        return removed_head.get_value()

    
    def remove_tail(self):
        removed_tail = self.tail_node
        if removed_tail == None:
            return None 
        else:
            self.tail_node = removed_tail.get_prev_link()

            if self.tail_node != None:
                self.tail_node.set_link(None)
            else:
                if removed_tail == self.head_node:
                    self.remove_head()
        
        return removed_tail.get_value()

    
    def remove_by_value(self, value):
        node_to_remove = None 
        current_node = self.head_node 

        while current_node:
            if current_node.get_value()[0] == value:
                node_to_remove = current_node 
                break 
            current_node = current_node.get_link()

        if current_node == self.head_node:
            self.remove_head()

        elif current_node == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_link()
            prev_node = node_to_remove.get_prev_link()

            next_node.set_prev_link(prev_node)
            prev_node.set_link(next_node)
    
        return node_to_remove.get_value()

    
    def get_head_node(self):
        return self.head_node

    def stringify_list(self):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                print("-"*24)
                print(current_node.get_value()[0])
            current_node = current_node.get_link()

    
    def linear_search(self, target_value):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value()[0] == target_value:
                return current_node.get_value()
            current_node = current_node.get_link()