import time
from graph import Graph

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
        nodes = []
    
    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node 

        if current_head != None:
            current_head.set_prev_link(new_head)
            new_head.set_link(current_head)
        
        self.head_node = new_head 
        nodes.append(new_value[0])

        if self.tail_node == None:
            self.tail_node = new_head 


    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node 

        if current_tail != None:
            current_tail.set_link(new_tail)
            new_tail.set_prev_link(current_tail)
        
        self.tail_node = new_tail 
        nodes.append(new_value[0])

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
                return current_node.get_value()[1]
            current_node = current_node.get_link()




server_base = DoubleLinkedList()


def initial_prompt(server_base=server_base):
    print('Welcome to Connection! ')
    print("You have 5 options: ")
    time.sleep(0.1)
    print("-"*24)
    print('/add_server: To add a new server to track your modems/routers')
    time.sleep(0.2)
    print('-'*24) 
    print('/remove_server: To remove a server/network from the software')
    time.sleep(0.2)
    print("-"*24)
    print("/view_servers: To view all the servers registered in the software ")
    time.sleep(0.2)
    print('-'*24)
    print("/access_server: To analyze and access one of the servers registered on the server" )
    time.sleep(0.2)
    print('-'*24)
    print("/quit: To quit the program")
    

    start = True 
    while start:
        user_prompt = input(':')
        
        if user_prompt == '/add_server':
            server_name = input('Please type in the name of the server ')
            
            if not server_name in server_base.nodes:
                server_extra_info = input('Is there any other extra info you would like to add (*Type \'None\' if not applicable): ')
                
                if server_extra_info == None:
                    new_server = [server_name, Graph()]
                else:
                    new_server = [server_name, Graph(), extra_info]

            server_base.add_to_tail(new_server)
            time.sleep(0.2)
            print("Your Server has been added. To view it, please type \'/view_servers\' or to access it, type \'/access_server\'")
        
        elif user_prompt == '/remove_server':
            sever_name = input('Please type in the name of the server: ')
            if not server_name in server_base.nodes:
                print("That server does not seem to be registered in this software currently ")
                time.sleep(0.1)
                print("Type \'/add_server\' to do so ")
                time.sleep(0.1)
            else:
                server_base.remove_by_value(server_name)
                time.sleep(0.1)
                print('Server has been successfully deleted ')
        
        elif user_prompt == '/view_servers':
            if len(server_base.nodes) == 0:
                print("There currently is no server registered on the software yet. ")


